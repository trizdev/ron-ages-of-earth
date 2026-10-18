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

# ======================================================================= v2 redesigns
def _side_chains(front, hind):
    """front/hind: dict side-> list of (bone, a, b) ; returns chooser"""
    def pick(p):
        s='L' if p.x>=0 else 'R'
        return chain_bone(p, front[s] if p.y<2.0 else hind[s])
    return pick
# ---------------- Mesohippus v2: small stocky early horse
def meso2_parts(bm,ex):
    def body_def(p):
        q=p.copy(); q.z+=1.0*max(0.0,min(1.0,(p.y+2)/14.0))     # slight rise to the rump
        return q
    ellipsoid(bm,(0,1.0,24.2),(6.3,15.5,8.6),deform=body_def)            # full round barrel, belly ~15.6
    ellipsoid(bm,(0,-9.0,24.6),(5.7,6.6,9.2))                             # deep chest
    ellipsoid(bm,(0,11.0,25.6),(6.2,7.4,7.6))                             # round rump
    tube(bm,[(0,-10.5,29.5),(0,-13.6,34.2),(0,-16.3,37.6)],[(5.2,4.0),(4.2,3.2),(3.4,2.7)],joints=False)   # short thick neck (height,width)
    ellipsoid(bm,(0,-13.0,37.9),(0.95,4.9,2.2),12,8,rot=Matrix.Rotation(math.radians(-48),3,'X'))         # short upright mane
    # horse head: forehead -> slightly arched snout -> muzzle
    tube(bm,[(0,-17.4,39.2),(0,-20.8,37.3),(0,-24.0,35.0)],[(3.1,2.5),(2.5,2.0),(2.0,1.6)],joints=False)
    ellipsoid(bm,(0,-18.4,37.0),(2.6,2.9,2.7))                            # cheek / jowl
    ellipsoid(bm,(0,-21.0,38.3),(1.5,2.6,1.0))                            # arched nose line
    ellipsoid(bm,(0,-24.2,34.7),(1.65,1.6,1.8))                           # muzzle
    for s in S2():
        cone(ex,(s*1.25,-17.1,40.4),(s*1.55,-16.5,43.4),(0.85,0.6),0.0,4)  # small ears (kept as exact geometry)
    tube(bm,[(0,17.0,31.0),(0,18.5,27.5),(0,19.0,25.0)],[1.8,1.5,1.3])    # short tail dock
    ellipsoid(bm,(0,19.2,23.6),(1.4,1.5,2.9))                             # hanging tuft
    for s in S2():
        tube(bm,[(s*4.6,-9.8,22.0),(s*3.6,-9.1,11.3),(s*3.3,-9.2,3.6),(s*3.3,-10.6,0.9)],[3.9,2.3,1.55,1.35])
        ellipsoid(bm,(s*3.3,-11.0,0.8),(1.45,1.7,0.85),10,6)
        for t in (-1,1): ellipsoid(bm,(s*3.3+t*1.15,-10.4,0.8),(0.55,0.7,0.55),8,5)
        tube(bm,[(s*4.9,12.6,24.5),(s*5.0,12.8,18.0),(s*4.3,16.6,13.8),(s*4.4,14.3,0.9)],[5.2,3.6,1.9,1.4])
        ellipsoid(bm,(s*4.4,13.8,0.8),(1.45,1.7,0.85),10,6)
        for t in (-1,1): ellipsoid(bm,(s*4.4+t*1.15,14.5,0.8),(0.55,0.7,0.55),8,5)
_HF={'L':[('sholderleft',(4.2,-10.3,20.6),(2.6,-9.1,11.3)),('elbowleft',(2.6,-9.1,11.3),(3.2,-9.2,3.6)),('wristleft',(3.2,-9.2,3.6),(3.2,-11.5,0.0))],
     'R':[('shoulderright',(-4.3,-10.3,20.6),(-2.3,-9.1,11.3)),('elbowright',(-2.3,-9.1,11.3),(-2.8,-9.2,3.6)),('wristright',(-2.8,-9.2,3.6),(-2.8,-11.5,0.0))]}
_HH={'L':[('hipleft',(4.2,12.9,25.7),(4.7,12.8,18.6)),('kneeleft',(4.7,12.8,18.6),(4.0,17.2,14.5)),('heelleft',(4.0,17.2,14.5),(4.4,14.2,0.0))],
     'R':[('hipright',(-4.3,12.9,25.7),(-4.7,12.8,18.6)),('kneeright',(-4.7,12.8,18.6),(-3.9,17.2,14.5)),('heelright',(-3.9,17.2,14.5),(-4.3,14.2,0.0))]}
_hpick=_side_chains(_HF,_HH)
def meso2_override(p):
    if p.y>16.5 and p.z>19.0 and abs(p.x)<2.6: return 'tail1' if p.z>27.0 else 'tail2'
    if p.y<-16.0 and p.z>30.0: return 'head con'
    if p.z<14.5 or (p.z<22.5 and abs(p.x)>5.2 and (abs(p.y+9.5)<4.5 or abs(p.y-13.5)<5.5)):
        return _hpick(p)
    return None
_MANE_C=Vector((0,-13.0,37.4)); _MANE_R=Matrix.Rotation(math.radians(50),3,'X')
def meso2_faces(c,n):
    if c.z<1.8: return 'hoof'
    if c.y<-23.0 and c.z<37.0: return 'muzzle'
    if -16.8<c.y<-9.0 and abs(c.x)<1.5 and n.z>0.1 and c.z>33.6+(-9.5-c.y)*1.0-0.6: return 'mane'
    if c.y>18.0 and c.z<26.5: return 'mane'   # dark tail tuft
    return 'skin'
_eye2=[(2.35,-19.0,39.3,0.62)]
MESO2=dict(MESO)
MESO2.update(parts=meso2_parts, voxel=0.3, smooth=4, target=270, override=meso2_override, region=lambda p:'body',
    faces=meso2_faces, preview='preview_v2', game_scale=(0.55,0.9),
    flats={'hoof':((0.15,0.12,0.10),0.3),'muzzle':((0.22,0.17,0.13),0.3),'mane':((0.17,0.12,0.09),0.35)},
    coats=[
      dict(colA=(0.62,0.47,0.32),colB=(0.67,0.53,0.38),dark=(0.36,0.26,0.17),belly=(0.80,0.71,0.57),stripe=(0.55,0.35),dapple=(0.30,0.3),dorsal=(1.3,0.6),pattern='fur',pscale=2.5,pstrength=0.18,eyes=_eye2),
      dict(colA=(0.52,0.36,0.24),colB=(0.57,0.41,0.28),dark=(0.28,0.19,0.12),belly=(0.74,0.63,0.49),stripe=(0.55,0.45),dapple=(0.30,0.3),dorsal=(1.3,0.6),pattern='fur',pscale=2.5,pstrength=0.18,eyes=_eye2),
      dict(colA=(0.70,0.62,0.47),colB=(0.66,0.59,0.47),dark=(0.40,0.33,0.24),belly=(0.84,0.79,0.67),stripe=(0.55,0.35),dapple=(0.30,0.3),dorsal=(1.3,0.7),pattern='fur',pscale=2.5,pstrength=0.18,eyes=_eye2),
    ])
ANIMALS['mesohippus2']=MESO2
# ---------------- Leptoceratops v2: clear ceratopsian silhouette
_FC=Vector((0,-11.5,21.3)); _FRAD=(5.7,1.35,4.5); _FROT=Matrix.Rotation(math.radians(-50),3,'X'); _FINV=_FROT.inverted()
_ARC=[(4.3*math.cos(t), -11.0+0.9*math.sin(t)*0+(-0.6)*(1-math.sin(t)), 21.8+4.6*math.sin(t)) for t in [math.radians(a) for a in (0,25,50,70,90,110,130,155,180)]]
def lept2_parts(bm,ex):
    def body_def(p):
        q=p.copy(); q.z+=2.2*max(0.0,min(1.0,(p.y+6)/14.0))      # hips clearly higher than shoulders
        return q
    ellipsoid(bm,(0,1.5,13.8),(5.6,10.5,6.3),deform=body_def)
    ellipsoid(bm,(0,9.0,17.6),(5.8,6.6,6.6))                         # heavy hindquarters (top ~24)
    ellipsoid(bm,(0,-7.8,13.6),(4.6,4.6,5.0))                        # chest
    tube(bm,[(0,12.5,18.6),(0,19.5,16.0),(0,26.0,11.8),(0,31.0,8.6),(0,33.5,7.4)],[(4.4,2.7),(3.4,2.0),(2.4,1.3),(1.2,0.7),(0.4,0.3)],joints=False)   # thick deep tail (height,width)
    tube(bm,[(0,-8.0,15.4),(0,-10.5,17.0),(0,-12.4,18.2)],[(4.4,3.5),(4.1,3.3),(3.8,3.1)],joints=False)  # short neck, head carried low
    def sk(p):
        q=p.copy()
        if q.z>0: q.z*=1.0-0.28*max(0.0,-p.y/3.8)   # skull roof slopes down toward the beak
        return q
    ellipsoid(bm,(0,-15.0,19.9),(2.9,4.2,4.2),deform=sk)                       # deep, narrow skull
    tube(bm,[(0,-16.8,19.6),(0,-19.0,18.8),(0,-20.8,18.2)],[(3.6,2.3),(3.1,1.8),(2.6,1.4)],joints=False)   # short, deep narrow snout
    ellipsoid(bm,(0,-17.2,16.4),(2.0,3.6,1.4))                       # lower jaw
    for s in S2(): ellipsoid(bm,(s*2.6,-16.2,17.4),(1.2,1.4,1.3),10,6) # jugal flare
    cone(ex,(0,-20.0,19.0),(0,-23.3,18.0),(2.5,1.75),1.3,6)      # upper beak (explicit, not remeshed) ...
    cone(ex,(0,-23.3,18.0),(0,-24.6,14.4),1.3,0.0,6)            # ... with a sharp downward hook
    cone(ex,(0,-20.4,16.6),(0,-22.9,15.7),(1.2,1.1),0.0,6)             # lower beak
    frill_plate(ex)                                                    # frill: explicit continuous shield (not remeshed)
    for s in S2():
        tube(bm,[(s*3.9,-9.8,12.0),(s*4.1,-9.4,5.8),(s*4.0,-10.0,0.6)],[2.5,1.7,1.35])
        ellipsoid(bm,(s*4.0,-10.6,0.5),(1.35,1.8,0.6),10,6)
        tube(bm,[(s*4.6,9.0,16.5),(s*4.8,11.5,6.4),(s*4.7,10.3,0.6)],[4.4,2.5,1.7])
        ellipsoid(bm,(s*4.7,9.3,0.5),(1.6,2.4,0.65),10,6)
_SF={'L':[('shoulder L',(3.2,-10.1,12.9),(3.5,-9.4,5.8)),('knee LF',(3.5,-9.4,5.8),(3.8,-9.7,-0.5))],
     'R':[('shoulder R',(-3.2,-10.1,12.9),(-3.5,-9.4,5.8)),('knee RF',(-3.5,-9.4,5.8),(-3.7,-9.7,-0.5))]}
_SH={'L':[('shoulder 1',(3.7,9.0,11.2),(4.1,11.5,6.4)),('knee LB',(4.1,11.5,6.4),(4.5,10.4,-0.5))],
     'R':[('shoulder 0',(-3.6,9.0,11.2),(-4.2,11.5,6.4)),('knee RB',(-4.2,11.5,6.4),(-4.6,10.4,-0.5))]}
_spick=_side_chains(_SF,_SH)
def lept2_override(p):
    if p.y>13.0 and p.z>5.5 and abs(p.x)<3.4: return 'base'          # tail rides the body
    if frill2_mask(p) or (p.y<-12.4 and p.z>13.0): return 'head'      # whole head incl. frill & beak
    if p.z<8.6 or (p.z<15.0 and abs(p.x)>5.0 and (abs(p.y+9.6)<3.8 or abs(p.y-10.0)<5.0)): return _spick(p)
    return None
# ---- explicit frill shield (hood): inner edge runs over the skull roof and down behind the cheeks to the jaw;
#      outer edge flares up/back over the neck -> profile rises continuously beak -> skull -> frill crest
_FZC=18.6; _FRI=(3.1,4.6); _FRO=(6.2,8.6)
def _fr_y(t,s_):
    up=max(0.0,math.cos(t))
    yi=-12.6-2.2*up                 # inner edge: on the skull roof at the top, behind the cheek at the sides
    yo=-9.6+3.2*math.sqrt(up)       # outer edge: whole rim flares back (no notch behind it), crest highest
    return yi+(yo-yi)*s_
def _fr_pt(t,s_,back):
    rx=_FRI[0]+(_FRO[0]-_FRI[0])*s_; rz=_FRI[1]+(_FRO[1]-_FRI[1])*s_
    zb=0.0
    return Vector((rx*math.sin(t), _fr_y(t,s_)+0.6*back, _FZC+rz*math.cos(t)+zb+0.5*back*0))
_FTS=[math.radians(a) for a in (-104,-74,-44,-15,15,44,74,104)]
_FSS=(0.0,0.6,1.0)
_FPLATE=[]
for _t in [math.radians(a) for a in range(-108,109,4)]:
    for _s in [i/10 for i in range(0,11)]:
        for _b in (0,1): _FPLATE.append((_fr_pt(_t,_s,_b),_s))
def _fp_tree(scale=1.0):
    from mathutils import kdtree
    piv=Vector((0,-12.4,20.4)); kd=kdtree.KDTree(len(_FPLATE))
    for i,(p,_) in enumerate(_FPLATE): kd.insert(piv+(p-piv)*scale,i)
    kd.balance(); return kd
_FKD={}
def _fp_near(co):
    best=(1e9,0.0)
    for sc in (1.0,1.2,1.08):
        if sc not in _FKD: _FKD[sc]=_fp_tree(sc)
        p,i,d=_FKD[sc].find(Vector(co))
        if d<best[0]: best=(d,_FPLATE[i][1])
    return best
def frill_plate(bm):
    rows=[]   # front rows for each s, then back rows reversed -> closed loop of rows
    for s_ in _FSS: rows.append([bm.verts.new(_fr_pt(t,s_,0)) for t in _FTS])
    for s_ in _FSS[::-1]: rows.append([bm.verts.new(_fr_pt(t,s_,1)) for t in _FTS])
    n=len(_FTS); R=len(rows)
    for k in range(R):
        a,bb=rows[k],rows[(k+1)%R]
        for i in range(n-1): bm.faces.new([a[i],a[i+1],bb[i+1],bb[i]])
    for i in (0,n-1):
        f=[r[i] for r in rows]; bm.faces.new(f if i else f[::-1])
    bmesh.ops.recalc_face_normals(bm,faces=bm.faces[:])
def _frill_s(co): return _fp_near(co)[1]
def _frill_q(co):
    q=_FINV@(Vector(co)-_FC); return Vector((q.x/_FRAD[0],q.y/_FRAD[1],q.z/_FRAD[2]))
def frill2_mask(co):
    return _fp_near(co)[0]<0.75
def lept2_faces(c,n):
    if c.y<-20.9 and c.z<21.0: return 'beak'
    if frill2_mask(c):
        return 'frilledge' if _frill_s(c)>0.66 else 'frill'
    return 'skin'
def frill2_scale(f):
    piv=Vector((0,-12.4,20.4))
    def tw(co):
        if frill2_mask(co): return piv+(co-piv)*f
        return co
    return tw
LEPT2=dict(LEPT)
LEPT2.update(parts=lept2_parts, voxel=0.2, smooth=3, target=290, override=lept2_override, region=lambda p:'body',
    faces=lept2_faces, preview='preview_v2',
    flats={'beak':((0.10,0.085,0.07),0.25),'frill':((0.66,0.42,0.19),0.25),'frilledge':((0.93,0.84,0.62),0.15)},
    coats=[dict(colA=(0.47,0.45,0.26),colB=(0.62,0.49,0.24),dark=(0.24,0.24,0.13),belly=(0.74,0.67,0.48),mscale=0.25,pattern='scales',pscale=1.4,pstrength=0.45,stripe=(0.35,0.25),dorsal=(1.8,0.85),eyes=[(2.35,-15.4,21.1,0.62)])],
    tweaks={'frill':frill2_scale(1.2),'juv':head_scale(1.08)})
ANIMALS['leptoceratops2']=LEPT2

