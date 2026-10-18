import bpy
W='/workspace/kannemeyeria'
arm=bpy.data.objects['Armature']; K=bpy.data.objects['kannemeyeria']
if arm.animation_data: arm.animation_data.action=None
for pb in arm.pose.bones: pb.matrix_basis.identity()
for o in bpy.context.selected_objects: o.select_set(False)
arm.select_set(True); K.select_set(True); bpy.context.view_layer.objects.active=arm
bpy.ops.export_scene.gltf(filepath=W+'/export/kannemeyeria.glb',use_selection=True,export_animations=False,export_format='GLB')
