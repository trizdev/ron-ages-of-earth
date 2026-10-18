import math
from mathutils import Vector, Matrix
from lib import *
S2=lambda: (1,-1)
# ---------------------------------------------------------------- Mesohippus on wild-horse skeleton
def meso_parts(bm,ex):
    def body_def(p):
        q=p.copy(); q.z+=1.6*max(0.0,min(1.0,(p.y+2)/14.0))   # arched back, rump higher than withers
        return q
    ellipsoid(bm,(0,1.5,26.0),(4.7,14.0,6.6),deform=body_def)
    ellipsoid(bm,(0,-8.3,26.6),(4.4,6.0,7.0))
    ellipsoid(bm,(0,11.0,27.6),(4.9,6.2,6.6))
    tube(bm,[(0,-10.5,29.5),(0,-14.0,33.5),(0,-16.6,36.8)],[3.8,3.1,2.6])          # short neck
    ellipsoid(bm,(0,-18.8,37.6),(2.5,3.2,2.8))                                       # skull
    tube(bm,[(0,-19.8,37.0),(0,-23.2,34.6)],[1.9,1.35],joints=False)                 # short face
    ellipsoid(bm,(0,-23.3,34.5),(1.45,1.6,1.45))                                     # muzzle
    for s in S2():
        cone(bm,(s*1.2,-17.8,39.8),(s*1.5,-17.2,42.4),0.75,0.15,8)                    # ears
    tube(bm,[(0,16.5,30.5),(0,18.8,26.0),(0,19.6,21.5)],[1.6,1.35,0.9])              # tail
    for s in S2():
        tube(bm,[(s*4.0,-10.3,24.5),(s*3.0,-9.1,11.3),(s*3.2,-9.2,3.6),(s*3.2,-10.5,0.9)],[2.7,1.4,1.0,0.9])
        ellipsoid(bm,(s*3.2,-10.9,0.75),(1.05,1.35,0.75),10,6)
        for t in (-1,1): ellipsoid(bm,(s*3.2+t*0.95,-10.2,0.8),(0.45,0.6,0.5),8,5)   # little side toes
        tube(bm,[(s*4.2,12.0,27.0),(s*4.6,12.8,18.6),(s*4.0,17.2,14.5),(s*4.3,14.3,0.9)],[3.8,2.1,1.15,0.9])
        ellipsoid(bm,(s*4.3,13.8,0.75),(1.05,1.35,0.75),10,6)
        for t in (-1,1): ellipsoid(bm,(s*4.3+t*0.95,14.5,0.8),(0.45,0.6,0.5),8,5)
def meso_faces(c,n):
    if c.z<1.7: return 'hoof'
    if c.y<-22.6: return 'muzzle'
    return 'skin'
MESO=dict(
    folder='mesohippus', src='Wildhorse_1', anim='general_walk', parts=meso_parts, voxel=0.3, smooth=3, target=210,
    legbones=('hipleft','kneeleft','heelleft','heelendleft','hipright','kneeright','heelright','heelendright','sholderleft','elbowleft','wristleft','wristendleft','shoulderright','elbowright','wristright','wristendright'),
    region=lambda p: 'leg' if p.z<18.5 else 'body', override=lambda p: ('tail1' if p.z>26.5 else 'tail2') if (p.y>16.0 and p.z>19.0 and abs(p.x)<2.2) else None,
    faces=meso_faces,
    flats={'hoof':((0.16,0.13,0.10),0.3),'muzzle':((0.20,0.16,0.13),0.3)},
    coats=[  # one per variant
      dict(colA=(0.47,0.34,0.21),colB=(0.53,0.40,0.26),dark=(0.25,0.17,0.10),belly=(0.70,0.60,0.46),stripe=(0.55,0.35),dapple=(0.35,0.35),pattern='fur',pscale=2.5,pstrength=0.25,eyes=[(2.2,-19.6,38.5,0.65)]),
      dict(colA=(0.30,0.20,0.13),colB=(0.36,0.25,0.16),dark=(0.13,0.09,0.06),belly=(0.55,0.45,0.33),stripe=(0.55,0.55),dapple=(0.35,0.30),pattern='fur',pscale=2.5,pstrength=0.25,eyes=[(2.2,-19.6,38.5,0.65)]),
      dict(colA=(0.55,0.49,0.38),colB=(0.50,0.46,0.39),dark=(0.25,0.21,0.16),belly=(0.78,0.72,0.60),stripe=(0.55,0.35),dapple=(0.35,0.35),pattern='fur',pscale=2.5,pstrength=0.25,eyes=[(2.2,-19.6,38.5,0.65)]),
    ],
    variants=[('Wildhorse_1',0,None),('Wildhorse_3',1,None),('Wildhorse_4',2,None)],
    texmode='atlas', texsize=64, texname='WildHorses.tga', size=60, legz=19,
)
# ---------------------------------------------------------------- Diictodon on pig skeleton
def diic_parts(bm,ex):
    def body_def(p):
        q=p.copy()
        if q.z<0: q.z*=0.9
        return q
    ellipsoid(bm,(0,1.2,6.5),(4.4,7.6,3.9),deform=body_def)
    tube(bm,[(0,-5.0,7.4),(0,-7.0,7.8)],[3.4,3.2],joints=False)                     # thick short neck
    def hd(p):
        t=(-p.y)/3.6; return Vector((p.x*(1-0.25*max(0,t)),p.y,p.z))
    ellipsoid(bm,(0,-8.6,7.9),(3.3,3.5,3.0),deform=hd)                              # big head
    ellipsoid(bm,(0,-11.0,6.6),(1.9,1.8,2.2))                                        # deep snout
    ellipsoid(bm,(0,-9.6,5.1),(2.2,2.6,1.1))                                         # jaw
    cone(bm,(0,-11.9,6.6),(0,-12.9,4.4),(1.5,1.8),0.55,10)                           # horny beak
    for s in S2():
        tube(bm,[(s*3.4,-3.9,5.2),(s*4.1,-3.6,3.0),(s*4.0,-4.3,0.5)],[1.7,1.3,1.15])
        ellipsoid(bm,(s*4.1,-4.6,0.45),(1.3,1.6,0.6),10,6)
        tube(bm,[(s*2.8,4.9,5.4),(s*3.2,6.6,3.2),(s*3.1,5.6,0.5)],[2.0,1.4,1.2])
        ellipsoid(bm,(s*3.1,5.3,0.45),(1.3,1.7,0.6),10,6)
    cone(bm,(0,8.2,7.0),(0,10.6,5.6),(1.4,1.2),0.35,8)                               # short tail
    for s in S2(): cone(ex,(s*1.55,-10.8,5.4),(s*1.7,-11.2,3.3),0.42,0.0,5)           # two small tusks
def diic_faces(c,n):
    if c.y<-11.8 and c.z<6.9: return 'beak'
    return 'skin'
DIIC=dict(
    folder='diictodon', src='pig', anim='pig_walk', parts=diic_parts, voxel=0.15, smooth=3, target=150,
    legbones=('shoulder 01','knee RB','ankle RB','shoulder 02','knee LB','ankle LB','shoulder L','knee LF','ankle LF','shoulder R','knee RF','ankle RF'),
    region=lambda p: 'leg' if p.z<3.3 else 'body', override=lambda p: 'neck01' if p.y<-7.0 else None,
    faces=diic_faces, flats={'beak':((0.20,0.17,0.13),0.3),'tusk':((0.82,0.76,0.62),0.15)},
    coats=[
      dict(colA=(0.62,0.48,0.40),colB=(0.58,0.50,0.44),dark=(0.44,0.33,0.27),belly=(0.76,0.64,0.54),mscale=0.4,pattern='wrinkle',pscale=1.6,pstrength=0.35,eyes=[(2.75,-9.3,9.0,0.5)]),
      dict(colA=(0.40,0.35,0.29),colB=(0.45,0.42,0.37),dark=(0.25,0.21,0.17),belly=(0.62,0.55,0.46),mscale=0.4,pattern='wrinkle',pscale=1.6,pstrength=0.35,eyes=[(2.75,-9.3,9.0,0.5)]),
    ],
    variants=[('pig',0,None),('pig_black',1,None)],
    texmode='separate', texsize=64, texnames=['pig.tga','pig_black.tga'], size=27, legz=3.3,
)
# ---------------------------------------------------------------- Leptoceratops on sheep skeleton
def lept_parts(bm,ex):
    def body_def(p):
        q=p.copy(); q.z+=1.3*max(0.0,min(1.0,(p.y+4)/12.0))   # hips higher than shoulders
        return q
    ellipsoid(bm,(0,1.5,14.6),(5.8,11.5,6.2),deform=body_def)                         # stocky body
    ellipsoid(bm,(0,-7.6,14.4),(4.9,4.8,5.6))                                          # chest over the front legs
    ellipsoid(bm,(0,9.5,16.6),(5.2,5.8,5.6))                                           # strong hips
    tube(bm,[(0,12.5,17.2),(0,18.5,15.0),(0,24.5,11.2),(0,28.5,8.4)],[(2.3,4.8),(1.8,3.6),(1.1,2.1),(0.5,0.8)],joints=False)  # deep tail
    tube(bm,[(0,-8.0,17.0),(0,-11.0,19.2),(0,-13.0,20.6)],[3.8,3.4,3.1],joints=False)  # thick neck
    def hd(p):
        t=(-p.y)/4.8; return Vector((p.x*(1-0.3*max(0,t)),p.y,p.z))
    ellipsoid(bm,(0,-15.8,21.2),(3.3,4.8,3.4),deform=hd)                              # big skull
    ellipsoid(bm,(0,-19.8,20.4),(1.8,2.6,2.6))                                         # deep snout
    ellipsoid(bm,(0,-17.4,18.2),(2.3,3.4,1.4))                                         # jaw
    cone(bm,(0,-21.6,21.0),(0,-23.7,18.0),(1.5,1.9),0.45,10)                          # parrot beak (hooked)
    ellipsoid(bm,(0,-11.4,22.4),(4.7,1.7,2.5),16,8,rot=Matrix.Rotation(math.radians(-76),3,'X'))  # short low frill, no horns, laid back over the neck
    for s in S2():
        tube(bm,[(s*3.8,-9.6,12.0),(s*4.0,-9.4,5.8),(s*3.9,-10.0,0.6)],[2.5,1.6,1.25])
        ellipsoid(bm,(s*3.9,-10.6,0.5),(1.3,1.7,0.6),10,6)
        tube(bm,[(s*4.3,9.0,14.0),(s*4.7,11.5,6.4),(s*4.6,10.3,0.6)],[3.6,2.1,1.4])
        ellipsoid(bm,(s*4.6,9.4,0.5),(1.5,2.2,0.6),10,6)
def lept_faces(c,n):
    if c.y<-21.4 and c.z<21.4: return 'beak'
    if frill_mask(c) and n.z>0.2: return 'frill'
    return 'skin'
def frill_mask(co): return co.y>-14.0 and co.y<-9.0 and co.z>21.5 and abs(co.x)<5.4
def frill_scale(f):
    piv=Vector((0,-13.3,22.0))
    def tw(co):
        if frill_mask(co): return piv+(co-piv)*f
        return co
    return tw
def head_scale(f):
    piv=Vector((0,-13.0,20.0))
    def tw(co):
        if co.y<-12.0 and co.z>16.0: return piv+(co-piv)*f
        return co
    return tw
LEPT=dict(
    folder='leptoceratops', src='sheep2', anim='sheep_walk', parts=lept_parts, voxel=0.22, smooth=4, target=190,
    legbones=('shoulder 0','knee RB','ankle RB','shoulder 1','knee LB','ankle LB','shoulder L','knee LF','ankle LF','shoulder R','knee RF','ankle RF'),
    region=lambda p: 'leg' if p.z<8.5 else 'body', override=lambda p: 'base' if (p.y>12.5 and p.z>6.0 and abs(p.x)<3.2) else ('head' if p.y<-12.2 and p.z>15.5 else None),
    faces=lept_faces, flats={'beak':((0.18,0.15,0.11),0.3),'frill':((0.50,0.38,0.20),0.35)},
    coats=[dict(colA=(0.43,0.41,0.24),colB=(0.58,0.45,0.22),dark=(0.27,0.27,0.15),belly=(0.70,0.63,0.45),mscale=0.25,pattern='scales',pscale=1.2,pstrength=0.4,stripe=(0.35,0.3),eyes=[(2.75,-16.8,22.6,0.6)])],
    variants=[('sheep3',0,None),('sheep2',0,'frill'),('sheep1',0,'juv')],
    tweaks={'frill':frill_scale(1.22),'juv':head_scale(1.08)},
    texmode='shared', texsize=64, texname='sheep.tga', size=50, legz=8.5,
)
ANIMALS={'mesohippus':MESO,'diictodon':DIIC,'leptoceratops':LEPT}
