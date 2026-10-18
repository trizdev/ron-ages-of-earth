import bpy,sys,os,math
sys.path.insert(0,'/workspace/prehistoric-herds/scripts')
from lib import *
from mathutils import Vector
G='/workspace/prehistoric-herds/skysea/glb/'; S='/workspace/prehistoric-herds/skysea/src/'; O='/workspace/prehistoric-herds/skysea/orig_views/'
jobs=[('bird_dirty','bird_flap','bird_dirty.tga'),('bird_dirty','bird_soar','bird_dirty.tga'),('bird_gul','bird_flap','bird_gul.tga'),('flock','flock_move1','flock.tga'),('fish1','fish_swim1','fishherd.tga'),('whale','whale_walk3','whale.tga')]
for m,a,t in jobs:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=G+f'{m}_{a}.glb')
    arm=[o for o in bpy.data.objects if o.type=='ARMATURE'][0]
    me=[o for o in bpy.data.objects if o.type=='MESH' and o.parent==arm][0]
    for o in bpy.data.objects:
        if o.type=='MESH' and o.parent is None: o.hide_render=True
    tex_material(me,S+t)
    act=arm.animation_data.action; f0,f1=act.frame_range
    cam=setup_scene()
    bpy.data.objects['ground'].location.z=-60
    sc=bpy.context.scene
    for k,fr in enumerate([f0+(f1-f0)*i/4 for i in range(4)]):
        sc.frame_set(int(fr))
        dg=bpy.context.evaluated_depsgraph_get(); e=me.evaluated_get(dg); pts=[e.matrix_world@v.co for v in e.data.vertices]
        mn=Vector([min(p[i] for p in pts) for i in range(3)]); mx=Vector([max(p[i] for p in pts) for i in range(3)]); C=(mn+mx)/2; R=(mx-mn).length
        shot(cam,O+f'{m}_{a}_{k}.png',(C.x+R*0.9,C.y-R*1.3,C.z+R*1.0),C,lens=50,res=(500,400))
