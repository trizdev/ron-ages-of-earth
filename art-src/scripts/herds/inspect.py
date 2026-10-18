import bpy, sys
from collections import Counter
f=sys.argv[sys.argv.index('--')+1]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=f)
arm=[o for o in bpy.data.objects if o.type=='ARMATURE'][0]
if arm.animation_data: arm.animation_data.action=None
print('OBJS',[(o.name,o.type) for o in bpy.data.objects])
for b in arm.data.bones:
    h=arm.matrix_world@b.head_local
    print('BONE %-14s %-14s (%.1f, %.1f, %.1f)'%(b.name,b.parent.name if b.parent else '-',h.x,h.y,h.z))
for m in [o for o in bpy.data.objects if o.type=='MESH' and o.parent]:
    c=Counter(m.vertex_groups[max(v.groups,key=lambda g:g.weight).group].name for v in m.data.vertices if v.groups)
    print('MESH',m.name,len(m.data.vertices),len(m.data.polygons),dict(c))
    print('MAT',[s.material.name for s in m.material_slots])
for a in bpy.data.actions: print('ACT',a.name,a.frame_range[:])
