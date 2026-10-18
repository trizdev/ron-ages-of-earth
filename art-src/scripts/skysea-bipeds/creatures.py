import math
import numpy as np
from mathutils import Vector
from skylib import *
CREATURES={}

# =============== pterosaurs on the RoN bird skeleton (Root / Bone Head / Bone Tail / Wing06-08 left(-x) / Wing1,02,03 right(+x))
def wbone(p):
    ax=abs(p.x); L=p.x<0
    if ax<1.6: return 'Root'
    inner,mid,tip=('Bone Wing06','Bone Wing07','Bone Wing08') if L else ('Bone Wing1','Bone Wing02','Bone Wing03')
    if ax<11.0: return inner
    if ax<19.5: return mid
    return tip
WBOX=((0.8,21.0),(-3.0,7.0))
def wing_pair(mb,Lp,Lz,Tp,Tz,H,Hz,cls='wing'):
    for s in (1,-1):
        pts=[Vector((s*x,y,z)) for (x,y),z in zip(Lp,Lz)]+[Vector((s*x,y,z)) for (x,y),z in zip(Tp,Tz)]+[Vector((s*H[0],H[1],Hz))]
        bones=[wbone(p) for p in pts]; bones[8]='Root'      # ankle: membrane attaches to the hind foot
        faces=[(0,1,7,8),(0,8,9),(1,2,6,7),(2,3,5,6),(3,4,5)]
        planar(mb,pts,bones,cls,faces,(0,1),WBOX,two=True)
def claws(mb,wr,z):
    for s in (1,-1):
        x,y=wr; pts=[Vector((s*(x-0.9),y+0.15,z+0.05)),Vector((s*(x-1.6),y-1.1,z+0.1)),Vector((s*(x+0.2),y+0.1,z+0.05))]
        planar(mb,pts,[wbone(p) for p in pts],'dark',[(0,1,2)],(0,1),((0,3),(2,8)),two=True)
def legs(mb,pts2,z0=0.25,z1=0.12):
    for s in (1,-1):
        (a,b),(c,d),(e,f),(g,h)=pts2
        pts=[Vector((s*a,b,z0)),Vector((s*c,d,z0)),Vector((s*e,f,z1)),Vector((s*g,h,z1))]
        planar(mb,pts,['Root']*4,'dark',[(0,1,2,3)],(0,1),((0,3),(2,8)),two=True)
BIRD_RECTS={'wing':(0,0.5,1,1),'body':(0,0,0.5,0.5),'head':(0.5,0.25,1,0.5),'dark':(0.5,0,0.75,0.25),'crest':(0.75,0,1,0.25)}

# ---- Anurognathid (WILDBIRD): broad short frog-like head with huge eyes, stub tail, broad membrane wings tied to the ankles
AL=[(0.8,-1.3),(5.5,-2.1),(11.0,-2.6),(16.0,-1.5),(20.8,1.2)]; ALz=[0.75,0.95,1.05,0.85,0.55]
AT=[(17.6,2.0),(13.0,2.5),(8.2,4.7),(2.9,6.4)]; ATz=[0.5,0.55,0.5,0.15]; AH=(0.7,3.4)
ANU_HEAD=[(-1.4,0.8,0.55,0.55),(-2.5,1.55,0.5,0.72),(-3.5,1.45,0.4,0.55)]
def anuro(mb):
    loft(mb,[(-1.9,0.7,0.45,0.55),(-0.6,1.2,0.4,0.8),(2.0,1.05,0.35,0.7),(4.2,0.5,0.3,0.38)],lambda p:'Bone Tail' if p.y>5.0 else 'Root','body',6,cap0=(0,-2.3,0.5),cap1=(0,5.4,0.3))
    loft(mb,ANU_HEAD,lambda p:'Bone Head','head',6,cap0=(0,-4.25,0.35))
    wing_pair(mb,AL,ALz,AT,ATz,AH,0.45)
    legs(mb,[(0.5,3.0),(0.95,3.2),(3.3,7.2),(2.9,7.35)],z0=0.32,z1=0.2)
    claws(mb,AL[2],ALz[2])
def wing_painter(Lp,Tp,H,membrane,arm,trail,fib=0.07,inner_light=0.12,armw=1.0,box=None):
    box=box or WBOX
    lx=np.array([p[0] for p in Lp]); ly=np.array([p[1] for p in Lp])
    tpts=[H]+Tp[::-1]; tx=np.array([p[0] for p in tpts]); ty=np.array([p[1] for p in tpts])
    def f(s,t,sh):
        x=box[0][0]+(box[0][1]-box[0][0])*s; y=box[1][0]+(box[1][1]-box[1][0])*t
        yle=np.interp(x,lx,ly); yte=np.interp(x,tx,ty,right=Lp[-1][1])
        span=np.maximum(yte-yle,0.3); u=(y-yle)/span
        n=vnoise(sh[0],sh[1],10,3); n2=vnoise(sh[0],sh[1],24,4)
        col=C(membrane,sh)*(0.92+0.14*n[...,None])
        col=lerp(col,C(trail,sh),smooth(0.72,1.0,u))                       # darker trailing edge
        col=col*(1+inner_light*(1-np.clip(x/(box[0][1]*0.6),0,1)))[...,None]            # lighter, thicker near the body
        ang=np.arctan2(y-ly[2],x-lx[2]); fibres=0.5+0.5*np.sin(ang*55+n2*2)
        col=col*(1-fib*fibres)[...,None]                                     # actinofibrils fanning from the wrist
        col=lerp(col,C(arm,sh)*(0.9+0.2*n2[...,None]),smooth(armw,armw-0.2,(y-yle)))  # arm + wing finger along the leading edge
        return col
    return f
def countershade(back,belly,noise=0.18,cells=12,seed=5,e0=0.38,e1=0.78):
    def f(s,t,sh):
        n=vnoise(sh[0],sh[1],cells,seed); col=lerp(C(back,sh),C(belly,sh),smooth(e0,e1,s))
        return col*(1-noise/2+noise*n[...,None])
    return f
def head_painter(back,belly,eye_s,eye_t,eye_r,eye_col=(0.04,0.03,0.02),ring=None,mouth=None,tip=None):
    base=countershade(back,belly,e0=0.42,e1=0.72)
    def f(s,t,sh):
        col=base(s,t,sh)
        if mouth is not None: col=lerp(col,C(mouth[1],sh),smooth(0.05,0.0,np.abs(s-mouth[0]))*0.8)
        if tip is not None: col=lerp(col,C(tip[1],sh),smooth(tip[0]+0.04,tip[0],t))
        d=np.hypot((s-eye_s)/eye_r[0],(t-eye_t)/eye_r[1])
        if ring is not None: col=lerp(col,C(ring,sh),smooth(1.45,1.15,d))
        col=lerp(col,C(eye_col,sh),smooth(1.0,0.75,d))
        col=lerp(col,C((0.9,0.9,0.85),sh),smooth(0.32,0.15,np.hypot((s-eye_s+0.25*eye_r[0])/eye_r[0],(t-eye_t-0.3*eye_r[1])/eye_r[1])))
        return col
    return f
def flat(c,noise=0.15,cells=6):
    def f(s,t,sh): return C(c,sh)*(1-noise/2+noise*vnoise(sh[0],sh[1],cells,9)[...,None])
    return f
def anuro_coat(back,belly,membrane,arm):
    trail=tuple(x*0.72 for x in membrane)
    return {'wing':wing_painter(AL,AT,AH,membrane,arm,trail),'body':countershade(back,belly,noise=0.25,cells=16),
            'head':head_painter(back,belly,0.36,0.47,(0.14,0.2),ring=tuple(min(1,x*1.25) for x in belly)),
            'dark':flat(arm),'crest':flat(arm)}
CREATURES['pterowing']=dict(folder='pterowing',anim=('bird_dirty','bird_flap'),texsize=64,rects=BIRD_RECTS,
    models={'anuro':anuro},
    coats={'bird_dirty.tga':('anuro',anuro_coat((0.34,0.24,0.15),(0.63,0.51,0.37),(0.58,0.40,0.27),(0.17,0.11,0.07))),
           'bird_snow.tga':('anuro',anuro_coat((0.62,0.63,0.66),(0.90,0.90,0.90),(0.64,0.65,0.69),(0.30,0.31,0.34))),
           'bird_african.tga':('anuro',anuro_coat((0.64,0.50,0.30),(0.87,0.77,0.57),(0.74,0.58,0.37),(0.40,0.28,0.16))),
           'bird_amer.tga':('anuro',anuro_coat((0.22,0.32,0.15),(0.62,0.66,0.40),(0.32,0.45,0.21),(0.13,0.19,0.09)))},
    exports={'bird_dirty':('anuro','bird_dirty'),'bird_snow':('anuro','bird_snow'),'bird_african':('anuro','bird_african')},
    orig_tex='bird_dirty.tga',preview_model=('anuro','bird_dirty.tga'),pose_frame=None,
    variants=[('anuro','bird_dirty.tga','brown (dirty)'),('anuro','bird_snow.tga','light grey (snowy/arctic)'),('anuro','bird_african.tga','sand (savannah/GS)'),('anuro','bird_amer.tga','green (jungle)')])

# ---- Anhanguera (GULLBIRD): long narrow jaws with rounded crests at the tips, long narrow wings, short tail
GL=[(0.7,-1.0),(5.5,-1.9),(10.8,-2.6),(15.8,-1.6),(20.8,1.9)]; GLz=[0.8,1.0,1.1,0.85,0.5]
GT=[(17.6,2.6),(13.5,1.6),(8.0,2.9),(2.2,4.6)]; GTz=[0.5,0.55,0.5,0.2]; GH=(0.6,3.2)
CRBOX=((-10.6,-6.0),(-1.5,2.9))
def anhang(mb):
    loft(mb,[(-1.9,0.6,0.5,0.5),(-0.5,1.0,0.45,0.72),(2.0,0.85,0.4,0.6),(4.0,0.4,0.35,0.32)],lambda p:'Bone Tail' if p.y>5.0 else 'Root','body',6,cap0=(0,-2.2,0.55),cap1=(0,5.6,0.35))
    loft(mb,[(-1.5,0.55,0.75,0.5),(-3.2,0.62,0.82,0.74),(-6.0,0.33,0.6,0.45),(-9.0,0.17,0.5,0.28)],lambda p:'Bone Head','head',6,cap0=(0,-10.8,0.47))
    up=[Vector(p) for p in [(0,-6.4,1.0),(0,-8.3,2.7),(0,-9.7,2.0),(0,-10.4,0.72),(0,-9.2,0.72)]]
    lo=[Vector(p) for p in [(0,-6.2,0.18),(0,-7.9,-1.3),(0,-9.3,-0.8),(0,-10.1,0.25),(0,-9.0,0.25)]]
    for pts in (up,lo): planar(mb,pts,['Bone Head']*5,'crest',[(0,1,4),(1,2,4),(2,3,4)],(1,2),CRBOX,two=True)
    wing_pair(mb,GL,GLz,GT,GTz,GH,0.5)
    legs(mb,[(0.5,3.0),(0.8,3.3),(2.1,4.9),(1.85,5.0)])
    claws(mb,GL[2],GLz[2])
def crest_painter(c,rim):
    def f(s,t,sh):
        y=CRBOX[0][0]+(CRBOX[0][1]-CRBOX[0][0])*s; z=CRBOX[1][0]+(CRBOX[1][1]-CRBOX[1][0])*t
        n=vnoise(sh[0],sh[1],8,2); col=C(c,sh)*(0.9+0.2*n[...,None])
        e=np.abs(z-0.55); col=lerp(col,C(rim,sh),smooth(0.9,1.5,e))   # darker crest edge
        return col
    return f
GULL_COAT={'wing':wing_painter(GL,GT,GH,(0.50,0.47,0.45),(0.12,0.11,0.11),(0.30,0.28,0.27),fib=0.06,inner_light=0.25,armw=0.8),
    'body':countershade((0.80,0.80,0.78),(0.96,0.95,0.92),noise=0.12),
    'head':head_painter((0.86,0.85,0.82),(0.95,0.94,0.90),0.38,0.80,(0.09,0.06),mouth=(0.62,(0.35,0.30,0.28)),tip=(0.14,(0.30,0.24,0.20))),
    'dark':flat((0.55,0.45,0.35)),'crest':crest_painter((0.86,0.36,0.14),(0.40,0.12,0.06))}
CREATURES['anhanguera']=dict(folder='anhanguera',anim=('bird_gul','bird_flap'),texsize=64,rects=BIRD_RECTS,
    models={'anhang':anhang},coats={'bird_gul.tga':('anhang',GULL_COAT)},
    exports={'bird_gul':('anhang','bird_gul')},orig_tex='bird_gul.tga',preview_model=('anhang','bird_gul.tga'),pose_frame=None)

# =============== Eudimorphodon flock (FLOCKBIRD): 4 identical birds, one bone per wing
FLOCK=[('bird',0.0,'wing','wing02'),('bird01',17.75,'wing06','wing04'),('bird02',-16.03,'wing10','wing08'),('bird03',34.84,'wing14','wing12')]
EL=[(0.35,-0.5),(2.6,-1.25),(6.2,0.7)]; ELz=[0.3,0.45,0.3]
ET=[(4.0,1.0),(1.5,1.6)]; ETz=[0.25,0.25]; EH=(0.35,1.2)
EBOX=((0.3,6.3),(-1.4,2.0)); VBOX=((0,0.8),(5.2,7.2))
def eudi(mb):
    for body,x0,wp,wn in FLOCK:
        bf=lambda p,b=body:b
        loft(mb,[(-0.8,0.35,0.2,0.33,x0),(1.0,0.5,0.2,0.42,x0)],bf,'body',4,cap0=(x0,-2.9,0.25),cap1=(x0,5.6,0.12))
        vp=[Vector((x0,5.2,0.12)),Vector((x0+0.75,6.1,0.12)),Vector((x0,7.2,0.12)),Vector((x0-0.75,6.1,0.12))]
        ids=[mb.v(p,body,(abs(p.x-x0)/0.8,(p.y-5.2)/2.0)) for p in vp]; mb.f(ids,'vane',two=True)
        for s,wb in ((1,wp),(-1,wn)):
            pts=[Vector((x0+s*x,y,z)) for (x,y),z in zip(EL,ELz)]+[Vector((x0+s*x,y,z)) for (x,y),z in zip(ET,ETz)]+[Vector((x0+s*EH[0],EH[1],0.25))]
            bones=[body,wb,wb,wb,wb,body]
            ids=[mb.v(p,b,((abs(p.x-x0)-EBOX[0][0])/(EBOX[0][1]-EBOX[0][0]),(p.y-EBOX[1][0])/(EBOX[1][1]-EBOX[1][0]))) for p,b in zip(pts,bones)]
            for f in [(0,1,4,5),(1,3,4),(1,2,3)]: mb.f([ids[i] for i in f],'wing',two=True)
FLOCK_RECTS={'wing':(0,0.5,1,1),'body':(0,0,0.5,0.5),'vane':(0.5,0,0.75,0.25),'spare':(0.5,0.25,1,0.5),'spare2':(0.75,0,1,0.25)}
def eudi_body(back,belly):
    base=countershade(back,belly,noise=0.2)
    def f(s,t,sh):
        col=base(s,t,sh)
        d=np.hypot((s-0.38)/0.13,(t-0.17)/0.05); col=lerp(col,C((0.03,0.03,0.03),sh),smooth(1.0,0.7,d))
        return col
    return f
def eudi_coat(back,belly,membrane,arm,vane):
    return {'wing':wing_painter(EL,ET,EH,membrane,arm,tuple(x*0.75 for x in membrane),fib=0.05,armw=0.45,box=EBOX),
            'body':eudi_body(back,belly),'vane':flat(vane,0.1),'spare':flat(back),'spare2':flat(back)}
CREATURES['ptero_flock']=dict(folder='ptero_flock',anim=('flock','flock_move1'),texsize=64,rects=FLOCK_RECTS,models={'eudi':eudi},
    coats={'flock.tga':('eudi',eudi_coat((0.27,0.23,0.21),(0.66,0.60,0.50),(0.56,0.41,0.30),(0.13,0.10,0.09),(0.78,0.22,0.10))),
           'flock_african.tga':('eudi',eudi_coat((0.58,0.44,0.27),(0.86,0.77,0.58),(0.76,0.58,0.38),(0.33,0.23,0.13),(0.85,0.50,0.12)))},
    exports={'flock':('eudi','flock')},orig_tex='flock.tga',preview_model=('eudi','flock.tga'),pose_frame=None,gap=0.12,
    variants=[('eudi','flock.tga','normal (also snow)'),('eudi','flock_african.tga','savannah')])

# =============== HERDFISH: 5 fish per model; each fish = (body bone, tail bone, x centre, y head, y tail end, z centre, tail pivot y)
FISH=[('ammo node 0','tail04',-9.64,-11.23,18.68,9.3,2.08),('ammo node 1','tail03',-4.95,-6.61,11.64,9.5,1.72),
      ('ammo node 2','tail01',4.18,-8.12,13.94,9.4,1.82),('ammo node 3','tail',0.0,-6.61,11.64,9.5,0.92),('head02','tail02',8.40,-4.08,7.77,9.6,1.30)]
def vst(mb,p,b,st): return mb.v(p,b,st)
def lepto(mb):
    for bb,tb,xc,ya,yb,zc,piv in FISH:
        L=yb-ya; bf=lambda p,bb=bb,tb=tb,piv=piv: tb if p.y>piv+0.02*L else bb
        loft(mb,[(ya+0.13*L,0.034*L,zc,0.07*L,xc),(ya+0.34*L,0.05*L,zc+0.004*L,0.1*L,xc),(ya+0.62*L,0.014*L,zc,0.025*L,xc)],bf,'body',4,
             cap0=(xc,ya,zc-0.005*L),cap1=(xc,ya+0.66*L,zc),y0=ya,y1=ya+0.66*L)
        y0=ya+0.6*L; pts=[(y0,zc+0.02*L),(yb,zc+0.14*L),(yb-0.11*L,zc),(yb,zc-0.13*L),(y0,zc-0.02*L)]
        ids=[mb.v(Vector((xc,y,z)),tb,((y-y0)/(yb-y0),(z-zc)/(0.3*L)+0.5)) for y,z in pts]
        for f in [(0,1,2),(0,2,4),(4,2,3)]: mb.f([ids[i] for i in f],'fin',two=True)
        # small dorsal fin
        d=[(ya+0.36*L,zc+0.1*L),(ya+0.47*L,zc+0.16*L),(ya+0.5*L,zc+0.07*L)]
        ids=[mb.v(Vector((xc,y,z)),bb,(0.2+0.5*(y-ya-0.36*L)/(0.14*L),0.5+(z-zc)/(0.3*L))) for y,z in d]; mb.f(ids,'fin',two=True)
def belem(mb):
    for bb,tb,xc,ya,yb,zc,piv in FISH:
        L=yb-ya; bf=lambda p,bb=bb: bb
        loft(mb,[(ya+0.40*L,0.07*L,zc,0.07*L,xc),(ya+0.62*L,0.055*L,zc,0.055*L,xc),(ya+0.70*L,0.045*L,zc,0.04*L,xc)],bf,'body',4,
             cap0=(xc,ya,zc),cap1=(xc,ya+0.75*L,zc),y0=ya,y1=ya+0.75*L)
        for s in (1,-1):   # lateral fins near the pointed end
            pts=[Vector((xc+s*0.035*L,ya+0.12*L,zc)),Vector((xc+s*0.13*L,ya+0.26*L,zc)),Vector((xc+s*0.06*L,ya+0.36*L,zc))]
            ids=[mb.v(p,bb,(abs(p.x-xc)/(0.14*L),(p.y-ya)/(0.4*L))) for p in pts]; mb.f(ids,'fins',two=True)
        for ax,az in ((0.03,0.025),(-0.03,0.025),(0.03,-0.025),(-0.03,-0.025)):   # 4 trailing arm bundles (tail bone = wiggle)
            pts=[Vector((xc+ax*L,ya+0.72*L,zc+az*L)),Vector((xc+ax*L*0.3,ya+0.72*L,zc+az*L*0.3)),Vector((xc+ax*L*2.0,yb,zc+az*L*2.0))]
            ids=[mb.v(p,tb,(0.5+(p.x-xc)/(0.15*L),(p.y-ya-0.7*L)/(0.3*L))) for p in pts]; mb.f(ids,'arms',two=True)
def coil(mb):
    roll=math.radians(40)
    for bb,tb,xc,ya,yb,zc,piv in FISH:
        L=yb-ya; R=0.27*L; cy=ya+R*1.05; cz=zc; n=10; th=0.30*R
        def P(lx,ly,lz):   # shell-local (x=side, y, z) rolled about the y axis so the coil faces up/sideways
            return Vector((xc+lx*math.cos(roll)-lz*math.sin(roll),cy+ly,cz+lx*math.sin(roll)+lz*math.cos(roll)))
        rim=[mb.v(P(0,R*math.cos(2*math.pi*k/n),R*math.sin(2*math.pi*k/n)),bb,(0.5+0.5*math.cos(2*math.pi*k/n),0.5+0.5*math.sin(2*math.pi*k/n))) for k in range(n)]
        for s in (1,-1):
            c=mb.v(P(s*th,0,0),bb,(0.5,0.5))
            for k in range(n):
                f=[rim[k],rim[(k+1)%n],c]; mb.f(f if s>0 else f[::-1],'shell')
        # trailing tentacles from the aperture (lower rear of the body whorl), tail bone = wiggle
        for dz,dx in ((0.05,0.0),(-0.04,0.04),(-0.04,-0.04)):
            a=P(0.05*L,0.62*R,-0.45*R); b=P(-0.05*L,0.62*R,-0.5*R); tip=P(dx*L,yb-0.18*L-cy,-0.45*R+dz*L)
            ids=[mb.v(p,tb,(0.5+(p.x-xc)/(0.25*L),(p.y-cy-0.62*R)/(yb-cy))) for p in (a,b,tip)]; mb.f(ids,'tent',two=True)
FISH_RECTS={'lepto':{'body':(0,0,1,0.6),'fin':(0,0.6,0.5,1),'spare':(0.5,0.6,1,1)},
            'belem':{'body':(0,0,1,0.6),'arms':(0,0.6,0.5,1),'fins':(0.5,0.6,1,1)},
            'coil':{'shell':(0,0,0.75,0.75),'tent':(0.75,0,1,0.75),'spare':(0,0.75,1,1)}}
def lepto_body(s,t,sh):
    n=vnoise(sh[0],sh[1],14,11)
    col=lerp(C((0.16,0.27,0.30),sh),C((0.74,0.78,0.80),sh),smooth(0.22,0.42,s))
    col=lerp(col,C((0.93,0.93,0.90),sh),smooth(0.6,0.8,s))
    col=lerp(col,C((0.30,0.36,0.38),sh),smooth(0.04,0.0,np.abs(s-0.45))*smooth(0.2,0.3,t)*0.7)   # lateral line
    col=col*(0.93+0.12*n[...,None])
    d=np.hypot((s-0.36)/0.1,(t-0.12)/0.045); col=lerp(col,C((0.85,0.85,0.8),sh),smooth(1.5,1.2,d)); col=lerp(col,C((0.03,0.03,0.04),sh),smooth(1.0,0.75,d))
    return col
def lepto_fin(s,t,sh):
    col=C((0.52,0.58,0.60),sh); return lerp(col,C((0.25,0.30,0.33),sh),smooth(0.6,1.0,s))
def belem_body(s,t,sh):
    n=vnoise(sh[0],sh[1],20,12); sp=(vnoise(sh[0],sh[1],40,13)>0.62).astype(float)
    col=lerp(C((0.58,0.27,0.19),sh),C((0.86,0.62,0.50),sh),smooth(0.4,0.8,s))
    col=col*(1-0.25*sp[...,None])*(0.92+0.15*n[...,None])
    col=lerp(col,C((0.86,0.80,0.68),sh),smooth(0.16,0.06,t))          # pale guard tip
    d=np.hypot((s-0.42)/0.16,(t-0.88)/0.05); col=lerp(col,C((0.04,0.03,0.03),sh),smooth(1.0,0.7,d))
    return col
def coil_shell(s,t,sh):
    x=(s-0.5)*2; y=(t-0.5)*2; r=np.maximum(np.hypot(x,y),1e-3); a=np.arctan2(y,x)
    W=2.1; u=-np.log(r)/np.log(W)-a/(2*np.pi)
    sut=np.abs(((u+0.5)%1.0)-0.5)                     # 0 on the whorl suture
    ribs=np.abs(((a/(2*np.pi)*26+r*2.5)%1.0)-0.5)
    band=0.5+0.5*np.sin(a*3+r*4)
    col=lerp(C((0.88,0.78,0.58),sh),C((0.62,0.36,0.20),sh),smooth(0.55,0.85,band)*0.85)
    col=col*(1-0.22*smooth(0.18,0.0,ribs))[...,None]
    col=lerp(col,C((0.30,0.18,0.10),sh),smooth(0.07,0.0,sut))
    col=lerp(col,C((0.25,0.16,0.10),sh),smooth(0.16,0.08,r))
    col=col*(0.9+0.12*vnoise(sh[0],sh[1],10,14)[...,None])
    return col
CREATURES['bait_shoal']=dict(folder='bait_shoal',anim=('fish1','fish_swim1'),texsize=64,rects=FISH_RECTS,
    models={'lepto':lepto,'belem':belem,'coil':coil},
    coats={'fishherd.tga':('lepto',{'body':lepto_body,'fin':lepto_fin,'spare':flat((0.5,0.55,0.58))}),
           'fishherd_salmon.tga':('belem',{'body':belem_body,'arms':flat((0.42,0.17,0.13),0.2),'fins':flat((0.62,0.33,0.25),0.2)}),
           'fishherd_mahi.tga':('coil',{'shell':coil_shell,'tent':flat((0.62,0.42,0.36),0.2),'spare':flat((0.8,0.7,0.5))})},
    exports={'fish1':('lepto','fish1'),'fish2':('lepto','fish2'),'fish_belem':('belem','fish1'),'fish_coil':('coil','fish1')},
    orig_tex='fishherd.tga',preview_model=('lepto','fishherd.tga'),pose_frame=None,ground=(0.08,0.20,0.26),gz=-20,gap=0.2,water=True,
    strip_models=[('lepto','fishherd.tga','leptolepis'),('belem','fishherd_salmon.tga','belemnite'),('coil','fishherd_mahi.tga','ammonite')],
    variants=[('lepto','fishherd.tga','Leptolepis (fish1/fish2 + fishherd.tga)'),('belem','fishherd_salmon.tga','belemnites (fish_belem + fishherd_salmon.tga)'),('coil','fishherd_mahi.tga','ammonites (fish_coil + fishherd_mahi.tga)')])

# =============== Stenopterygius on the whale skeleton
def whb(p):
    if abs(p.x)>4.4 and p.z<-2.5 and -6<p.y<6:   # front paddles
        return ('Dummy14' if abs(p.x)<9 else 'Dummy15') if p.x>0 else ('Dummy17' if abs(p.x)<9 else 'Dummy18')
    y=p.y
    if y<=-12.4: return 'Dummy11'
    if y<10.8: return 'whaleroot01'
    if y<24.1: return 'Dummy06'
    if y<38.1: return 'Dummy07'
    if y<47.5: return 'Dummy08'
    return 'Dummy09'
STEN_RINGS=[(-21,0.75,0.8,0.75),(-15.5,2.4,1.4,2.4),(-11,3.8,1.2,4.0),(-3,5.6,0.6,6.0),(6,5.3,0.6,6.2),(14,4.2,0.8,5.0),(24,2.6,0.6,3.2),(34,1.4,0.3,1.8),(40,1.0,0.0,1.3),(44,0.7,-0.4,1.0)]
TFBOX=((40,52.5),(-11,11.5))
def steno(mb):
    loft(mb,STEN_RINGS,whb,'body',8,cap0=(0,-27.5,0.6),cap1=(0,46,-0.6))
    tf=[(40.5,1.0),(46.5,6.5),(51.8,11.0),(48.8,4.5),(47.4,0.0),(48.6,-4.5),(51.2,-10.5),(45.8,-6.0),(42.5,-1.2)]
    pts=[Vector((0,y,z)) for y,z in tf]
    planar(mb,pts,[whb(p) for p in pts],'tail',[(0,1,3),(1,2,3),(0,3,4),(0,4,8),(8,4,5),(8,5,7),(7,5,6)],(1,2),TFBOX)
    pts=[Vector(p) for p in [(0,2.5,6.5),(0,10.5,12.6),(0,13.5,12.0),(0,16.5,5.0)]]
    planar(mb,pts,[whb(p) for p in pts],'dorsal',[(0,1,2,3)],(1,2),((2,17),(4.5,13)))
    for s in (1,-1):
        pts=[Vector((s*x,y,z)) for x,y,z in [(4.8,-4.5,-3.2),(4.8,0.0,-3.6),(10.0,3.6,-5.6),(15.0,4.6,-7.2),(12.5,1.0,-6.4)]]
        planar(mb,pts,[whb(p) for p in pts],'flip',[(0,1,2,4),(4,2,3)],(0,1),((4.5,15.5),(-5,5)))
        pts=[Vector((s*x,y,z)) for x,y,z in [(2.8,21.5,-2.0),(2.6,25.0,-2.0),(7.0,27.0,-3.0)]]
        planar(mb,pts,[whb(p) for p in pts],'flip',[(0,1,2)],(0,1),((2.5,7.5),(21,27.5)))
STEN_RECTS={'body':(0,0.25,0.6,1),'tail':(0.6,0.5,1,1),'dorsal':(0.6,0.25,0.8,0.5),'flip':(0.8,0.25,1,0.5),'spare':(0,0,1,0.25)}
def steno_body(s,t,sh):
    n=vnoise(sh[0],sh[1],18,21); n2=vnoise(sh[0],sh[1],50,22)
    col=lerp(C((0.20,0.25,0.30),sh),C((0.84,0.82,0.74),sh),smooth(0.42,0.66,s))
    col=col*(0.9+0.14*n[...,None]+0.05*n2[...,None])
    col=lerp(col,C((0.12,0.14,0.17),sh),smooth(0.05,0.0,np.abs(s-0.56))*smooth(0.2,0.14,t)*0.8)   # jaw line
    d=np.hypot((s-0.36)/0.135,(t-0.19)/0.018)
    col=lerp(col,C((0.80,0.78,0.68),sh),smooth(1.55,1.25,d))     # sclerotic ring
    col=lerp(col,C((0.03,0.03,0.04),sh),smooth(1.0,0.8,d))
    return col
def steno_fin(dark,light):
    def f(s,t,sh): return lerp(C(dark,sh),C(light,sh),smooth(0.75,1.0,s)*0.5)*(0.92+0.12*vnoise(sh[0],sh[1],8,23)[...,None])
    return f
CREATURES['stenopterygius']=dict(folder='stenopterygius',anim=('whale','whale_walk3'),texsize=128,rects=STEN_RECTS,models={'steno':steno},
    coats={'whale.tga':('steno',{'body':steno_body,'tail':steno_fin((0.27,0.32,0.37),(0.45,0.50,0.55)),'dorsal':steno_fin((0.27,0.32,0.37),(0.42,0.46,0.50)),
                                 'flip':steno_fin((0.30,0.34,0.38),(0.60,0.60,0.56)),'spare':flat((0.2,0.25,0.3))})},
    exports={'whale':('steno','whale')},orig_tex='whale.tga',preview_model=('steno','whale.tga'),pose_frame=None,ground=(0.08,0.20,0.26),gz=-25,gap=0.3,water=True)
