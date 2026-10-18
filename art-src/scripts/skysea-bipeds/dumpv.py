import bpy
from collections import defaultdict
for m in ['whale']:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=f'/workspace/prehistoric-herds/skysea/glb/{m}_plain.glb')
    arm=[o for o in bpy.data.objects if o.type=='ARMATURE'][0]
    o=[o for o in bpy.data.objects if o.type=='MESH' and o.parent==arm][0]
    d=defaultdict(list)
    for v in o.data.vertices:
        g=max(v.groups,key=lambda g:g.weight); d[o.vertex_groups[g.group].name].append(tuple(round(x,1) for x in o.matrix_world@v.co))
    print('=====',m)
    for k,vs in d.items():
        if m.startswith('f') and not (k in ('bird','wing','wing02','ammo node 3','tail','head02','tail02')): continue
        print(' ',k,sorted(set(vs)))
