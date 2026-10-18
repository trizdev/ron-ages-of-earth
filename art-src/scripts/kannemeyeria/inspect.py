import bpy, mathutils
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath='/workspace/kannemeyeria/src/bison_walk.glb')
for o in bpy.data.objects:
    print('OBJ',o.name,o.type,o.parent.name if o.parent else None,tuple(round(x,3) for x in o.location),tuple(round(x,3) for x in o.rotation_euler),tuple(round(x,3) for x in o.scale))
arm=[o for o in bpy.data.objects if o.type=='ARMATURE'][0]
for b in arm.data.bones:
    print('BONE',b.name,b.parent.name if b.parent else None,[round(x,3) for x in (arm.matrix_world@b.head_local)],[round(x,3) for x in (arm.matrix_world@b.tail_local)])
me=[o for o in bpy.data.objects if o.type=='MESH']
for m in me:
    ws=[mathutils.Vector(m.matrix_world@v.co) for v in m.data.vertices]
    print('MESH',m.name,len(m.data.vertices),len(m.data.polygons),'min',[round(min(w[i] for w in ws),3) for i in range(3)],'max',[round(max(w[i] for w in ws),3) for i in range(3)])
    print(' groups',[g.name for g in m.vertex_groups])
    multi=sum(1 for v in m.data.vertices if len([g for g in v.groups if g.weight>0])>1)
    print(' multiweight verts',multi, 'uv',[u.name for u in m.data.uv_layers], 'mats',[s.material.name if s.material else None for s in m.material_slots])
    from collections import Counter
    c=Counter(m.vertex_groups[max(v.groups,key=lambda g:g.weight).group].name for v in m.data.vertices if v.groups)
    print(' bone vert counts',dict(c))
print('ACTIONS',[(a.name,a.frame_range[:]) for a in bpy.data.actions])
print('fps',bpy.context.scene.render.fps)
