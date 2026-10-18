import bpy,sys,os,math
sys.path.insert(0,'/workspace/prehistoric-herds/scripts')
from lib import *
from mathutils import Vector
G='/workspace/prehistoric-herds/bipeds/glb/'; S='/workspace/prehistoric-herds/bipeds/src/'; O='/workspace/prehistoric-herds/bipeds/orig_views/'
jobs=[('peacock','peacock_idle2','peafowl.tga'),('peacock','peacock_idle3','peafowl.tga'),('peahen','peahen_idle1','peafowl.tga'),('peahen','peahen_idle2','peafowl.tga')]
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
    bpy.data.objects['ground'].location.z=0
    sc=bpy.context.scene
    for k,fr in enumerate([f0+(f1-f0)*i/4 for i in range(4)]):
        sc.frame_set(int(fr))
        dg=bpy.context.evaluated_depsgraph_get(); e=me.evaluated_get(dg); pts=[e.matrix_world@v.co for v in e.data.vertices]
        mn=Vector([min(p[i] for p in pts) for i in range(3)]); mx=Vector([max(p[i] for p in pts) for i in range(3)]); C=(mn+mx)/2; R=(mx-mn).length
        shot(cam,O+f'{m}_{a}_{k}.png',(C.x+R*1.4,C.y-R*0.9,C.z+R*0.5),C,lens=50,res=(500,400))
