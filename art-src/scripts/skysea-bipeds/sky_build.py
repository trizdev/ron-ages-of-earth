import sys, os, json, math
sys.path.insert(0,'/workspace/prehistoric-herds/skysea/scripts')
import bpy
import numpy as np
from mathutils import Vector
from skylib import *
import creatures, bipeds
name=sys.argv[sys.argv.index('--')+1]
ALL={**creatures.CREATURES,**bipeds.CREATURES}; A=ALL[name]
G=A.get('glbdir','/workspace/prehistoric-herds/skysea/glb/'); S=A.get('srcdir','/workspace/prehistoric-herds/skysea/src/')
R='/workspace/prehistoric-herds/'+A['folder']
PD=A.get('pdir','preview')
for d in (PD,'export','tex'): os.makedirs(R+'/'+d,exist_ok=True)
PF=A.get('prefix',''); P=R+'/'+PD+'/'+PF
CAP={}
bpy.ops.wm.read_factory_settings(use_empty=True)
am,an=A['anim']
bpy.ops.import_scene.gltf(filepath=G+f'{am}_{an}.glb')
arm=[o for o in bpy.data.objects if o.type=='ARMATURE'][0]
act=arm.animation_data.action; arm.animation_data.action=None
for pb in arm.pose.bones: pb.matrix_basis.identity()
orig=[o for o in bpy.data.objects if o.type=='MESH' and o.parent==arm][0]
for o in bpy.data.objects:
    if o.type=='MESH' and o.parent is None: o.hide_render=True; o.hide_viewport=True
orig.hide_render=True; orig.name='_orig'
bipeds.BH={b.name:(arm.matrix_world@b.head_local) for b in arm.data.bones}
models={}
for mname,builder in A['models'].items():
    mb=MB(); builder(mb); models[mname]=mb.build(mname,arm,A['rects'][mname] if isinstance(A['rects'],dict) and mname in A['rects'] else A['rects'],A['texsize'])
# textures
texpaths={}
def coat_list(v): return v if isinstance(v,list) else [v]
for texname,cv in A['coats'].items():
    img=None
    for mname,painters in coat_list(cv):
        rects=A['rects'][mname] if mname in A['rects'] else A['rects']
        im2=paint(A['texsize'],rects,painters); img=im2 if img is None else np.where(im2.sum(-1,keepdims=True)>0,im2,img)
    p=R+'/tex/'+texname.replace('.tga','.png'); save_rgb(img,p); texpaths[texname]=p
json.dump({k:v for k,v in texpaths.items()},open(R+'/tex/outtex.json','w'))
for mname,ob in models.items():
    tex=A.get('model_tex',{}).get(mname) or [t for t,cv in A['coats'].items() if any(m==mname for m,_ in coat_list(cv))][0]
    img_material(ob,texpaths[tex],mname+'_mat')
# export + verify
report=[]
for bh3,(mname,srcmodel) in A['exports'].items():
    ob=models[mname]
    report.append(export_verify(arm,ob,G+f'{srcmodel}_plain.glb',R+'/export',bh3,orig))
json.dump(report,open(R+'/export/verify'+('_'+PF.strip('_') if PF else '')+'.json','w'),indent=1)
print('REPORT',json.dumps(report))
bpy.ops.wm.save_as_mainfile(filepath=f"{R}/{A['folder']}{('_'+PF.strip('_')) if PF else ''}_work.blend")
# ------------ renders
cam=setup_scene(ground=A.get('ground',(0.20,0.17,0.10)),gz=A.get('gz',-40))
mainm,maintex=A['preview_model']
for mname,ob in models.items(): ob.hide_render=(mname!=mainm)
img_material(models[mainm],texpaths[maintex],'prev')
def set_act(a,action,frame=None):
    ad=a.animation_data_create(); ad.action=action
    try:
        if action is not None and action.slots: ad.action_slot=action.slots[0]
    except Exception: pass
    if action is None:
        for pb in a.pose.bones: pb.matrix_basis.identity()
    if frame is not None: bpy.context.scene.frame_set(int(frame))
sc=bpy.context.scene
f0,f1=act.frame_range
pf=A.get('pose_frame')   # frame for stills (None = rest pose)
set_act(arm,act if pf is not None else None, (f0+(f1-f0)*pf) if pf is not None else 0)
mn,mx=evaluated_bbox([models[mainm]]); Cc=(mn+mx)/2; Sz=(mx-mn).length
el=A.get('cam_el',1.0)
def view(path,target,d,scale,res):
    d=Vector(d).normalized(); shot(cam,path,Vector(target)+d*Sz*4,target,ortho=scale,res=res)
TQ=A.get('tq_dir',(0.6,-0.85,0.75*el)); GA=A.get('ga_dir',(-0.15,-0.8,1.0))
view(P+'01_three_quarter.png',Cc,TQ,Sz*0.95,(1000,700))
view(P+'06_top_view.png',Cc,(0,-0.02,1),Sz*0.95,(1000,700))
# original copy for comparison (cs = our in-game XML scale / original's XML scale; the original is shown at 1/cs)
def compare(mname,glbname,origtex,cs,suffix,caption):
    for m2,o2 in models.items(): o2.hide_render=(m2!=mname)
    bpy.context.view_layer.update(); mn,mx=evaluated_bbox([models[mname]]); Cc=(mn+mx)/2
    before=set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=G+glbname+'.glb')
    new=[o for o in bpy.data.objects if o not in before]
    oarm=[o for o in new if o.type=='ARMATURE'][0]; oact=oarm.animation_data.action
    om=[o for o in new if o.type=='MESH' and o.parent==oarm][0]
    for o in new:
        if o.type=='MESH' and o.parent is None: o.hide_render=True
    img_material(om,S+origtex,'origtex'+suffix)
    set_act(oarm,oact if pf is not None else None,(f0+(f1-f0)*pf) if pf is not None else 0)
    oarm.scale=(1/cs,)*3; bpy.context.view_layer.update()
    w=(mx.x-mn.x); gap=A.get('gap',0.25)
    omn,omx=evaluated_bbox([om]); w=max(w,omx.x-omn.x)
    ln=max(mx.y-mn.y,omx.y-omn.y); oarm.location=(0,ln*1.1,0)
    hh=max(mx.z,omx.z)
    view(P+'07_side_compare'+suffix+'.png',Vector((Cc.x,Cc.y+ln*0.55,hh*0.5)),(1,0,0),ln*2.4,(1400,600))
    oarm.location=(w*(1+gap),0,0)
    cx=Cc.x+w*(1+gap)/2
    view(P+'02_compare_game_angle'+suffix+'.png',Vector((cx,Cc.y,Cc.z)),GA,max((w*(2+gap))*1.08,(mx.y-mn.y)*1.05*1400/800),(1400,800))
    for o in new: o.hide_render=True
    if caption: CAP['07_side_compare'+suffix+'.png']=caption; CAP['02_compare_game_angle'+suffix+'.png']=caption
    return w
w=compare(mainm,A.get('compare_glb',f'{am}_{an}'),A['orig_tex'],A.get('cmp_scale',1.0),'',A.get('cmp_caption'))
for (m2,g2,t2,cs2,suf2,cap2) in A.get('extra_compares',[]): compare(m2,g2,t2,cs2,suf2,cap2)
for m2,o2 in models.items(): o2.hide_render=(m2!=mainm)
# animation strips (fixed framing over the whole clip)
nf=A.get('strip_frames',6); frames=[f0+(f1-f0)*i/nf for i in range(nf)]
os.makedirs(R+'/_frames',exist_ok=True)
SM=A.get('strip_models',[(mainm,maintex,'')])
if A.get('water'):
    bpy.data.objects['ground'].location.z=-95
    bpy.ops.mesh.primitive_plane_add(size=2000,location=(0,0,0)); wp=bpy.context.object; wp.name='water'
    wm=bpy.data.materials.new('water'); wm.use_nodes=True; wb=wm.node_tree.nodes['Principled BSDF']
    wb.inputs['Base Color'].default_value=(0.10,0.30,0.36,1); wb.inputs['Alpha'].default_value=0.35; wb.inputs['Roughness'].default_value=0.3
    try: wm.surface_render_method='BLENDED'
    except Exception: pass
    wp.data.materials.append(wm); wp.visible_shadow=False
for ent in SM:
    mname,tex,label=ent[:3]; sact=act; sf0,sf1=f0,f1
    if len(ent)>3:
        b4=set(bpy.data.objects); bpy.ops.import_scene.gltf(filepath=G+ent[3]+'.glb')
        nw=[o for o in bpy.data.objects if o not in b4]; ta=[o for o in nw if o.type=='ARMATURE'][0]
        sact=ta.animation_data.action; sact.use_fake_user=True; sf0,sf1=sact.frame_range
        for o in nw: bpy.data.objects.remove(o)
    frames=[sf0+(sf1-sf0)*i/nf for i in range(nf)]
    for o2 in models.values(): o2.hide_render=True
    ob2=models[mname]; ob2.hide_render=False; img_material(ob2,texpaths[tex],'strip_'+mname)
    set_act(arm,sact)
    bb=[]
    for fr in frames:
        sc.frame_set(int(fr)); bb.append(evaluated_bbox([ob2]))
    S2=max((b[1]-b[0]).length for b in bb)
    for k,fr in enumerate(frames):
        sc.frame_set(int(fr)); C2=(bb[k][0]+bb[k][1])/2
        view(R+f'/_frames/anim_{label}_{k}.png',C2,TQ,S2*1.0,(640,480)); FR=frames
json.dump(dict(anim=an,prefix=PF,pdir=PD,captions=CAP,strips=[[x[2],(x[3] if len(x)>3 else an)] for x in SM],frames=[int(f) for f in frames]),open(R+'/_frames/info.json','w'))
# variants lineup (game angle, rest pose / pose frame)
set_act(arm,act if pf is not None else None,(f0+(f1-f0)*pf) if pf is not None else 0)
VAR=A.get('variants')
if VAR:
    objs=[]
    for i,ve in enumerate(VAR):
        mname,tex,label=ve[:3]
        src=models[mname]; o=src.copy(); o.data=src.data.copy(); sc.collection.objects.link(o)
        o.parent=arm; o.hide_render=False
        if len(ve)>3: o.scale=(ve[3],)*3
        img_material(o,texpaths[tex],'var%d'%i); objs.append(o)
    for o in models.values(): o.hide_render=True
    step=w*(1+A.get('vgap',0.15)); 
    for i,o in enumerate(objs): o.location=(i*step,0,0)
    tot=(len(objs)-1)*step
    view(P+'04_variants_game_angle.png',Vector((Cc.x+tot/2,Cc.y,Cc.z)),GA,max((tot+w)*1.08,(mx.y-mn.y)*1.05*1600/700),(1600,700))
    json.dump([v[2] for v in VAR],open(R+'/_frames/variants.json','w'))
    if A.get('var_caption'): CAP['04_variants_game_angle.png']=A['var_caption']
    i2=json.load(open(R+'/_frames/info.json')); i2['captions']=CAP; json.dump(i2,open(R+'/_frames/info.json','w'))
print('DONE')
