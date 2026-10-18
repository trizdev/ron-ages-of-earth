import bpy
from collections import defaultdict
for m,pairs in [('fish1',[('ammo node 0','tail04'),('ammo node 1','tail03'),('ammo node 2','tail01'),('ammo node 3','tail'),('head02','tail02')]),('flock',[('bird','wing','wing02'),('bird01','wing04','wing06'),('bird02','wing08','wing10'),('bird03','wing12','wing14')])]:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=f'/workspace/prehistoric-herds/skysea/glb/{m}_plain.glb')
    arm=[o for o in bpy.data.objects if o.type=='ARMATURE'][0]
    o=[o for o in bpy.data.objects if o.type=='MESH' and o.parent==arm][0]
    d=defaultdict(list)
    for v in o.data.vertices:
        g=max(v.groups,key=lambda g:g.weight); d[o.vertex_groups[g.group].name].append(o.matrix_world@v.co)
    for p in pairs:
        vs=sum((d[k] for k in p),[])
        mn=[round(min(v[i] for v in vs),2) for i in range(3)]; mx=[round(max(v[i] for v in vs),2) for i in range(3)]
        bp=[tuple(round(x,2) for x in (arm.matrix_world@arm.data.bones[k].head_local)) for k in p]
        print(m,p,'min',mn,'max',mx,'bones',bp)
