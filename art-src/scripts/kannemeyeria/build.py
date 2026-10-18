import bpy, bmesh, math, sys
from mathutils import Vector
W='/workspace/kannemeyeria'
TEX=int(sys.argv[sys.argv.index('--')+1]) if '--' in sys.argv else 128
TARGET=int(sys.argv[sys.argv.index('--')+2]) if '--' in sys.argv and len(sys.argv)>sys.argv.index('--')+2 else 440
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=W+'/src/bison_walk.glb')
arm=bpy.data.objects['Armature']; bison=bpy.data.objects['bison']
if arm.animation_data: arm.animation_data.action=None
for pb in arm.pose.bones: pb.matrix_basis.identity()
bonenames=[b.name for b in arm.data.bones]
J={b.name:(arm.matrix_world@b.head_local).copy() for b in arm.data.bones}

def frame(d):
    d=d.normalized(); a=Vector((1,0,0)) if abs(d.x)<0.9 else Vector((0,1,0))
    u=d.cross(a).normalized(); return u,d.cross(u).normalized()
def ellipsoid(bm,c,r,segs=24,rings=16,deform=None):
    c=Vector(c); R=[]
    for i in range(1,rings):
        th=math.pi*i/rings; ring=[]
        for j in range(segs):
            ph=2*math.pi*j/segs
            p=Vector((math.sin(th)*math.cos(ph)*r[0], math.sin(th)*math.sin(ph)*r[1], math.cos(th)*r[2]))
            if deform: p=deform(p)
            ring.append(bm.verts.new(c+p))
        R.append(ring)
    pt=Vector((0,0,r[2])); pb=Vector((0,0,-r[2]))
    if deform: pt=deform(pt); pb=deform(pb)
    vt=bm.verts.new(c+pt); vb=bm.verts.new(c+pb)
    for j in range(segs):
        k=(j+1)%segs
        bm.faces.new([vt,R[0][k],R[0][j]]); bm.faces.new([vb,R[-1][j],R[-1][k]])
        for i in range(len(R)-1): bm.faces.new([R[i][j],R[i][k],R[i+1][k],R[i+1][j]])
def tube(bm,pts,radii,sides=16,sub=3):
    # smooth-ish tube with spheres at joints (caps)
    P=[Vector(p) for p in pts]; rings=[]
    def rr(x): return x if isinstance(x,tuple) else (x,x)
    for n in range(len(P)-1):
        for s in range(sub if n<len(P)-2 else sub+1):
            t=s/sub; p=P[n].lerp(P[n+1],t)
            a,b=rr(radii[n]),rr(radii[n+1]); r=(a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t)
            d=P[min(n+1,len(P)-1)]-P[n]
            u,w=frame(d)
            # keep foot ellipse long axis along Y
            ring=[bm.verts.new(p+u*math.cos(2*math.pi*j/sides)*r[0]+w*math.sin(2*math.pi*j/sides)*r[1]) for j in range(sides)]
            rings.append(ring)
    for i in range(len(rings)-1):
        for j in range(sides):
            k=(j+1)%sides; bm.faces.new([rings[i][j],rings[i][k],rings[i+1][k],rings[i+1][j]])
    bm.faces.new(rings[-1]); bm.faces.new(list(reversed(rings[0])))
    for p,r in zip(P,radii):
        r=rr(r); ellipsoid(bm,p,(max(r)*0.98,max(r)*0.98,max(r)*0.98),12,8)
def cone(bm,base,tip,r,tipr=0.0,sides=12):
    base=Vector(base); tip=Vector(tip); u,w=frame(tip-base)
    rx,ry=(r,r) if not isinstance(r,tuple) else r
    ring=[bm.verts.new(base+u*math.cos(2*math.pi*j/sides)*rx+w*math.sin(2*math.pi*j/sides)*ry) for j in range(sides)]
    if tipr<=0:
        vt=bm.verts.new(tip)
        for j in range(sides): bm.faces.new([ring[j],ring[(j+1)%sides],vt])
    else:
        r2=[bm.verts.new(tip+u*math.cos(2*math.pi*j/sides)*tipr+w*math.sin(2*math.pi*j/sides)*tipr) for j in range(sides)]
        for j in range(sides): k=(j+1)%sides; bm.faces.new([ring[j],ring[k],r2[k],r2[j]])
        bm.faces.new(r2[::-1] if False else r2)
    bm.faces.new(list(reversed(ring)))
def to_obj(bm,name):
    me=bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    o=bpy.data.objects.new(name,me); bpy.context.scene.collection.objects.link(o); return o

bm=bmesh.new()
# body: deep low barrel, wide, a bit higher at shoulders, tapering to the hips
def body_def(p):
    t=(p.y+17.5)/35.0
    sx=1.0-0.20*max(0,t-0.5)/0.5
    q=Vector((p.x*sx,p.y,p.z))
    if q.z>0: q.z*=1.0-0.15*t           # back slopes down a little toward the tail
    else: q.z*=0.95
    return q
ellipsoid(bm,(0,1.5,17.6),(10.6,17.5,10.4),deform=body_def)
# shoulder mass
ellipsoid(bm,(0,-9.5,19.5),(10.0,8.0,9.2))
# neck: short and thick
tube(bm,[(0,-11,21),(0,-17,22),(0,-21.5,22.5)],[7.2,6.2,5.6])
# skull: broad at the back (big jaw muscles), eyes high
def head_def(p):
    t=(-p.y)/6.8
    q=Vector((p.x*(1.0-0.30*max(0,t)),p.y,p.z))
    return q
ellipsoid(bm,(0,-25.5,22.5),(6.2,6.8,6.0),deform=head_def)
# deep, short snout
ellipsoid(bm,(0,-31.2,19.6),(3.7,3.8,4.6))
# lower jaw
ellipsoid(bm,(0,-28.8,16.6),(4.0,4.6,2.4))
# brow ridges over the eyes
pass  # (brow ridges removed: read as bear ears)
# caniniform bulges where the tusks come out
for s in (1,-1): ellipsoid(bm,(s*3.0,-30.6,18.0),(1.7,1.8,2.0),12,8)
# horny beak: blunt, hooked down like a turtle
cone(bm,(0,-32.8,19.2),(0,-35.0,14.6),(2.8,3.3),tipr=1.5)
# legs: stout, elbows/knees turned out (sprawling-ish)
for s in (1,-1):
    tube(bm,[(s*8.0,-10.2,15.0),(s*10.2,-8.9,8.0),(s*8.8,-9.3,3.4),(s*8.6,-11.0,0.9)],[4.6,3.6,2.9,(3.0,3.4)])
    ellipsoid(bm,(s*8.8,-11.6,0.9),(3.0,3.8,1.4),12,8)          # broad front foot
    tube(bm,[(s*7.5,10.5,15.5),(s*9.0,13.1,11.2),(s*7.8,15.6,6.4),(s*7.2,14.5,0.9)],[5.6,4.4,3.2,(3.2,3.6)])
    ellipsoid(bm,(s*7.3,13.4,0.9),(3.2,4.2,1.4),12,8)           # broad hind foot
# short thick tail
cone(bm,(0,16.0,19.5),(0,21.8,15.6),(3.0,2.7),tipr=0.9)
main=to_obj(bm,'kmain')
bm=bmesh.new()
for s in (1,-1): cone(bm,(s*3.1,-30.9,17.6),(s*3.5,-32.0,12.0),0.95,sides=5)
tusk=to_obj(bm,'ktusk')

def apply(o,m):
    bpy.context.view_layer.objects.active=o
    for x in bpy.context.selected_objects: x.select_set(False)
    o.select_set(True); bpy.ops.object.modifier_apply(modifier=m.name)
r=main.modifiers.new('r','REMESH'); r.mode='VOXEL'; r.voxel_size=0.55; apply(main,r)
sm=main.modifiers.new('s','SMOOTH'); sm.factor=0.6; sm.iterations=4; apply(main,sm)
# flatten soles on the ground
for v in main.data.vertices:
    if v.co.z<0.0: v.co.z=0.0
n0=len(main.data.polygons)
d=main.modifiers.new('d','DECIMATE'); d.decimate_type='COLLAPSE'; d.ratio=(TARGET-10)/(2.0*n0) if False else (TARGET-10)/float(sum(len(p.vertices)-2 for p in main.data.polygons)); d.use_collapse_triangulate=True; apply(main,d)
t=main.modifiers.new('t','TRIANGULATE'); apply(main,t)
# join tusks
NMAIN=len(main.data.vertices)
for x in bpy.context.selected_objects: x.select_set(False)
tusk.select_set(True); main.select_set(True); bpy.context.view_layer.objects.active=main
bpy.ops.object.join()
ob=main; ob.name='kannemeyeria'; me=ob.data; me.name='kannemeyeria'
bm=bmesh.new(); bm.from_mesh(me); bmesh.ops.triangulate(bm,faces=bm.faces[:]); bmesh.ops.remove_doubles(bm,verts=bm.verts[:],dist=0.0001); bm.to_mesh(me); bm.free()

# ---- rigid skinning: every vertex -> exactly one bison bone
def segdist(p,a,b):
    ab=b-a; t=max(0,min(1,(p-a).dot(ab)/ab.length_squared)); return (p-(a+ab*t)).length
legs={}
for side,s in (('left',1),('right',-1)):
    sh='sholderleft' if s>0 else 'shoulderright'
    legs[('f',s)]=[(sh,Vector((s*8.0,-10.2,15.0)),Vector((s*10.2,-8.9,8.0))),('elbow'+side,Vector((s*10.2,-8.9,8.0)),Vector((s*8.8,-9.3,3.4))),('wrist'+side,Vector((s*8.8,-9.3,3.4)),Vector((s*8.8,-11.6,0.0)))]
    legs[('h',s)]=[('hip'+side,Vector((s*7.5,10.5,15.5)),Vector((s*9.0,13.1,11.2))),('knee'+side,Vector((s*9.0,13.1,11.2)),Vector((s*7.8,15.6,6.4))),('heel'+side,Vector((s*7.8,15.6,6.4)),Vector((s*7.3,13.4,0.0)))]
def bone_for(p):
    if p.y < -21.0: return 'head con'
    if p.y > 16.0 and p.z > 12.0 and abs(p.x)<4.5: return 'tail1' if p.y<20.5 else 'tail2'
    fr = p.y < 2.0
    limb = p.z < (9.5 if fr else 9.0) or (abs(p.x)>9.6 and p.z<13.5)
    if limb:
        ch=legs[('f' if fr else 'h', 1 if p.x>=0 else -1)]
        return min(ch,key=lambda c:segdist(p,c[1],c[2]))[0]
    if p.y < -13.5 and p.z > 13.0: return 'neck'
    return 'dummy' if p.y<5.0 else 'ass con'
for n in bonenames: ob.vertex_groups.new(name=n)
from collections import Counter
cnt=Counter()
for v in me.vertices:
    bn=bone_for(v.co); ob.vertex_groups[bn].add([v.index],1.0,'REPLACE'); cnt[bn]+=1
print('STATS bonecounts',dict(cnt))
ob.parent=arm
mod=ob.modifiers.new('Armature','ARMATURE'); mod.object=arm
for p in me.polygons: p.use_smooth=True
# material regions: 0 skin, 1 beak, 2 tusk
me.materials.clear()
# --- materials for baking
def mat(name,build):
    m=bpy.data.materials.new(name); m.use_nodes=True; nt=m.node_tree
    for n in list(nt.nodes): nt.nodes.remove(n)
    out=nt.nodes.new('ShaderNodeOutputMaterial'); bs=nt.nodes.new('ShaderNodeBsdfDiffuse')
    nt.links.new(bs.outputs[0],out.inputs[0])
    build(nt,bs.inputs['Color']); return m
def lin(c):
    f=lambda x: x/12.92 if x<=0.04045 else ((x+0.055)/1.055)**2.4
    return tuple(f(x) for x in c[:3])+(1,)
def N(nt,t,**kw):
    n=nt.nodes.new(t)
    for k,v in kw.items():
        if k.startswith('i_'): n.inputs[k[2:].replace('_',' ')].default_value=v
        else: setattr(n,k,v)
    return n
def L(nt,a,b): nt.links.new(a,b)
def skin(nt,col_in):
    tc=N(nt,'ShaderNodeNewGeometry'); pos=tc.outputs['Position']
    sep=N(nt,'ShaderNodeSeparateXYZ'); L(nt,pos,sep.inputs[0])
    # mottled base: olive-brown vs grey
    n1=N(nt,'ShaderNodeTexNoise',i_Scale=0.16,i_Detail=5.0,i_Roughness=0.6); L(nt,pos,n1.inputs['Vector'])
    r1=N(nt,'ShaderNodeValToRGB'); L(nt,n1.outputs['Fac'],r1.inputs[0])
    e=r1.color_ramp.elements; e[0].position=0.36; e[0].color=lin((0.37,0.33,0.21)); e[1].position=0.70; e[1].color=lin((0.42,0.41,0.35))
    # belly lighter / back darker (countershading) by height
    sn=N(nt,'ShaderNodeSeparateXYZ'); L(nt,tc.outputs['Normal'],sn.inputs[0])
    zr=N(nt,'ShaderNodeMapRange',i_From_Min=0.2,i_From_Max=1.0,i_To_Min=0.0,i_To_Max=0.75); L(nt,sn.outputs['Z'],zr.inputs['Value'])
    belly=N(nt,'ShaderNodeMix',data_type='RGBA',blend_type='MIX'); 
    belly.inputs['B'].default_value=lin((0.22,0.20,0.13))
    L(nt,r1.outputs['Color'],belly.inputs['A']); L(nt,zr.outputs['Result'],belly.inputs['Factor'])
    lb=N(nt,'ShaderNodeMix',data_type='RGBA',blend_type='MIX')
    lb.inputs['B'].default_value=lin((0.56,0.50,0.38)); L(nt,belly.outputs['Result'],lb.inputs['A'])
    zr2=N(nt,'ShaderNodeMapRange',i_From_Min=-0.3,i_From_Max=-0.95); L(nt,sn.outputs['Z'],zr2.inputs['Value'])
    hd=N(nt,'ShaderNodeMath',operation='MULTIPLY'); hd.inputs[1].default_value=0.8; L(nt,zr2.outputs['Result'],hd.inputs[0])
    L(nt,hd.outputs[0],lb.inputs['Factor'])
    # wrinkles: voronoi cell edges (pebbly reptilian skin) + stretched wave folds
    vo=N(nt,'ShaderNodeTexVoronoi',feature='DISTANCE_TO_EDGE',i_Scale=0.9); L(nt,pos,vo.inputs['Vector'])
    vr=N(nt,'ShaderNodeMapRange',i_From_Min=0.0,i_From_Max=0.10,i_To_Min=0.55,i_To_Max=1.0); L(nt,vo.outputs['Distance'],vr.inputs['Value'])
    wv=N(nt,'ShaderNodeTexWave',wave_type='BANDS',bands_direction='Z',i_Scale=0.35,i_Distortion=6.0,i_Detail=2.0); L(nt,pos,wv.inputs['Vector'])
    wr=N(nt,'ShaderNodeMapRange',i_From_Min=0.0,i_From_Max=0.5,i_To_Min=0.68,i_To_Max=1.0); L(nt,wv.outputs['Fac'],wr.inputs['Value'])
    m1=N(nt,'ShaderNodeMath',operation='MULTIPLY'); L(nt,vr.outputs['Result'],m1.inputs[0]); L(nt,wr.outputs['Result'],m1.inputs[1])
    mm=N(nt,'ShaderNodeMix',data_type='RGBA',blend_type='MULTIPLY',i_Factor=1.0)
    L(nt,lb.outputs['Result'],mm.inputs['A'])
    cm=N(nt,'ShaderNodeCombineColor'); [L(nt,m1.outputs[0],cm.inputs[i]) for i in range(3)]
    L(nt,cm.outputs[0],mm.inputs['B'])
    # eyes: dark spot on both sides of the head (abs x)
    ab=N(nt,'ShaderNodeMath',operation='ABSOLUTE'); L(nt,sep.outputs['X'],ab.inputs[0])
    ce=N(nt,'ShaderNodeCombineXYZ'); L(nt,ab.outputs[0],ce.inputs['X']); L(nt,sep.outputs['Y'],ce.inputs['Y']); L(nt,sep.outputs['Z'],ce.inputs['Z'])
    ds=N(nt,'ShaderNodeVectorMath',operation='DISTANCE'); L(nt,ce.outputs[0],ds.inputs[0]); ds.inputs[1].default_value=(4.9,-27.6,24.6)
    er=N(nt,'ShaderNodeMapRange',i_From_Min=1.2,i_From_Max=1.7,i_To_Min=1.0,i_To_Max=0.0); L(nt,ds.outputs['Value'],er.inputs['Value'])
    em=N(nt,'ShaderNodeMix',data_type='RGBA',blend_type='MIX'); em.inputs['B'].default_value=(0.02,0.015,0.01,1)
    L(nt,mm.outputs['Result'],em.inputs['A']); L(nt,er.outputs['Result'],em.inputs['Factor'])
    L(nt,em.outputs['Result'],col_in)
def flat(c,noise=0.0):
    def b(nt,col_in):
        if noise==0: col_in.default_value=c; return
        tc=N(nt,'ShaderNodeNewGeometry'); n=N(nt,'ShaderNodeTexNoise',i_Scale=0.8,i_Detail=3.0); L(nt,tc.outputs['Position'],n.inputs['Vector'])
        r=N(nt,'ShaderNodeValToRGB'); L(nt,n.outputs['Fac'],r.inputs[0])
        e=r.color_ramp.elements; e[0].color=tuple(x*(1-noise) for x in c[:3])+(1,); e[1].color=c
        L(nt,r.outputs['Color'],col_in)
    return b
for nm,b in (('skin',skin),('beak',flat(lin((0.20,0.17,0.13)),0.35)),('tusk',flat(lin((0.82,0.76,0.62)),0.2))):
    me.materials.append(mat('k_'+nm,b))
for p in me.polygons:
    c=p.center
    if min(p.vertices)>=NMAIN: p.material_index=2
    elif c.y< -32.6 and c.z<19.6: p.material_index=1
    else: p.material_index=0

bpy.context.view_layer.objects.active=ob
for o in bpy.context.selected_objects: o.select_set(False)
ob.select_set(True)
bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.uv.smart_project(angle_limit=math.radians(60),island_margin=0.02,scale_to_bounds=True)
bpy.ops.uv.pack_islands(margin=0.012,rotate=True)
bpy.ops.object.mode_set(mode='OBJECT')
# --- bake diffuse color + AO
sc=bpy.context.scene; sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=64
def newimg(n): 
    im=bpy.data.images.new(n,TEX,TEX,alpha=False); return im
dif=newimg('k_diffuse'); ao=newimg('k_ao')
def set_target(im):
    for m in me.materials:
        nt=m.node_tree
        t=nt.nodes.get('BAKE') or nt.nodes.new('ShaderNodeTexImage'); t.name='BAKE'; t.image=im
        nt.nodes.active=t
set_target(dif)
sc.render.bake.use_pass_direct=False; sc.render.bake.use_pass_indirect=False; sc.render.bake.margin=4
bpy.ops.object.bake(type='DIFFUSE',pass_filter={'COLOR'})
set_target(ao)
# hide bison from AO
bison.hide_render=True; bpy.data.objects['Icosphere'].hide_render=True
bpy.ops.object.bake(type='AO')
import numpy as np
d=np.array(dif.pixels[:]).reshape(TEX,TEX,4); a=np.array(ao.pixels[:]).reshape(TEX,TEX,4)
out=d.copy(); out[...,:3]=d[...,:3]*(0.5+0.5*a[...,:1])
# linear -> sRGB for the final texture
def srgb(x): return np.where(x<=0.0031308,12.92*x,1.055*np.power(np.clip(x,0,1),1/2.4)-0.055)
out[...,3]=1.0
fin=bpy.data.images.new('Kannemeyeria',TEX,TEX,alpha=True)
fin.colorspace_settings.name='sRGB'
fin.pixels[:]=out.ravel()
fin.filepath_raw=W+'/kannemeyeria_tex.png'; fin.file_format='PNG'; fin.save()
# --- final single material using the baked texture
for m in list(me.materials): pass
me.materials.clear()
fm=bpy.data.materials.new('kannemeyeria'); fm.use_nodes=True; nt=fm.node_tree
bsdf=nt.nodes['Principled BSDF']; bsdf.inputs['Roughness'].default_value=0.85
ti=nt.nodes.new('ShaderNodeTexImage'); ti.image=fin; nt.links.new(ti.outputs['Color'],bsdf.inputs['Base Color'])
me.materials.append(fm)
for p in me.polygons: p.material_index=0
# bison gets its real texture for comparison
bt=bpy.data.images.load(W+'/src/Bison.tga'); bm_=bison.material_slots[0].material; bm_.use_nodes=True; nt=bm_.node_tree
bsdf=nt.nodes.get('Principled BSDF'); t2=nt.nodes.new('ShaderNodeTexImage'); t2.image=bt; nt.links.new(t2.outputs['Color'],bsdf.inputs['Base Color'])
bsdf.inputs['Roughness'].default_value=0.85; bsdf.inputs['Metallic'].default_value=0.0
bison.hide_render=False
bt.pack(); fin.pack()
print('STATS bison tris',len(bison.data.polygons),'verts',len(bison.data.vertices))
print('STATS kanne tris',len(me.polygons),'verts',len(me.vertices),'multi',sum(1 for v in me.vertices if len(v.groups)!=1))
print('STATS bones',[b.name for b in arm.data.bones]==bonenames, len(bonenames))
bpy.ops.wm.save_as_mainfile(filepath=W+'/kannemeyeria_work.blend')
