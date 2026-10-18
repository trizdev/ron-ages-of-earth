"""Explicit low-poly builder for RoN sky/sea critters: every vertex carries one bone and a part-local (s,t) UV coordinate."""
import bpy, bmesh, math, json, struct, subprocess, os
import numpy as np
from mathutils import Vector

class MB:
    def __init__(self): self.V=[]; self.F=[]
    def v(self,co,bone,st=(0.5,0.5)):
        self.V.append((Vector(co),bone,tuple(st))); return len(self.V)-1
    def f(self,idx,cls,two=False):
        self.F.append((list(idx),cls))
        if two:
            p=[self.V[i][0] for i in idx]; n=(p[1]-p[0]).cross(p[2]-p[0])
            n=n.normalized() if n.length>1e-9 else Vector((0,0,0))
            sz=max((a-b).length for a in p for b in p); off=n*(-min(0.03,0.004*sz+0.004))
            back=[self.v(self.V[i][0]+off,self.V[i][1],self.V[i][2]) for i in idx]
            self.F.append((back[::-1],cls))
    def build(self,name,arm,rects,texsize):
        me=bpy.data.meshes.new(name); bm=bmesh.new()
        bv=[bm.verts.new(c) for c,_,_ in self.V]; bm.verts.ensure_lookup_table()
        uvl=bm.loops.layers.uv.new('UVMap'); pad=1.0/texsize
        for idx,cls in self.F:
            face=bm.faces.new([bv[i] for i in idx])
            u0,v0,u1,v1=rects[cls]
            for l,i in zip(face.loops,idx):
                s,t=self.V[i][2]; s=min(1,max(0,s)); t=min(1,max(0,t))
                l[uvl].uv=(u0+pad+(u1-u0-2*pad)*s, v0+pad+(v1-v0-2*pad)*t)
            face.smooth=True
        bm.verts.index_update()
        bmesh.ops.triangulate(bm,faces=bm.faces[:])
        assert len(bm.verts)==len(self.V)
        bm.to_mesh(me); bm.free()
        ob=bpy.data.objects.new(name,me); bpy.context.scene.collection.objects.link(ob)
        groups={}
        for i,v in enumerate(me.vertices):
            b=self.V[i][1]
            if b not in groups: groups[b]=ob.vertex_groups.new(name=b)
            groups[b].add([i],1.0,'REPLACE')
        ob.parent=arm; md=ob.modifiers.new('arm','ARMATURE'); md.object=arm
        return ob

def loft(mb,rings,bone_fn,cls,sides=6,cap0=None,cap1=None,two_caps=True,y0=None,y1=None):
    """rings: list of (y,w,zc,h[,xc]); ring vertex k at angle th=2pi k/sides from the top. st=(s,t): s=|th|/pi (0 top,1 bottom), t along y."""
    ys=[r[0] for r in rings]+([cap0[1]] if cap0 else [])+([cap1[1]] if cap1 else [])
    ya=min(ys) if y0 is None else y0; yb=max(ys) if y1 is None else y1
    T=lambda y:(y-ya)/(yb-ya)
    R=[]
    for r in rings:
        y,w,zc,h=r[:4]; xc=r[4] if len(r)>4 else 0.0; ring=[]
        for k in range(sides):
            th=2*math.pi*k/sides; p=Vector((xc+w*math.sin(th),y,zc+h*math.cos(th)))
            s=min(th,2*math.pi-th)/math.pi
            ring.append(mb.v(p,bone_fn(p),(s,T(y))))
        R.append(ring)
    def add(idx,out):
        p=[mb.V[i][0] for i in idx]; n=(p[1]-p[0]).cross(p[2]-p[0])
        if n.length<1e-9 and len(p)>3: n=(p[2]-p[0]).cross(p[3]-p[0])
        if n.dot(out)<0: idx=idx[::-1]
        mb.f(idx,cls)
    for ri,(a,b) in enumerate(zip(R,R[1:])):
        r0=rings[ri]; r1=rings[ri+1]
        for k in range(sides):
            k2=(k+1)%sides; idx=[a[k],a[k2],b[k2],b[k]]
            cen=sum((mb.V[i][0] for i in idx),Vector())/4
            ax=Vector((r0[4] if len(r0)>4 else 0.0,cen.y,(r0[2]+r1[2])/2))
            add(idx,cen-ax)
    def cap(pt,ring,front):
        c=mb.v(pt,bone_fn(Vector(pt)),(0.5,T(pt[1])))
        rc=sum((mb.V[i][0] for i in ring),Vector())/len(ring)
        for k in range(sides):
            k2=(k+1)%sides; idx=[ring[k],ring[k2],c]
            cen=(mb.V[ring[k]][0]+mb.V[ring[k2]][0]+Vector(pt))/3
            add(idx,(Vector(pt)-rc)+(cen-rc)*0.3)
    if cap0: cap(cap0,R[0],True)
    if cap1: cap(cap1,R[-1],False)
    return R

def planar(mb,pts,bones,cls,faces,axes,box,two=True):
    """pts: list of 3D points; bones list; faces: index tuples into pts; st from axes (i,j) normalized by box ((a0,a1),(b0,b1)); uses |x| when axis 0."""
    def st(p):
        q=[abs(p[0]),p[1],p[2]]
        return ((q[axes[0]]-box[0][0])/(box[0][1]-box[0][0]),(q[axes[1]]-box[1][0])/(box[1][1]-box[1][0]))
    ids=[mb.v(p,b,st(p)) for p,b in zip(pts,bones)]
    for f in faces: mb.f([ids[i] for i in f],cls,two=two)
    return ids

# ---------------- painting (numpy, rows top-down)
_rng=np.random.default_rng(7)
def vnoise(h,w,cells,seed=0):
    r=np.random.default_rng(seed); g=r.random((cells+2,cells+2))
    ys=np.linspace(0,cells,h); xs=np.linspace(0,cells,w)
    yi=ys.astype(int); xi=xs.astype(int); fy=(ys-yi)[:,None]; fx=(xs-xi)[None,:]
    fy=fy*fy*(3-2*fy); fx=fx*fx*(3-2*fx)
    a=g[yi][:,xi]; b=g[yi][:,xi+1]; c=g[yi+1][:,xi]; d=g[yi+1][:,xi+1]
    return a*(1-fx)*(1-fy)+b*fx*(1-fy)+c*(1-fx)*fy+d*fx*fy
def paint(texsize,rects,painters,seed=1):
    img=np.zeros((texsize,texsize,3))
    for cls,(u0,v0,u1,v1) in rects.items():
        c0=int(round(u0*texsize)); c1=int(round(u1*texsize)); r0=int(round((1-v1)*texsize)); r1=int(round((1-v0)*texsize))
        h=r1-r0; w=c1-c0
        if h<=0 or w<=0: continue
        pad=1.0
        s=((np.arange(w)+0.5-pad)/(w-2*pad))[None,:].repeat(h,0)
        t=(1-(np.arange(h)+0.5-pad)/(h-2*pad))[:,None].repeat(w,1)
        col=painters[cls](np.clip(s,0,1),np.clip(t,0,1),(h,w))
        img[r0:r1,c0:c1]=np.clip(col,0,1)
    return img
def C(c,shape): return np.ones(shape+(3,))*np.array(c)[None,None,:]
def lerp(a,b,f): return a+(b-a)*f[...,None]
def smooth(e0,e1,x): t=np.clip((x-e0)/(e1-e0),0,1); return t*t*(3-2*t)
def save_rgb(img,path):
    h,w,_=img.shape; im=bpy.data.images.new(os.path.basename(path),w,h,alpha=True)
    a=np.ones((h,w,4)); a[...,:3]=img[::-1]; im.pixels[:]=a.ravel(); im.filepath_raw=path; im.file_format='PNG'; im.save(); return im

# --------------- export / verify (same checks as the herd pipeline)
DOT=['/home/box/opt/dotnet/dotnet','/home/box/opt/rfc/ron-file-converter.dll']
def gl(f):
    d=open(f,'rb').read(); l=struct.unpack('<I',d[12:16])[0]; return json.loads(d[20:20+l])
def fix_child_order(path,ref):
    d=open(path,'rb').read()
    l0=struct.unpack('<I',d[12:16])[0]; j=json.loads(d[20:20+l0]); rest=d[20+l0:]
    pos={n:i for i,n in enumerate(ref)}
    for n in j['nodes']:
        if 'children' in n: n['children'].sort(key=lambda c: pos.get(j['nodes'][c].get('name'),10**6))
    for s in j.get('scenes',[]): s['nodes'].sort(key=lambda c: pos.get(j['nodes'][c].get('name'),10**6))
    js=json.dumps(j,separators=(',',':')).encode(); js+=b' '*((4-len(js)%4)%4)
    open(path,'wb').write(d[:8]+struct.pack('<I',12+8+len(js)+len(rest))+struct.pack('<I',len(js))+b'JSON'+js+rest)
def export_verify(arm,ob,srcglb,outdir,name,orig=None):
    srcj=gl(srcglb); srcnodes=[(n.get('name'),n.get('translation'),n.get('rotation')) for n in srcj['nodes'] if 'mesh' not in n]
    for x in bpy.context.selected_objects: x.select_set(False)
    arm.select_set(True); ob.select_set(True); bpy.context.view_layer.objects.active=arm
    g=f"{outdir}/{name}.glb"
    bpy.ops.export_scene.gltf(filepath=g,use_selection=True,export_animations=False,export_format='GLB')
    fix_child_order(g,[x[0] for x in srcnodes])
    b3=f"{outdir}/{name}.BH3"
    r=subprocess.run(DOT+['gltf',g,'-mo',b3],capture_output=True,text=True); ok1='succeeded' in r.stdout
    rr=f"{outdir}/_reread_{name}.glb"
    r2=subprocess.run(DOT+['bh3',b3,'-o',rr],capture_output=True,text=True); ok2='succeeded' in r2.stdout
    if not ok1: print('CONVERR',r.stdout[-800:],r.stderr[-800:])
    j=gl(rr); nn=[(n.get('name'),n.get('translation'),n.get('rotation')) for n in j['nodes'] if 'mesh' not in n]
    same=[a[0] for a in nn]==[a[0] for a in srcnodes]; mx=0
    for a,b in zip(nn,srcnodes):
        for i in (1,2):
            x=a[i] or ([0,0,0] if i==1 else [0,0,0,1]); y=b[i] or ([0,0,0] if i==1 else [0,0,0,1])
            dd=max(abs(p-q) for p,q in zip(x,y))
            if i==2: dd=min(dd,max(abs(p+q) for p,q in zip(x,y)))
            mx=max(mx,dd)
    pm=j['meshes'][0]['primitives'][0]
    nv=j['accessors'][pm['attributes']['POSITION']]['count']; nt=j['accessors'][pm['indices']]['count']//3
    multi=sum(1 for v in ob.data.vertices if len(v.groups)!=1)
    rep=dict(file=name+'.BH3',convert=ok1,reread=ok2,bones_same=same,rest_maxdiff=mx,bh3_verts=nv,bh3_tris=nt,blender_tris=len(ob.data.polygons),multi_weight=multi,bh3_bytes=os.path.getsize(b3) if ok1 else 0)
    if orig is not None: rep['orig_tris']=len(orig.data.polygons); rep['orig_verts']=len(orig.data.vertices)
    return rep

# --------------- scene
def setup_scene(ground=(0.20,0.17,0.10),gz=-40):
    sc=bpy.context.scene
    sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=32; sc.cycles.use_denoising=True
    sc.view_settings.view_transform='Standard'
    w=bpy.data.worlds.new('w'); sc.world=w; w.use_nodes=True
    w.node_tree.nodes['Background'].inputs[0].default_value=(0.55,0.62,0.72,1); w.node_tree.nodes['Background'].inputs[1].default_value=0.9
    bpy.ops.mesh.primitive_plane_add(size=2000,location=(0,0,gz)); g=bpy.context.object; g.name='ground'
    gm=bpy.data.materials.new('ground'); gm.use_nodes=True; gb=gm.node_tree.nodes['Principled BSDF']
    gb.inputs['Base Color'].default_value=tuple(ground)+(1,); gb.inputs['Roughness'].default_value=1.0; g.data.materials.append(gm)
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
def img_material(ob,path,name):
    m=bpy.data.materials.new(name); m.use_nodes=True; nt=m.node_tree
    b=nt.nodes['Principled BSDF']; b.inputs['Roughness'].default_value=0.85
    t=nt.nodes.new('ShaderNodeTexImage'); t.image=bpy.data.images.load(path); t.interpolation='Closest' if False else 'Linear'
    nt.links.new(t.outputs['Color'],b.inputs['Base Color'])
    ob.data.materials.clear(); ob.data.materials.append(m)
    try: m.use_backface_culling=False
    except Exception: pass
    return m
def evaluated_bbox(objs):
    dg=bpy.context.evaluated_depsgraph_get(); pts=[]
    for o in objs:
        e=o.evaluated_get(dg); pts+=[e.matrix_world@v.co for v in e.data.vertices]
    mn=Vector([min(p[i] for p in pts) for i in range(3)]); mx=Vector([max(p[i] for p in pts) for i in range(3)]); return mn,mx

# ---------------- biped helpers
def segdist(p,a,b):
    ab=b-a; t=max(0.0,min(1.0,(p-a).dot(ab)/max(ab.length_squared,1e-9))); return (p-(a+ab*t)).length
def seg_bone(segs):
    """segs: list of (bone, a, b) Vectors -> function p -> bone of the nearest segment"""
    return lambda p: min(segs,key=lambda s: segdist(Vector(p),s[1],s[2]))[0]
def tube(mb,pts,radii,bone_fn,cls,sides=5,ref=Vector((0,0,1)),cap0=None,cap1=None):
    """rings perpendicular to a polyline. radii: r or (ru,rv) per point (ru along ref). st: s=angle from ref folded (0..1), t=length fraction."""
    pts=[Vector(p) for p in pts]; n=len(pts)
    L=[0.0]
    for a,b in zip(pts,pts[1:]): L.append(L[-1]+(b-a).length)
    tot=L[-1]+(cap0 or 0)+(cap1 or 0); off=cap0 or 0
    R=[]; frames=[]
    for i,p in enumerate(pts):
        tg=(pts[min(i+1,n-1)]-pts[max(i-1,0)]).normalized()
        u=(Vector(ref)-tg*Vector(ref).dot(tg))
        if u.length<1e-4: u=Vector((0,-1,0))-tg*Vector((0,-1,0)).dot(tg)
        u.normalize(); v=tg.cross(u); frames.append(tg)
        r=radii[i]; ru,rv=(r,r) if not isinstance(r,(tuple,list)) else r
        ring=[]
        for k in range(sides):
            th=2*math.pi*k/sides; q=p+u*(ru*math.cos(th))+v*(rv*math.sin(th))
            ring.append(mb.v(q,bone_fn(q),(min(th,2*math.pi-th)/math.pi,(L[i]+off)/tot)))
        R.append(ring)
    def add(idx,out):
        P=[mb.V[i][0] for i in idx]; nn=(P[1]-P[0]).cross(P[2]-P[0])
        if nn.dot(out)<0: idx=idx[::-1]
        mb.f(idx,cls)
    for i in range(n-1):
        axis=(pts[i]+pts[i+1])/2
        for k in range(sides):
            k2=(k+1)%sides; idx=[R[i][k],R[i][k2],R[i+1][k2],R[i+1][k]]
            cen=sum((mb.V[j][0] for j in idx),Vector())/4; add(idx,cen-axis)
    for c,i,sgn,tt in ((cap0,0,-1,0.0),(cap1,n-1,1,1.0)):
        if not c: continue
        tip=pts[i]+frames[i]*c*sgn; ti=mb.v(tip,bone_fn(tip),(0.5,tt))
        for k in range(sides):
            idx=[R[i][k],R[i][(k+1)%sides],ti]; add(idx,frames[i]*sgn)
    return R
def poly(mb,pts,bones,sts,cls,faces,two=True):
    ids=[mb.v(Vector(p),b,st) for p,b,st in zip(pts,bones,sts)]
    for f in faces: mb.f([ids[i] for i in f],cls,two=two)
    return ids
def vnoise2(h,w,cy,cx,seed=0):
    r=np.random.default_rng(seed); g=r.random((cy+2,cx+2))
    ys=np.linspace(0,cy,h); xs=np.linspace(0,cx,w)
    yi=ys.astype(int); xi=xs.astype(int); fy=(ys-yi)[:,None]; fx=(xs-xi)[None,:]
    fy=fy*fy*(3-2*fy); fx=fx*fx*(3-2*fx)
    a=g[yi][:,xi]; b=g[yi][:,xi+1]; c=g[yi+1][:,xi]; d=g[yi+1][:,xi+1]
    return a*(1-fx)*(1-fy)+b*fx*(1-fy)+c*(1-fx)*fy+d*fx*fy
