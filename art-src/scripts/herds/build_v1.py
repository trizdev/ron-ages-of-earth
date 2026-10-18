import sys, os, json, struct, subprocess, math
sys.path.insert(0,'/workspace/prehistoric-herds/scripts')
import bpy, bmesh, numpy as np
from mathutils import Vector
from lib import *
from animals import ANIMALS
name=sys.argv[sys.argv.index('--')+1]
A=ANIMALS[name]; R='/workspace/prehistoric-herds/'+A['folder']; SRC='/workspace/prehistoric-herds/src'
for d in ('preview','export','tex','_frames'): os.makedirs(R+'/'+d,exist_ok=True)
arm,orig,act=load_source(f"{SRC}/glb/{A['src']}_walk.glb")
orig.hide_render=True; orig.name='_orig_'+orig.name
bm=bmesh.new(); ex=bmesh.new(); A['parts'](bm,ex)
main=to_obj(bm,'main'); extras=[]
if len(ex.verts): extras=[to_obj(ex,'extra')]
else: ex.free()
ob,nmain=make_skin(main,extras,A['voxel'],A['smooth'],A['target'])
ob.name='new_base'
cnt=skin_by_transfer(ob,orig,arm,A['region'],A['override'],A['legbones'])
print('STATS bonecounts',dict(cnt))
# materials / face regions
flatnames=list(A['flats'].keys())
skins=[skin_material('skin%d'%i,c) for i,c in enumerate(A['coats'])]
flats=[flat_material(k,*A['flats'][k]) for k in flatnames]
me=ob.data; me.materials.clear(); me.materials.append(skins[0])
for f in flats: me.materials.append(f)
idx={k:i+1 for i,k in enumerate(flatnames)}
for p in me.polygons:
    if min(p.vertices)>=nmain and 'tusk' in idx: p.material_index=idx['tusk']; continue
    k=A['faces'](p.center,p.normal); p.material_index=idx.get(k,0)
box_uv(ob)
ts=A['texsize']; bakes=[]
for i,sk in enumerate(skins):
    me.materials[0]=sk
    bakes.append(bake(ob,[sk]+flats,ts,hide=[orig]))
T=R+'/tex/'
if A['texmode']=='atlas':
    at=np.zeros((2*ts,2*ts,4)); quads=[(0,1),(1,1),(0,0),(1,0)]
    for q,(c,r) in enumerate(quads):
        at[r*ts:(r+1)*ts,c*ts:(c+1)*ts]=bakes[q if q<len(bakes) else 0]
    save_png(at,T+'atlas.png'); texfiles=[T+'atlas.png']*len(bakes)
    uvx=lambda u,v,coat: ((u+quads[coat][0])/2.0,(v+quads[coat][1])/2.0)
    outtex=[(T+'atlas.png',A['texname'])]
elif A['texmode']=='separate':
    texfiles=[]; outtex=[]
    for i,b in enumerate(bakes):
        p=T+'coat%d.png'%i; save_png(b,p); texfiles.append(p); outtex.append((p,A['texnames'][i]))
    uvx=lambda u,v,coat:(u,v)
else:
    save_png(bakes[0],T+'coat0.png'); texfiles=[T+'coat0.png']; outtex=[(T+'coat0.png',A['texname'])]
    uvx=lambda u,v,coat:(u,v)
json.dump(outtex,open(T+'outtex.json','w'))
# variants
VO=[]
for vname,coat,tw in A['variants']:
    o=ob.copy(); o.data=ob.data.copy(); o.name=vname; o.data.name=vname
    bpy.context.scene.collection.objects.link(o)
    uvl=o.data.uv_layers.active
    for l in uvl.data: l.uv=uvx(l.uv[0],l.uv[1],coat)
    if tw:
        f=A['tweaks'][tw]
        for v in o.data.vertices: v.co=f(v.co.copy())
    final_material(o,vname+'_mat',texfiles[coat if A['texmode']!='shared' else 0])
    o.parent=arm; VO.append(o)
bpy.data.objects.remove(ob)
# export + convert + verify
DOT=['/home/box/opt/dotnet/dotnet','/tmp/rfc/ron-file-converter.dll']
def gl(f):
    d=open(f,'rb').read(); l=struct.unpack('<I',d[12:16])[0]; return json.loads(d[20:20+l])
srcj=gl(f"{SRC}/glb/{A['src']}_walk.glb")
srcnodes=[(n.get('name'),n.get('translation'),n.get('rotation')) for n in srcj['nodes'] if 'mesh' not in n]
report=[]
for o in VO:
    for x in VO: x.hide_set(False)
    for x in bpy.context.selected_objects: x.select_set(False)
    arm.select_set(True); o.select_set(True); bpy.context.view_layer.objects.active=arm
    g=f"{R}/export/{o.name}.glb"
    bpy.ops.export_scene.gltf(filepath=g,use_selection=True,export_animations=False,export_format='GLB')
    fix_child_order(g,[x[0] for x in srcnodes])
    b3=f"{R}/export/{o.name}.BH3"
    r=subprocess.run(DOT+['gltf',g,'-mo',b3],capture_output=True,text=True); ok1='succeeded' in r.stdout
    rr=f"{R}/export/_reread_{o.name}.glb"
    r2=subprocess.run(DOT+['bh3',b3,'-o',rr],capture_output=True,text=True); ok2='succeeded' in r2.stdout
    j=gl(rr); nn=[(n.get('name'),n.get('translation'),n.get('rotation')) for n in j['nodes'] if 'mesh' not in n]
    same_names=[a[0] for a in nn]==[a[0] for a in srcnodes]
    mx=0
    for a,b in zip(nn,srcnodes):
        for i in (1,2):
            x=a[i] or ([0,0,0] if i==1 else [0,0,0,1]); y=b[i] or ([0,0,0] if i==1 else [0,0,0,1])
            dd=max(abs(p-q) for p,q in zip(x,y))
            if i==2: dd=min(dd,max(abs(p+q) for p,q in zip(x,y)))   # q and -q are the same rotation
            mx=max(mx,dd)
    pm=j['meshes'][0]['primitives'][0]
    nv=j['accessors'][pm['attributes']['POSITION']]['count']; nt=j['accessors'][pm['indices']]['count']//3
    multi=sum(1 for v in o.data.vertices if len(v.groups)!=1)
    report.append(dict(variant=o.name,convert=ok1,reread=ok2,bones_same=same_names,rest_maxdiff=mx,bh3_verts=nv,bh3_tris=nt,blender_tris=len(o.data.polygons),multi_weight=multi,bh3_bytes=os.path.getsize(b3)))
    if not ok1: print('CONVERR',r.stdout[-500:],r.stderr[-500:])
po=orig.data; report.append(dict(original=orig.name,verts=len(po.vertices),tris=len(po.polygons)))
json.dump(report,open(R+'/export/verify.json','w'),indent=1)
print('REPORT',json.dumps(report))
bpy.ops.wm.save_as_mainfile(filepath=f"{R}/{A['folder']}_work.blend")
# ---------------- renders
cam=setup_scene()
def bbox(objs):
    pts=[o.matrix_world@v.co for o in objs for v in o.data.vertices]
    mn=Vector([min(p[i] for p in pts) for i in range(3)]); mx_=Vector([max(p[i] for p in pts) for i in range(3)]); return mn,mx_
mn,mxv=bbox([VO[0]]); S=max(mxv.y-mn.y, mxv.z)*1.0; C=(mn+mxv)/2
for o in VO[1:]: o.hide_render=True
P=R+'/preview/'
shot(cam,P+'01_three_quarter.png',(C.x+S*1.9,C.y-S*2.7,S*1.6),(C.x,C.y,C.z*0.8),lens=60)
# comparison with original at game camera angle
before=set(bpy.data.objects)
bpy.ops.import_scene.gltf(filepath=f"{SRC}/glb/{A['src']}_walk.glb")
new=[o for o in bpy.data.objects if o not in before]
oarm=[o for o in new if o.type=='ARMATURE'][0]
if oarm.animation_data: oarm.animation_data.action=None
for pb in oarm.pose.bones: pb.matrix_basis.identity()
om=[o for o in new if o.type=='MESH' and o.parent==oarm][0]
for o in new:
    if o.type=='MESH' and o.parent is None: o.hide_render=True
srctex={'Wildhorse_1':'WildHorses.tga','pig':'pig.tga','sheep2':'sheep.tga'}[A['src']]
tex_material(om,f"{SRC}/{srctex}")
w=(mxv.x-mn.x)
oarm.location=(w+S*0.25,0,0)
cx=(w+S*0.25)/2
shot(cam,P+'02_compare_game_angle.png',(cx-S*0.5,C.y-S*2.5,S*2.9),(cx,C.y,C.z*0.5),lens=45,res=(1200,800))
shot(cam,P+'03_compare_side.png',(S*4,C.y,C.z),(cx,C.y,C.z),ortho=S*1.25 if False else None,lens=50,res=(1200,700)) if False else None
# side comparison: ortho, original behind (to the right)
oarm.location=(0,(mxv.y-mn.y)*1.15,0)
cam.data.type='ORTHO'
shot(cam,P+'03_compare_side.png',(S*4,C.y+(mxv.y-mn.y)*0.575,C.z),(0,C.y+(mxv.y-mn.y)*0.575,C.z),ortho=(mxv.y-mn.y)*2.6,res=(1400,700))
for o in new: o.hide_render=True
# variant lineup
if len(VO)>1:
    for i,o in enumerate(VO):
        o.hide_render=False; o.location=(i*(w+S*0.15),0,0)
    tot=(len(VO)-1)*(w+S*0.15)
    shot(cam,P+'04_variants_game_angle.png',(tot/2-S*0.3,C.y-S*1.9-tot*0.5,S*2.1+tot*0.5),(tot/2,C.y,C.z*0.6),lens=50,res=(1400,800))
    for i,o in enumerate(VO):
        o.location=(0,0,0); o.hide_render=(i!=0)
# walk test
set_action(arm,act)
fr=act.frame_range; frames=[int(round(fr[0]+(fr[1]-fr[0])*k/4.0)) for k in range(4)]
sc=bpy.context.scene
for f in frames:
    sc.frame_set(f); shot(cam,R+'/_frames/walk_%03d.png'%f,(S*4,C.y,C.z),(0,C.y,C.z),ortho=S*1.9,res=(800,560))
json.dump(frames,open(R+'/_frames/frames.json','w'))
sc.frame_set(frames[1]); shot(cam,P+'06_walk_three_quarter.png',(C.x+S*1.9,C.y-S*2.7,S*1.6),(C.x,C.y,C.z*0.8),lens=60)
set_action(arm,None)
print('DONE')
