import bpy, math, sys
from mathutils import Vector
W='/workspace/kannemeyeria'; P=W+'/preview/'
sc=bpy.context.scene
arm=bpy.data.objects['Armature']; K=bpy.data.objects['kannemeyeria']; B=bpy.data.objects['bison']
bpy.data.objects['Icosphere'].hide_render=True
act=bpy.data.actions.get('bison_walk')
ad=arm.animation_data_create()
print('ANIMDATA action', ad.action.name if ad.action else None)
def rest():
    ad.action=None
    for pb in arm.pose.bones: pb.matrix_basis.identity()
def walk():
    ad.action=act
    try:
        if act.slots: ad.action_slot=act.slots[0]
    except Exception as e: print('slot',e)
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=48; sc.cycles.use_denoising=True
sc.render.resolution_x=1000; sc.render.resolution_y=700; sc.render.film_transparent=False
sc.view_settings.view_transform='Standard'
w=bpy.data.worlds.new('w'); sc.world=w; w.use_nodes=True
w.node_tree.nodes['Background'].inputs[0].default_value=(0.55,0.62,0.72,1); w.node_tree.nodes['Background'].inputs[1].default_value=0.9
bpy.ops.mesh.primitive_plane_add(size=600,location=(0,0,0)); g=bpy.context.object
gm=bpy.data.materials.new('ground'); gm.use_nodes=True; gb=gm.node_tree.nodes['Principled BSDF']
gb.inputs['Base Color'].default_value=(0.20,0.17,0.10,1); gb.inputs['Roughness'].default_value=1.0; g.data.materials.append(gm)
sd=bpy.data.lights.new('sun','SUN'); sd.energy=3.2; sd.angle=math.radians(8)
so=bpy.data.objects.new('sun',sd); sc.collection.objects.link(so); so.rotation_euler=(math.radians(40),0,math.radians(-35))
cd=bpy.data.cameras.new('cam'); cam=bpy.data.objects.new('cam',cd); sc.collection.objects.link(cam); sc.camera=cam
def aim(loc,target):
    cam.location=loc; d=Vector(target)-Vector(loc); cam.rotation_euler=d.to_track_quat('-Z','Y').to_euler()
def shot(name,loc,target,ortho=None,lens=50,res=(1000,700)):
    sc.render.resolution_x,sc.render.resolution_y=res
    if ortho: cd.type='ORTHO'; cd.ortho_scale=ortho
    else: cd.type='PERSP'; cd.lens=lens
    aim(loc,target); sc.render.filepath=P+name; bpy.ops.render.render(write_still=True); print('WROTE',P+name)
T=(0,-6,15)
rest(); B.hide_render=True
shot('01_side.png',(200,-6,16),T,ortho=80)
shot('02_three_quarter.png',(110,-150,70),(0,-6,14),lens=60)
shot('03_top_ingame_angle.png',(0,-115,125),(0,-4,10),lens=55)   # ~47 deg down, like RoN's camera
shot('04_front.png',(25,-200,30),(0,-6,16),lens=60)
# comparison: bison behind (to the right in side view), same scale
B.hide_render=False; B.location=(0,64,0)
shot('05_compare_side_bison.png',(220,26,22),(0,26,20),ortho=135,res=(1400,700))
B.location=(36,0,0)
shot('06_compare_ingame_angle.png',(-12,-125,135),(18,-4,12),lens=50,res=(1400,800))
B.hide_render=True; B.location=(0,0,0)
# walk pose test
walk()
fs=[]
for f in (4,9,14,19):
    sc.frame_set(f); shot('_walk_f%02d.png'%f,(200,-6,16),T,ortho=80,res=(800,560)); fs.append(P+'_walk_f%02d.png'%f)
sc.frame_set(9); shot('08_walk_three_quarter_f09.png',(110,-150,70),(0,-6,14),lens=60)
rest()
bpy.ops.wm.save_as_mainfile(filepath=W+'/kannemeyeria_preview_scene.blend')
