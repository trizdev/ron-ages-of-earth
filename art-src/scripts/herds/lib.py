import bpy, bmesh, math
from mathutils import Vector, Matrix, kdtree
from collections import Counter
BL='/home/box/opt/blender-5.2.2-linux-x64/blender'
def lin(c):
    f=lambda x: x/12.92 if x<=0.04045 else ((x+0.055)/1.055)**2.4
    return tuple(f(x) for x in c[:3])+(1,)
def frame(d):
    d=d.normalized(); a=Vector((1,0,0)) if abs(d.x)<0.9 else Vector((0,1,0))
    u=d.cross(a).normalized(); return u,d.cross(u).normalized()
def ellipsoid(bm,c,r,segs=20,rings=12,deform=None,rot=None):
    c=Vector(c); R=[]
    def P(p):
        if deform: p=deform(p)
        if rot: p=rot@p
        return c+p
    for i in range(1,rings):
        th=math.pi*i/rings
        R.append([bm.verts.new(P(Vector((math.sin(th)*math.cos(2*math.pi*j/segs)*r[0], math.sin(th)*math.sin(2*math.pi*j/segs)*r[1], math.cos(th)*r[2])))) for j in range(segs)])
    vt=bm.verts.new(P(Vector((0,0,r[2])))); vb=bm.verts.new(P(Vector((0,0,-r[2]))))
    for j in range(segs):
        k=(j+1)%segs
        bm.faces.new([vt,R[0][k],R[0][j]]); bm.faces.new([vb,R[-1][j],R[-1][k]])
        for i in range(len(R)-1): bm.faces.new([R[i][j],R[i][k],R[i+1][k],R[i+1][j]])
def tube(bm,pts,radii,sides=14,sub=3,joints=True):
    P=[Vector(p) for p in pts]; rings=[]
    rr=lambda x: x if isinstance(x,tuple) else (x,x)
    for n in range(len(P)-1):
        for s in range(sub if n<len(P)-2 else sub+1):
            t=s/sub; p=P[n].lerp(P[n+1],t)
            a,b=rr(radii[n]),rr(radii[n+1]); r=(a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t)
            u,w=frame(P[n+1]-P[n])
            rings.append([bm.verts.new(p+u*math.cos(2*math.pi*j/sides)*r[0]+w*math.sin(2*math.pi*j/sides)*r[1]) for j in range(sides)])
    for i in range(len(rings)-1):
        for j in range(sides):
            k=(j+1)%sides; bm.faces.new([rings[i][j],rings[i][k],rings[i+1][k],rings[i+1][j]])
    bm.faces.new(rings[-1]); bm.faces.new(list(reversed(rings[0])))
    if joints:
        for p,r in zip(P,radii):
            m=max(rr(r))*0.97; ellipsoid(bm,p,(m,m,m),10,6)
def cone(bm,base,tip,r,tipr=0.0,sides=10):
    base=Vector(base); tip=Vector(tip); u,w=frame(tip-base)
    rx,ry=(r,r) if not isinstance(r,tuple) else r
    ring=[bm.verts.new(base+u*math.cos(2*math.pi*j/sides)*rx+w*math.sin(2*math.pi*j/sides)*ry) for j in range(sides)]
    if tipr<=0:
        vt=bm.verts.new(tip)
        for j in range(sides): bm.faces.new([ring[j],ring[(j+1)%sides],vt])
    else:
        r2=[bm.verts.new(tip+u*math.cos(2*math.pi*j/sides)*tipr+w*math.sin(2*math.pi*j/sides)*tipr) for j in range(sides)]
        for j in range(sides): k=(j+1)%sides; bm.faces.new([ring[j],ring[k],r2[k],r2[j]])
        bm.faces.new(r2)
    bm.faces.new(list(reversed(ring)))
def to_obj(bm,name):
    me=bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    o=bpy.data.objects.new(name,me); bpy.context.scene.collection.objects.link(o); return o
def select_only(o):
    for x in bpy.context.selected_objects: x.select_set(False)
    o.select_set(True); bpy.context.view_layer.objects.active=o
def apply(o,m): select_only(o); bpy.ops.object.modifier_apply(modifier=m.name)

def load_source(glb):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    arm=[o for o in bpy.data.objects if o.type=='ARMATURE'][0]
    act=arm.animation_data.action if arm.animation_data else None
    if arm.animation_data: arm.animation_data.action=None
    for pb in arm.pose.bones: pb.matrix_basis.identity()
    orig=[o for o in bpy.data.objects if o.type=='MESH' and o.parent==arm][0]
    for o in bpy.data.objects:
        if o.type=='MESH' and o.parent is None: o.hide_render=True; o.hide_viewport=True
    return arm,orig,act

def make_skin(main,extras,voxel,smooth_it,target,ground=0.0,protect=None,pfactor=3.0):
    r=main.modifiers.new('r','REMESH'); r.mode='VOXEL'; r.voxel_size=voxel; apply(main,r)
    sm=main.modifiers.new('s','SMOOTH'); sm.factor=0.6; sm.iterations=smooth_it; apply(main,sm)
    for v in main.data.vertices:
        if v.co.z<ground: v.co.z=ground
    ntri=sum(len(p.vertices)-2 for p in main.data.polygons)
    ex=sum(sum(len(p.vertices)-2 for p in e.data.polygons) for e in extras)
    if not protect:
        d=main.modifiers.new('d','DECIMATE'); d.decimate_type='COLLAPSE'; d.ratio=(target-ex)/float(ntri); d.use_collapse_triangulate=True
        apply(main,d)
    else:
        # weighted decimation (lower weight = keeps more detail); bisect the ratio to hit the triangle target
        g=main.vertex_groups.new(name='decim')
        for v in main.data.vertices: g.add([v.index],protect(v.co),'REPLACE')
        base=main.data.copy(); lo,hi=0.0005,(target-ex)/float(ntri)*4
        best=None
        for it in range(14):
            mid=(lo+hi)/2; main.data=base.copy()
            d=main.modifiers.new('d','DECIMATE'); d.decimate_type='COLLAPSE'; d.ratio=mid; d.use_collapse_triangulate=True
            d.vertex_group='decim'; d.vertex_group_factor=pfactor; apply(main,d)
            n=sum(len(p.vertices)-2 for p in main.data.polygons)
            if n>target-ex: hi=mid
            else: lo=mid; best=mid
        main.data=base.copy()
        d=main.modifiers.new('d','DECIMATE'); d.decimate_type='COLLAPSE'; d.ratio=best or lo; d.use_collapse_triangulate=True
        d.vertex_group='decim'; d.vertex_group_factor=pfactor; apply(main,d)
        print('WDECIM ratio',best,'tris',sum(len(p.vertices)-2 for p in main.data.polygons))
        main.vertex_groups.remove(main.vertex_groups['decim'])
    t=main.modifiers.new('t','TRIANGULATE'); apply(main,t)
    nmain=len(main.data.vertices)
    if extras:
        for x in bpy.context.selected_objects: x.select_set(False)
        for e in extras: e.select_set(True)
        main.select_set(True); bpy.context.view_layer.objects.active=main; bpy.ops.object.join()
    me=main.data
    bm=bmesh.new(); bm.from_mesh(me); bmesh.ops.triangulate(bm,faces=bm.faces[:]); bm.to_mesh(me); bm.free()
    for p in me.polygons: p.use_smooth=True
    return main,nmain

def skin_by_transfer(ob,orig,arm,region=None,override=None,legbones=()):
    """rigid skinning: each vertex takes the bone of the nearest original-model vertex (same side, same region class)."""
    bonenames=[b.name for b in arm.data.bones]
    ov=[]
    for v in orig.data.vertices:
        if not v.groups: continue
        g=max(v.groups,key=lambda g:g.weight); ov.append(((orig.matrix_world@v.co).copy(),orig.vertex_groups[g.group].name))
    def build(filt):
        pts=[o for o in ov if filt(o)]
        kd=kdtree.KDTree(len(pts))
        for i,(p,b) in enumerate(pts): kd.insert(p,i)
        kd.balance(); return kd,pts
    trees={}
    for side in (-1,0,1):
        for cls in ('leg','body'):
            def f(o,side=side,cls=cls):
                isleg=o[1] in legbones
                if cls=='leg' and not isleg: return False
                if cls=='body' and isleg: return False
                if side==0: return True
                return o[0].x*side>-0.3
            trees[(side,cls)]=build(f)
    for n in bonenames:
        if n not in ob.vertex_groups: ob.vertex_groups.new(name=n)
    cnt=Counter()
    for v in ob.data.vertices:
        p=v.co
        bn=override(p) if override else None
        if bn is None:
            cls=region(p) if region else 'body'
            side=0 if abs(p.x)<0.6 else (1 if p.x>0 else -1)
            kd,pts=trees[(side,cls)]
            if len(pts)==0: kd,pts=trees[(0,cls)]
            bn=pts[kd.find(p)[1]][1]
        ob.vertex_groups[bn].add([v.index],1.0,'REPLACE'); cnt[bn]+=1
    ob.parent=arm
    m=ob.modifiers.new('Armature','ARMATURE'); m.object=arm
    return cnt

def box_uv(ob,side_bias=1.25):
    """hand-style projection UVs: mirrored side view (y,z) for flanks, separate top/bottom/front/back projections; then pack."""
    me=ob.data
    bm=bmesh.new(); bm.from_mesh(me)
    uvl=bm.loops.layers.uv.verify()
    for f in bm.faces:
        n=f.normal; ax,ay,az=abs(n.x)*side_bias,abs(n.y),abs(n.z)
        for l in f.loops:
            c=l.vert.co
            if ax>=ay and ax>=az: uv=(c.y,c.z)
            elif az>=ay: uv=(c.y, c.x+(1000 if n.z>0 else 2000))
            else: uv=(c.x+(3000 if n.y<0 else 4000), c.z)
            l[uvl].uv=uv
    bm.to_mesh(me); bm.free()
    select_only(ob)
    bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.select_all(action='SELECT')
    try:
        bpy.ops.uv.pack_islands(rotate=False,margin=0.03,merge_overlap=True,shape_method='CONCAVE')
    except TypeError as e:
        print('pack fallback',e); bpy.ops.uv.pack_islands(rotate=False,margin=0.03)
    bpy.ops.object.mode_set(mode='OBJECT')

def N(nt,t,**kw):
    n=nt.nodes.new(t)
    for k,v in kw.items():
        if k.startswith('i_'): n.inputs[k[2:].replace('_',' ')].default_value=v
        else: setattr(n,k,v)
    return n
def L(nt,a,b): nt.links.new(a,b)
def newmat(name):
    m=bpy.data.materials.new(name); m.use_nodes=True; nt=m.node_tree
    for n in list(nt.nodes): nt.nodes.remove(n)
    out=nt.nodes.new('ShaderNodeOutputMaterial'); bs=nt.nodes.new('ShaderNodeBsdfDiffuse')
    nt.links.new(bs.outputs[0],out.inputs[0]); return m,nt,bs.inputs['Color']
def mix(nt,a,b,fac,blend='MIX'):
    m=N(nt,'ShaderNodeMix',data_type='RGBA',blend_type=blend)
    for s,v in (('A',a),('B',b)):
        if isinstance(v,tuple): m.inputs[s].default_value=v
        else: L(nt,v,m.inputs[s])
    if isinstance(fac,float): m.inputs['Factor'].default_value=fac
    else: L(nt,fac,m.inputs['Factor'])
    return m.outputs['Result']
def maprange(nt,v,a,b,c=0.0,d=1.0):
    m=N(nt,'ShaderNodeMapRange'); m.inputs['From Min'].default_value=a; m.inputs['From Max'].default_value=b
    m.inputs['To Min'].default_value=c; m.inputs['To Max'].default_value=d; L(nt,v,m.inputs['Value']); return m.outputs['Result']
def skin_material(name,S):
    """S: dict(colA,colB,dark,belly,mscale,pattern('scales'|'wrinkle'|'stripes'|'fur'),pscale,pstrength,eyes=[(x,y,z,r)],stripe=(scale,strength))"""
    m,nt,col=newmat(name)
    g=N(nt,'ShaderNodeNewGeometry'); pos=g.outputs['Position']
    sp=N(nt,'ShaderNodeSeparateXYZ'); L(nt,pos,sp.inputs[0])
    sn=N(nt,'ShaderNodeSeparateXYZ'); L(nt,g.outputs['Normal'],sn.inputs[0])
    n1=N(nt,'ShaderNodeTexNoise',i_Scale=S.get('mscale',0.15),i_Detail=5.0,i_Roughness=0.6); L(nt,pos,n1.inputs['Vector'])
    r1=N(nt,'ShaderNodeValToRGB'); L(nt,n1.outputs['Fac'],r1.inputs[0])
    e=r1.color_ramp.elements; e[0].position=0.38; e[0].color=lin(S['colA']); e[1].position=0.66; e[1].color=lin(S['colB'])
    c=r1.outputs['Color']
    c=mix(nt,c,lin(S['dark']),maprange(nt,sn.outputs['Z'],0.25,1.0,0.0,S.get('darkf',0.7)))
    c=mix(nt,c,lin(S['belly']),maprange(nt,sn.outputs['Z'],-0.25,-0.9,0.0,S.get('bellyf',0.85)))
    if 'stripe' in S:   # faint vertical stripes / dapples along the body
        sc,st=S['stripe']
        w=N(nt,'ShaderNodeTexWave',wave_type='BANDS',bands_direction='Y',i_Scale=sc,i_Distortion=2.5,i_Detail=1.0); L(nt,pos,w.inputs['Vector'])
        f=maprange(nt,w.outputs['Fac'],0.55,0.9,0.0,st)
        c=mix(nt,c,lin(S['dark']),f)
    if 'dapple' in S:
        sc,st=S['dapple']
        v=N(nt,'ShaderNodeTexVoronoi',feature='F1',i_Scale=sc); L(nt,pos,v.inputs['Vector'])
        f=maprange(nt,v.outputs['Distance'],0.15,0.45,st,0.0)
        c=mix(nt,c,lin(S['belly']),f)
    if 'dorsal' in S:   # darker stripe along the spine
        ab0=N(nt,'ShaderNodeMath',operation='ABSOLUTE'); L(nt,sp.outputs['X'],ab0.inputs[0])
        wdt,stg=S['dorsal']
        m1=maprange(nt,ab0.outputs[0],wdt,wdt*0.4,0.0,1.0); m2=maprange(nt,sn.outputs['Z'],0.35,0.75,0.0,stg)
        mm=N(nt,'ShaderNodeMath',operation='MULTIPLY'); L(nt,m1,mm.inputs[0]); L(nt,m2,mm.inputs[1])
        c=mix(nt,c,lin(S['dark']),mm.outputs[0])
    pat=S.get('pattern','wrinkle'); ps=S.get('pscale',0.9); pst=S.get('pstrength',0.4)
    if pat in ('scales','wrinkle'):
        vo=N(nt,'ShaderNodeTexVoronoi',feature='DISTANCE_TO_EDGE',i_Scale=ps); L(nt,pos,vo.inputs['Vector'])
        k=maprange(nt,vo.outputs['Distance'],0.0,0.1,1.0-pst,1.0)
        cc=N(nt,'ShaderNodeCombineColor'); [L(nt,k,cc.inputs[i]) for i in range(3)]
        c=mix(nt,c,cc.outputs[0],1.0,'MULTIPLY')
    if pat=='fur':
        nn=N(nt,'ShaderNodeTexNoise',i_Scale=ps,i_Detail=8.0,i_Roughness=0.7); L(nt,pos,nn.inputs['Vector'])
        k=maprange(nt,nn.outputs['Fac'],0.3,0.7,1.0-pst,1.0)
        cc=N(nt,'ShaderNodeCombineColor'); [L(nt,k,cc.inputs[i]) for i in range(3)]
        c=mix(nt,c,cc.outputs[0],1.0,'MULTIPLY')
    for (ex,ey,ez,er) in S.get('eyes',[]):
        ab=N(nt,'ShaderNodeMath',operation='ABSOLUTE'); L(nt,sp.outputs['X'],ab.inputs[0])
        ce=N(nt,'ShaderNodeCombineXYZ'); L(nt,ab.outputs[0],ce.inputs['X']); L(nt,sp.outputs['Y'],ce.inputs['Y']); L(nt,sp.outputs['Z'],ce.inputs['Z'])
        ds=N(nt,'ShaderNodeVectorMath',operation='DISTANCE'); L(nt,ce.outputs[0],ds.inputs[0]); ds.inputs[1].default_value=(ex,ey,ez)
        c=mix(nt,c,(0.015,0.012,0.01,1),maprange(nt,ds.outputs['Value'],er*0.75,er,1.0,0.0))
    L(nt,c,col); return m
def flat_material(name,color,noise=0.3,scale=0.8):
    m,nt,col=newmat(name)
    g=N(nt,'ShaderNodeNewGeometry'); n=N(nt,'ShaderNodeTexNoise',i_Scale=scale,i_Detail=3.0); L(nt,g.outputs['Position'],n.inputs['Vector'])
    r=N(nt,'ShaderNodeValToRGB'); L(nt,n.outputs['Fac'],r.inputs[0])
    c=lin(color); e=r.color_ramp.elements; e[0].color=tuple(x*(1-noise) for x in c[:3])+(1,); e[1].color=c
    L(nt,r.outputs['Color'],col); return m

def bake(ob,mats,size,hide=()):
    import numpy as np
    sc=bpy.context.scene; sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=64
    prev=[o.hide_render for o in hide]
    for o in hide: o.hide_render=True
    me=ob.data
    def target(im):
        for m in mats:
            nt=m.node_tree; t=nt.nodes.get('BAKE') or nt.nodes.new('ShaderNodeTexImage'); t.name='BAKE'; t.image=im; nt.nodes.active=t
    dif=bpy.data.images.new('tmp_dif',size,size); ao=bpy.data.images.new('tmp_ao',size,size)
    select_only(ob)
    sc.render.bake.margin=max(2,size//32)
    target(dif); bpy.ops.object.bake(type='DIFFUSE',pass_filter={'COLOR'})
    target(ao); bpy.ops.object.bake(type='AO')
    d=np.array(dif.pixels[:]).reshape(size,size,4); a=np.array(ao.pixels[:]).reshape(size,size,4)
    out=d.copy(); out[...,:3]=d[...,:3]*(0.55+0.45*a[...,:1]); out[...,3]=1.0
    bpy.data.images.remove(dif); bpy.data.images.remove(ao)
    for o,pv in zip(hide,prev): o.hide_render=pv
    return out   # sRGB-encoded floats, rows bottom-up

def save_png(arr,path,name='out'):
    h,w=arr.shape[0],arr.shape[1]
    im=bpy.data.images.new(name,w,h,alpha=True); im.pixels[:]=arr.ravel()
    im.filepath_raw=path; im.file_format='PNG'; im.save(); return im

def final_material(ob,name,imgpath):
    me=ob.data; me.materials.clear()
    m=bpy.data.materials.new(name); m.use_nodes=True; nt=m.node_tree
    b=nt.nodes['Principled BSDF']; b.inputs['Roughness'].default_value=0.85
    t=nt.nodes.new('ShaderNodeTexImage'); t.image=bpy.data.images.load(imgpath); t.image.pack()
    L(nt,t.outputs['Color'],b.inputs['Base Color']); me.materials.append(m)
    for p in me.polygons: p.material_index=0
    return m
def tex_material(ob,imgpath):
    m=ob.material_slots[0].material; m.use_nodes=True; nt=m.node_tree
    b=nt.nodes.get('Principled BSDF'); t=nt.nodes.new('ShaderNodeTexImage'); t.image=bpy.data.images.load(imgpath)
    L(nt,t.outputs['Color'],b.inputs['Base Color']); b.inputs['Roughness'].default_value=0.85; b.inputs['Metallic'].default_value=0.0

# ---------- rendering
def setup_scene():
    sc=bpy.context.scene
    sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=40; sc.cycles.use_denoising=True
    sc.view_settings.view_transform='Standard'
    w=bpy.data.worlds.new('w'); sc.world=w; w.use_nodes=True
    w.node_tree.nodes['Background'].inputs[0].default_value=(0.55,0.62,0.72,1); w.node_tree.nodes['Background'].inputs[1].default_value=0.9
    bpy.ops.mesh.primitive_plane_add(size=800,location=(0,0,0)); g=bpy.context.object; g.name='ground'
    gm=bpy.data.materials.new('ground'); gm.use_nodes=True; gb=gm.node_tree.nodes['Principled BSDF']
    gb.inputs['Base Color'].default_value=(0.20,0.17,0.10,1); gb.inputs['Roughness'].default_value=1.0; g.data.materials.append(gm)
    sd=bpy.data.lights.new('sun','SUN'); sd.energy=3.2; sd.angle=math.radians(8)
    so=bpy.data.objects.new('sun',sd); sc.collection.objects.link(so); so.rotation_euler=(math.radians(40),0,math.radians(-35))
    cd=bpy.data.cameras.new('cam'); cam=bpy.data.objects.new('cam',cd); sc.collection.objects.link(cam); sc.camera=cam
    return cam
def shot(cam,path,loc,target,ortho=None,lens=50,res=(1000,700)):
    sc=bpy.context.scene; sc.render.resolution_x,sc.render.resolution_y=res
    if ortho: cam.data.type='ORTHO'; cam.data.ortho_scale=ortho
    else: cam.data.type='PERSP'; cam.data.lens=lens
    cam.location=loc; cam.rotation_euler=(Vector(target)-Vector(loc)).to_track_quat('-Z','Y').to_euler()
    sc.render.filepath=path; bpy.ops.render.render(write_still=True)
def set_action(arm,act):
    ad=arm.animation_data_create(); ad.action=act
    if act is not None:
        try:
            if act.slots: ad.action_slot=act.slots[0]
        except Exception: pass
    else:
        for pb in arm.pose.bones: pb.matrix_basis.identity()

def fix_child_order(path,ref):
    """Blender's glTF exporter re-sorts sibling bones; restore the original game's depth-first bone order."""
    import json,struct
    d=open(path,'rb').read()
    l0=struct.unpack('<I',d[12:16])[0]; j=json.loads(d[20:20+l0]); rest=d[20+l0:]
    pos={n:i for i,n in enumerate(ref)}
    for n in j['nodes']:
        if 'children' in n: n['children'].sort(key=lambda c: pos.get(j['nodes'][c].get('name'),10**6))
    for s in j.get('scenes',[]): s['nodes'].sort(key=lambda c: pos.get(j['nodes'][c].get('name'),10**6))
    js=json.dumps(j,separators=(',',':')).encode()
    js+=b' '*((4-len(js)%4)%4)
    out=d[:8]+struct.pack('<I',12+8+len(js)+len(rest))+struct.pack('<I',len(js))+b'JSON'+js+rest
    open(path,'wb').write(out)

def segdist(p,a,b):
    a=Vector(a); b=Vector(b); ab=b-a; t=max(0.0,min(1.0,(p-a).dot(ab)/ab.length_squared)); return (p-(a+ab*t)).length
def chain_bone(p,chains):
    """chains: list of (bone,a,b); returns bone of nearest segment"""
    return min(chains,key=lambda c:segdist(p,c[1],c[2]))[0]
