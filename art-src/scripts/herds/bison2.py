import sys, json, struct, subprocess, os
sys.path.insert(0,'/workspace/prehistoric-herds/scripts')
import bpy
from mathutils import Vector
from lib import *
R='/workspace/kannemeyeria/bison2'
arm=bpy.data.objects['Armature']; K=bpy.data.objects['kannemeyeria']
if arm.animation_data: arm.animation_data.action=None
for pb in arm.pose.bones: pb.matrix_basis.identity()
for o in bpy.data.objects:
    if o.type=='MESH' and o is not K: o.hide_render=True
V=K.copy(); V.data=K.data.copy(); V.name='bison2'; V.data.name='bison2'; bpy.context.scene.collection.objects.link(V)
hc=V.vertex_groups['head con'].index
nt=nb=0
for v in V.data.vertices:
    co=v.co
    g=[x.group for x in v.groups]
    if (-33.5<co.y<-29.0) and co.z<17.2 and 2.0<abs(co.x)<4.6 and hc in g:      # tusks: 30% longer
        s=1 if co.x>0 else -1; base=Vector((s*3.1,-30.9,17.6)); v.co=base+(co-base)*1.3; nt+=1
    elif co.y>-21.0 and co.z>6.0:                                                  # bulkier barrel (+6% wide, +3% deep)
        v.co=Vector((co.x*1.06,co.y,9.0+(co.z-9.0)*1.03 if co.z>9.0 else co.z)); nb+=1
print('TWEAK tusk verts',nt,'body verts',nb)
for x in bpy.context.selected_objects: x.select_set(False)
arm.select_set(True); V.select_set(True); bpy.context.view_layer.objects.active=arm
g=R+'/export/bison2.glb'
bpy.ops.export_scene.gltf(filepath=g,use_selection=True,export_animations=False,export_format='GLB')
def gl(f):
    d=open(f,'rb').read(); l=struct.unpack('<I',d[12:16])[0]; return json.loads(d[20:20+l])
src=[(n.get('name'),n.get('translation') or [0,0,0],n.get('rotation') or [0,0,0,1]) for n in gl('/workspace/prehistoric-herds/src/glb/bison2_plain.glb')['nodes'] if 'mesh' not in n]
fix_child_order(g,[x[0] for x in src])
DOT=['/home/box/opt/dotnet/dotnet','/tmp/rfc/ron-file-converter.dll']
r=subprocess.run(DOT+['gltf',g,'-mo',R+'/export/bison2.BH3'],capture_output=True,text=True)
r2=subprocess.run(DOT+['bh3',R+'/export/bison2.BH3','-o',R+'/export/_reread_bison2.glb'],capture_output=True,text=True)
j=gl(R+'/export/_reread_bison2.glb'); nn=[(n.get('name'),n.get('translation') or [0,0,0],n.get('rotation') or [0,0,0,1]) for n in j['nodes'] if 'mesh' not in n]
mx=0
for a,b in zip(nn,src):
    mx=max(mx,max(abs(p-q) for p,q in zip(a[1],b[1])),min(max(abs(p-q) for p,q in zip(a[2],b[2])),max(abs(p+q) for p,q in zip(a[2],b[2]))))
pm=j['meshes'][0]['primitives'][0]
rep=dict(variant='bison2',convert='succeeded' in r.stdout,reread='succeeded' in r2.stdout,bones_same=[a[0] for a in nn]==[a[0] for a in src],rest_maxdiff=mx,bh3_verts=j['accessors'][pm['attributes']['POSITION']]['count'],bh3_tris=j['accessors'][pm['indices']]['count']//3,bh3_bytes=os.path.getsize(R+'/export/bison2.BH3'))
json.dump(rep,open(R+'/export/verify.json','w'),indent=1); print('REPORT',rep)
# renders: TYPE0/1 (bison2 variant) next to TYPE2 (bison)
for o in bpy.data.objects:
    if o.type in ('LIGHT','CAMERA') or o.name in ('ground',): bpy.data.objects.remove(o)
cam=setup_scene()
K.hide_render=False; V.hide_render=False; K.location=(30,0,0)
shot(cam,R+'/preview/01_bison2_vs_bison_game_angle.png',(0,-130,140),(15,-6,12),lens=50,res=(1300,800))
shot(cam,R+'/preview/02_bison2_vs_bison_three_quarter.png',(140,-160,80),(15,-6,14),lens=55,res=(1300,800))
K.location=(0,0,0); K.hide_render=True
act=bpy.data.actions.get('bison_walk'); set_action(arm,act)
for f in (4,14):
    bpy.context.scene.frame_set(f); shot(cam,R+'/preview/03_bison2_walk_f%02d.png'%f,(200,-6,16),(0,-6,15),ortho=80,res=(800,560))
print('DONE')
