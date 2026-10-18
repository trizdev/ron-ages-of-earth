import bpy,sys,glob,os
from mathutils import Vector
for f in sorted(glob.glob('/workspace/prehistoric-herds/skysea/glb/*.glb')):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=f)
    print('=====',os.path.basename(f))
    for o in bpy.data.objects:
        if o.type=='ARMATURE':
            def walk(b,d=0):
                print('  '*d+b.name, tuple(round(x,1) for x in (o.matrix_world@b.head_local)))
                for c in b.children: walk(c,d+1)
            if 'plain' in f:
                for b in o.data.bones:
                    if not b.parent: walk(b)
        if o.type=='MESH':
            me=o.data; vs=[o.matrix_world@v.co for v in me.vertices]
            mn=Vector([min(v[i] for v in vs) for i in range(3)]); mx=Vector([max(v[i] for v in vs) for i in range(3)])
            tris=sum(len(p.vertices)-2 for p in me.polygons)
            cnt={}
            for v in me.vertices:
                if v.groups:
                    g=max(v.groups,key=lambda g:g.weight); n=o.vertex_groups[g.group].name; cnt[n]=cnt.get(n,0)+1
            print(' MESH',o.name,'v',len(me.vertices),'tris',tris,'min',tuple(round(x,1) for x in mn),'max',tuple(round(x,1) for x in mx),'mats',[m.name for m in me.materials])
            if 'plain' in f: print('  groups',cnt)
    for a in bpy.data.actions: print(' ACTION',a.name,tuple(a.frame_range))
