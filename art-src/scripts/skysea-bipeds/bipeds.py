import math
import numpy as np
from mathutils import Vector
from skylib import *
from creatures import countershade, flat
CREATURES={}; BH={}
GB='/workspace/prehistoric-herds/bipeds/glb/'; SB='/workspace/prehistoric-herds/bipeds/src/'
def B(n): return BH[n].copy()
def V(*a): return Vector(a)
def R4(x0,x1,y0,y1): return (x0,y0,x1,y1)

# ---------- painters
def streaky(back,belly,cy=6,cx=40,amt=0.28,seed=3,e0=0.4,e1=0.75,stripes=None):
    def f(s,t,sh):
        n=vnoise2(sh[0],sh[1],cy,cx,seed); n2=vnoise(sh[0],sh[1],10,seed+1)
        col=lerp(C(back,sh),C(belly,sh),smooth(e0,e1,s))
        col=col*(1-amt/2+amt*n[...,None])*(0.94+0.1*n2[...,None])
        if stripes is not None:   # faint transverse bands (t direction)
            k,a=stripes; col=col*(1-a*smooth(0.55,0.9,0.5+0.5*np.sin(t*k*2*np.pi))*smooth(0.55,0.2,s))[...,None]
        return col
    return f
def eye_head(back,belly,eye_s,eye_t,er,beak=None,ring=(0.85,0.8,0.65),eyecol=(0.05,0.04,0.03),mask=None,amt=0.15):
    base=streaky(back,belly,cy=4,cx=20,amt=amt,e0=0.45,e1=0.75)
    def f(s,t,sh):
        col=base(s,t,sh)
        if mask is not None: col=lerp(col,C(mask[0],sh),smooth(mask[1]+0.06,mask[1],np.abs(s-eye_s))*smooth(eye_t+0.25,eye_t+0.15,t)*0.8)
        if beak is not None: col=lerp(col,C(beak[1],sh),smooth(beak[0]+0.04,beak[0]-0.02,t))
        d=np.hypot((s-eye_s)/er[0],(t-eye_t)/er[1])
        col=lerp(col,C(ring,sh),smooth(1.5,1.2,d)); col=lerp(col,C(eyecol,sh),smooth(1.0,0.78,d))
        col=lerp(col,C((0.92,0.92,0.88),sh),smooth(0.3,0.12,np.hypot((s-eye_s+0.3*er[0])/er[0],(t-eye_t-0.3*er[1])/er[1])))
        return col
    return f
def feather(base,tip,bars=0,bar_col=None,bar_amt=0.8,edge=None):
    """planar feather/plume: t along the feather (0 base ->1 tip), s across"""
    def f(s,t,sh):
        n=vnoise2(sh[0],sh[1],5,24,7)
        col=lerp(C(base,sh),C(tip,sh),smooth(0.55,1.0,t))*(0.9+0.18*n[...,None])
        if bars: col=lerp(col,C(bar_col,sh),smooth(0.25,0.0,np.abs(((t*bars)%1.0)-0.5)-0.15)*bar_amt*smooth(0.15,0.3,t))
        col=col*(1-0.25*smooth(0.12,0.0,np.abs(s-0.5)))[...,None]   # dark rachis
        if edge is not None: col=lerp(col,C(edge,sh),smooth(0.85,1.0,t))
        return col
    return f
def scaly(c,dark):
    def f(s,t,sh):
        n=vnoise(sh[0],sh[1],16,5); rings=0.5+0.5*np.sin(t*40)
        return lerp(C(c,sh),C(dark,sh),smooth(0.3,0.0,rings)*0.5+0.2*n)
    return f

# ================= Mei long (FARMCHICKEN): hen + rooster skeletons, shared fowls.tga (hen left half, rooster right half)
def meilong(male):
    def build(mb):
        root=B('Root'); nk=B('neck'); hd=B('Dummy04'); bk=B('Dummy05'); tl=B('tail')
        hips=[(B('Dummy09'),B('Dummy10'),B('Dummy11'),'Dummy09','Dummy10',-1),(B('Dummy17'),B('Dummy18'),B('Dummy19'),'Dummy17','Dummy18',1)]
        bz=hips[0][0].z+1.9
        loft(mb,[(-3.0,1.0,bz+0.35,1.1),(-0.8,1.5,bz,1.55),(1.9,1.0,bz+0.1,1.0)],lambda p:'Root','body',6,cap0=(0,-4.0,bz+0.55),cap1=(0,2.9,bz+0.15))
        hc=hd+V(0,-0.4,-0.9)
        nsegs=[('Root',root,nk),('neck',nk,hd),('Dummy04',hd,bk)]
        tube(mb,[V(0,-3.1,bz+0.6),V(0,(hc.y-3.1)/2-0.5,(bz+hc.z)/2+0.2),hc+V(0,0.7,-0.5)],[1.15,0.75,0.6],seg_bone(nsegs),'neck',4,ref=V(0,1,0))
        loft(mb,[(hc.y+0.9,0.65,hc.z+0.05,0.7),(hc.y-0.2,0.85,hc.z+0.1,0.85),(hc.y-1.3,0.55,hc.z-0.15,0.5)],lambda p:'Dummy04','head',5,
             cap0=(0,hc.y-2.2,hc.z-0.3),cap1=(0,hc.y+1.4,hc.z+0.1))
        for hip,ank,toe,b1,b2,s in hips:
            top=V(hip.x*1.1,hip.y-0.5,bz-0.2); knee=V(hip.x*1.2,hip.y-1.1,hip.z-0.4); heel=V(ank.x,ank.y+0.5,1.5)
            tube(mb,[top,knee,heel,ank+V(0,0,0.15)],[0.75,0.42,0.22,0.17],lambda p,b=b1:b,'leg',3,ref=V(0,-1,0))
            fw=toe-ank; fw.z=0
            pts=[ank+V(0,0,0.08),toe+V(0,0,0.05),toe+V(s*0.9,0.6,0.05),toe+V(-s*0.9,0.6,0.05),ank+V(0,0.9,0.05)]
            poly(mb,pts,[b2]*5,[(0.5,0),(0.5,1),(1,0.8),(0,0.8),(0.5,0.3)],'leg',[(0,1,2),(0,3,1),(0,4,2)])
        tsegs=[('Root',V(0,0,bz),tl),('tail',tl,V(0,14,bz))]
        tube(mb,[V(0,2.3,bz+0.15),V(0,6.5,bz+0.35),V(0,11.5,bz+0.35)],[0.62,0.33,0.13],seg_bone(tsegs),'tail',4,cap1=0.7)
        z=bz+0.35; fr=[V(0,4.2,z),V(1.0,8.3,z),V(0.75,12.4,z),V(0,13.8,z),V(-0.75,12.4,z),V(-1.0,8.3,z)]
        poly(mb,fr,[seg_bone(tsegs)(p) for p in fr],[(0.5+p.x/2.2,(p.y-4.2)/9.6) for p in fr],'frond',[(0,1,2),(0,2,3),(0,3,4),(0,4,5)])
        for s,wb in ((-1,'wing_left1'),(1,'wing_right1')):
            pts=[V(s*1.0,-2.6,bz+0.5),V(s*1.45,-1.3,bz-0.45),V(s*1.5,1.7,bz),V(s*1.3,0.2,bz+0.7)]
            poly(mb,pts,[wb]*4,[(0,0),(1,0.25),(0.6,1),(0,0.6)],'wing',[(0,1,2,3)])
        if male:   # small display crest of feathers on the head
            pts=[hc+V(0,0.1,0.75),hc+V(0,1.4,1.9),hc+V(0,1.9,0.6)]
            poly(mb,pts,['Dummy04']*3,[(0.5,0),(0.5,1),(0.8,0.6)],'frond',[(0,1,2)])
    return build
def fowl_rects(x0): return {'body':R4(x0,x0+0.5,0.5,1),'head':R4(x0,x0+0.25,0.25,0.5),'neck':R4(x0+0.25,x0+0.5,0.25,0.5),
    'tail':R4(x0,x0+0.25,0.125,0.25),'frond':R4(x0+0.25,x0+0.5,0,0.25),'wing':R4(x0,x0+0.125,0,0.125),'leg':R4(x0+0.125,x0+0.25,0,0.125)}
HEN={'body':streaky((0.40,0.35,0.29),(0.72,0.67,0.58),cy=10,cx=30,amt=0.3),'neck':streaky((0.42,0.37,0.31),(0.74,0.70,0.62),cy=6,cx=16),
     'head':eye_head((0.44,0.39,0.33),(0.74,0.70,0.62),0.36,0.55,(0.15,0.09)),
     'tail':streaky((0.36,0.31,0.26),(0.62,0.56,0.48),stripes=(5,0.25)),'frond':feather((0.40,0.34,0.27),(0.30,0.25,0.20),bars=4,bar_col=(0.25,0.21,0.17),bar_amt=0.5),
     'wing':feather((0.42,0.36,0.29),(0.30,0.25,0.20),bars=3,bar_col=(0.26,0.22,0.18),bar_amt=0.5),'leg':scaly((0.55,0.47,0.34),(0.35,0.29,0.21))}
ROOSTER={'body':streaky((0.66,0.30,0.12),(0.90,0.80,0.60),cy=10,cx=30,amt=0.25),'neck':streaky((0.72,0.38,0.14),(0.90,0.78,0.56),cy=6,cx=16,e0=0.6,e1=0.9),
     'head':eye_head((0.64,0.30,0.12),(0.90,0.80,0.62),0.36,0.55,(0.15,0.09),ring=(0.95,0.75,0.25),mask=((0.12,0.12,0.14),0.36)),
     'tail':streaky((0.20,0.20,0.22),(0.70,0.68,0.62),stripes=(6,0.5)),'frond':feather((0.12,0.30,0.30),(0.92,0.90,0.86),bars=5,bar_col=(0.06,0.10,0.10),bar_amt=0.9),
     'wing':feather((0.10,0.32,0.33),(0.08,0.16,0.18),bars=0),'leg':scaly((0.70,0.58,0.30),(0.40,0.32,0.18))}
FOWL_RECTS={'hen':fowl_rects(0.0),'rooster':fowl_rects(0.5)}
FOWL_COAT={'fowls.tga':[('hen',HEN),('rooster',ROOSTER)]}
for nm,anim,male,idle in (('hen',('hen','rooster_walk'),False,'hen_rooster_idle1'),('rooster',('rooster','rooster_walk'),True,'rooster_rooster_idle1')):
    CREATURES['meilong_'+nm]=dict(folder='mei_long',prefix=nm+'_',glbdir=GB,srcdir=SB,anim=anim,texsize=128,rects=FOWL_RECTS,
        models={nm:meilong(male)},coats=FOWL_COAT,exports={nm:(nm,nm)},orig_tex='fowls.tga',preview_model=(nm,'fowls.tga'),
        pose_frame=None,gz=0,tq_dir=(0.9,-0.75,0.5),ga_dir=(-0.15,-0.8,1.0),
        strip_models=[(nm,'fowls.tga','walk'),(nm,'fowls.tga','idle1',idle)])

# ================= Caudipteryx (HERDPEACOCKS): male on peacock skeleton, female on peahen; shared peafowl.tga (male left, female right)
FAN=[(-55,'Dummy20'),(-27,'Dummy26'),(0,'Dummy29'),(27,'Dummy27'),(55,'Dummy22')]
def caudi(male):
    def build(mb):
        root=B('Root'); d4=B('Dummy04'); d5=B('Dummy05'); d6=B('Dummy06'); d7=B('Dummy07'); tl=B('tail')
        loft(mb,[(-3.6,1.7,12.6,1.9),(-1.0,2.5,11.8,2.7),(2.0,2.3,11.4,2.4),(4.5,1.2,11.3,1.3)],lambda p:'Root','body',6,cap0=(0,-4.6,13.4),cap1=(0,5.6,11.3))
        hc=d6+V(0,-0.3,-0.9)
        nsegs=[('Root',root,d4),('Dummy04',d4,d5),('Dummy05',d5,d6),('Dummy06',d6,d7)]
        tube(mb,[V(0,-3.5,13.6),V(0,(hc.y-3.5)/2-0.8,(13.6+hc.z)/2-0.6),hc+V(0,0.9,-0.9)],[1.45,1.05,0.85],seg_bone(nsegs),'neck',5,ref=V(0,1,0))
        loft(mb,[(hc.y+0.9,0.8,hc.z+0.1,0.9),(hc.y-0.4,0.95,hc.z+0.05,1.05),(hc.y-1.6,0.6,hc.z-0.35,0.65)],lambda p:'Dummy06','head',5,
             cap0=(0,hc.y-2.7,hc.z-0.55),cap1=(0,hc.y+1.5,hc.z+0.2))
        for b1,b2,b3,b4,s in (('Dummy08','Dummy09','Dummy10','Dummy11',-1),('Dummy16','Dummy17','Dummy18','Dummy19',1)):
            hip=B(b1); heel=B(b2); ank=B(b3); toe=B(b4)
            top=V(s*1.5,hip.y-0.5,9.8); knee=V(s*1.45,hip.y-1.3,6.4)
            segs=[(b1,top,knee),(b1,knee,heel),(b2,heel,ank)]
            tube(mb,[top,knee,heel,ank+V(0,0,0.1)],[1.3,0.7,0.3,0.25],seg_bone(segs),'leg',3,ref=V(0,-1,0))
            pts=[ank+V(0,0,0.06),toe+V(0,-0.4,0.05),toe+V(s*1.1,0.5,0.05),toe+V(-s*1.1,0.5,0.05),ank+V(0,1.0,0.05)]
            poly(mb,pts,[b3]*5,[(0.5,0),(0.5,1),(1,0.8),(0,0.8),(0.5,0.3)],'leg',[(0,1,2),(0,3,1),(0,4,2)])
        tube(mb,[V(0,4.6,11.4),V(0,8.6,11.6)],[1.0,0.5],lambda p:'tail','tail',4,cap1=0.6)
        base=V(0,8.0,11.7)
        for ang,bn in FAN:
            a=math.radians(ang); d=V(math.sin(a),math.cos(a),0.12); side=V(math.cos(a),-math.sin(a),0)
            ln=7.2 if ang==0 else 6.4
            pts=[base+side*0.3,base+d*ln+side*1.05,base+d*ln-side*1.05,base-side*0.3]
            poly(mb,pts,[bn]*4,[(1,0),(1,1),(0,1),(0,0)],'fan',[(0,1,2,3)])
        for s,wb in ((-1,'Dummy12'),(1,'Dummy14')):
            pts=[V(s*1.9,-2.4,12.9),V(s*2.6,-0.6,10.8),V(s*2.8,3.6,10.6),V(s*2.4,1.6,12.0)]
            poly(mb,pts,[wb]*4,[(0.5,0),(1,0.3),(0.5,1),(0,0.5)],'wing',[(0,1,2,3)])
    return build
def peaf_rects(x0): return {'body':R4(x0,x0+0.5,0.5,1),'neck':R4(x0,x0+0.25,0.25,0.5),'head':R4(x0+0.25,x0+0.5,0.25,0.5),'fan':R4(x0,x0+0.25,0,0.25),
    'leg':R4(x0+0.25,x0+0.375,0.125,0.25),'wing':R4(x0+0.375,x0+0.5,0.125,0.25),'tail':R4(x0+0.25,x0+0.5,0,0.125)}
CMALE={'body':streaky((0.25,0.22,0.20),(0.80,0.74,0.64),cy=12,cx=36,amt=0.3),'neck':streaky((0.36,0.33,0.30),(0.92,0.90,0.85),cy=6,cx=18,e0=0.45,e1=0.6),
       'head':eye_head((0.38,0.36,0.34),(0.90,0.88,0.84),0.36,0.62,(0.12,0.07),beak=(0.28,(0.12,0.10,0.09))),
       'fan':feather((0.10,0.09,0.09),(0.95,0.94,0.90),bars=4,bar_col=(0.93,0.92,0.88),bar_amt=0.9,edge=(0.97,0.97,0.95)),'leg':scaly((0.55,0.46,0.32),(0.32,0.26,0.18)),
       'wing':feather((0.12,0.11,0.11),(0.95,0.94,0.90),bars=3,bar_col=(0.92,0.91,0.87),bar_amt=0.85),'tail':streaky((0.20,0.18,0.17),(0.5,0.45,0.4))}
CFEM={'body':streaky((0.45,0.37,0.28),(0.78,0.71,0.60),cy=12,cx=36,amt=0.3),'neck':streaky((0.48,0.41,0.32),(0.80,0.75,0.66),cy=6,cx=18),
       'head':eye_head((0.48,0.42,0.34),(0.80,0.75,0.66),0.36,0.62,(0.12,0.07),beak=(0.28,(0.20,0.17,0.14))),
       'fan':feather((0.42,0.34,0.26),(0.55,0.47,0.37),bars=4,bar_col=(0.30,0.24,0.18),bar_amt=0.45),'leg':scaly((0.55,0.46,0.32),(0.32,0.26,0.18)),
       'wing':feather((0.44,0.36,0.28),(0.56,0.48,0.38),bars=3,bar_col=(0.32,0.26,0.20),bar_amt=0.4),'tail':streaky((0.42,0.35,0.27),(0.6,0.52,0.42))}
PEAF_RECTS={'peacock':peaf_rects(0.0),'peahen':peaf_rects(0.5)}
PEAF_COAT={'peafowl.tga':[('peacock',CMALE),('peahen',CFEM)]}
CREATURES['caudi_male']=dict(folder='caudipteryx',prefix='male_',glbdir=GB,srcdir=SB,anim=('peacock','peacock_walk1'),texsize=128,rects=PEAF_RECTS,
    models={'peacock':caudi(True)},coats=PEAF_COAT,exports={'Peacock':('peacock','peacock')},orig_tex='peafowl.tga',preview_model=('peacock','peafowl.tga'),
    pose_frame=None,gz=0,tq_dir=(0.9,-0.75,0.5),strip_models=[('peacock','peafowl.tga','walk'),('peacock','peafowl.tga','idle3_display','peacock_peacock_idle3'),('peacock','peafowl.tga','idle2_peck','peacock_peacock_idle2')])
CREATURES['caudi_female']=dict(folder='caudipteryx',prefix='female_',glbdir=GB,srcdir=SB,anim=('peahen','peahen_walk1'),texsize=128,rects=PEAF_RECTS,
    models={'peahen':caudi(False)},coats=PEAF_COAT,exports={'Peahen':('peahen','peahen')},orig_tex='peafowl.tga',preview_model=('peahen','peafowl.tga'),
    pose_frame=None,gz=0,tq_dir=(0.9,-0.75,0.5),strip_models=[('peahen','peafowl.tga','walk'),('peahen','peafowl.tga','idle1_wings','peahen_peahen_idle1')])

# ================= Beipiaosaurus (HERDBLACKBEAR) on the PEAHEN skeleton (bear anims -> Peahen anims in XML)
def beipiao(head=1.0,body=1.0,fluff=1.0,claw=1.0):
    def build(mb):
        root=B('Root'); d4=B('Dummy04'); d5=B('Dummy05'); d6=B('Dummy06'); d7=B('Dummy07')
        bs=body*(1+0.08*(fluff-1))
        loft(mb,[(-4.6,2.4*bs,13.6,2.6*bs),(-2.4,3.9*bs,12.0,4.4*bs),(0.6,4.3*bs,11.0,4.8*bs),(3.4,3.3*bs,11.2,3.6*bs),(5.4,1.6*bs,11.6,1.8*bs)],
             lambda p:'Root','body',6,cap0=(0,-5.4,14.6),cap1=(0,6.2,11.6))
        nsegs=[('Root',root,d4),('Dummy04',d4,d5),('Dummy05',d5,d6),('Dummy06',d6,d7)]
        nb=seg_bone(nsegs)
        tube(mb,[V(0,-4.6,14.8),V(0,-6.1,16.7),V(0,-6.8,18.8),V(0,-7.0,19.9)],[1.6*bs,1.2*bs,0.95*fluff**0.5,0.85],nb,'neck',5,ref=V(0,1,0))
        hc=d6+V(0,-0.6,-0.3); H=lambda y,z:(hc.y+(y-hc.y)*head,hc.z+(z-hc.z)*head)
        rings=[]
        for y,w,z,h in [(hc.y+0.8,0.75,hc.z+0.1,0.8),(hc.y-0.4,0.8,hc.z,0.8),(hc.y-1.5,0.45,hc.z-0.3,0.45)]:
            yy,zz=H(y,z); rings.append((yy,w*head,zz,h*head))
        c0=H(hc.y-2.4,hc.z-0.5); c1=H(hc.y+1.3,hc.z+0.15)
        loft(mb,rings,lambda p:'Dummy06','head',5,cap0=(0,c0[0],c0[1]),cap1=(0,c1[0],c1[1]))
        for s,wb in ((-1,'Dummy12'),(1,'Dummy14')):
            sh=V(s*3.3*bs,-3.3,13.6); el=V(s*3.9*bs,-3.7,10.6); wr=V(s*3.4*bs,-5.4,8.6)
            tube(mb,[sh,el,wr],[1.05*fluff**0.5,0.75*fluff**0.5,0.5],lambda p,b=wb:b,'arm',4,ref=V(0,-1,0))
            for dx in (-0.45,0.0,0.45):   # three long sickle claws
                tip=wr+V(s*dx*0.8,-2.3*claw,-1.6*claw); mid=wr+V(s*dx*0.5,-1.6*claw,-0.4*claw)
                pts=[wr+V(s*dx-0.12,0.1,0.1),mid,tip,wr+V(s*dx+0.12,0.1,-0.1)]
                poly(mb,pts,[wb]*4,[(0,0),(0.5,0.6),(0.5,1),(1,0)],'claw',[(0,1,3),(1,2,3)])
            fl=fluff
            pts=[el+V(s*0.2,0.6,0.3),wr+V(s*0.15,0.6,0.0),wr+V(s*0.2,0.9,-1.9*fl),el+V(s*0.3,1.2,-2.4*fl)]
            poly(mb,pts,[wb]*4,[(0,0),(1,0),(1,1),(0,1)],'fringe',[(0,1,2,3)])
        for b1,b2,b3,b4,s in (('Dummy08','Dummy09','Dummy10','Dummy11',-1),('Dummy16','Dummy17','Dummy18','Dummy19',1)):
            heel=B(b2); ank=B(b3); toe=B(b4)
            top=V(s*2.5*bs,1.6,10.2); knee=V(s*2.2*bs,0.4,6.3); hl=V(s*1.4,heel.y,heel.z)
            segs=[(b1,top,knee),(b1,knee,hl),(b2,hl,ank)]
            tube(mb,[top,knee,hl,V(s*1.2,ank.y-0.1,0.45)],[2.1*bs,1.35*fluff**0.5,0.6,0.5],seg_bone(segs),'leg',4,ref=V(0,-1,0))
            a=V(s*1.2,ank.y-0.2,0.35)
            for dx,ln in ((-0.9,1.9),(0.0,2.5),(0.9,1.9)):   # three slim forward toes + small hallux
                tp=V(s*1.2+dx*1.1,ank.y-0.2-ln*1.05,0.06)
                pts=[a+V(-0.28,0,0),tp,a+V(0.28,0,0),a+V(0,0,-0.3)]
                poly(mb,pts,[b3]*4,[(0,0),(0.5,1),(1,0),(0.5,0.2)],'toes',[(0,1,3),(3,1,2)])
            pts=[a+V(-0.2,0,0),V(s*1.2,ank.y+1.0,0.1),a+V(0.2,0,0)]
            poly(mb,pts,[b3]*3,[(0,0),(0.5,1),(1,0)],'toes',[(0,1,2)])
        tube(mb,[V(0,5.6,11.6),V(0,10.0,11.0)],[1.4*bs,0.5],lambda p:'tail','tail',5,cap1=0.8)
        pts=[V(0,7.6,12.5),V(0,12.4+1.5*(fluff-1),12.6),V(0,12.2+1.5*(fluff-1),9.6),V(0,8.2,10.3)]
        poly(mb,pts,['tail']*4,[(0,0),(0,1),(1,1),(1,0)],'fringe',[(0,1,2,3)])
        # dorsal filament mane along neck and back (zig-zag)
        line=[V(0,-6.6,20.3),V(0,-5.9,18.2),V(0,-5.0,16.6),V(0,-3.2,16.3*bs**0.3+0.4),V(0,-0.6,15.9*bs**0.3+0.5),V(0,2.2,15.0*bs**0.3+0.3),V(0,4.6,13.4)]
        bones=[nb(p) for p in line]; L=len(line)
        for i in range(L-1):
            a,b=line[i],line[i+1]; tip=(a+b)/2+V(0,0.9*fluff,0.9*fluff)
            poly(mb,[a,tip,b],[bones[i],bones[i],bones[i+1]],[(0,i/(L-1)),(0.5+0.5*fluff/1.4,(i+0.5)/(L-1)),(0,(i+1)/(L-1))],'fringe',[(0,1,2)])
    return build
BEI_RECTS={'body':(0,0.5,0.5,1),'neck':(0.5,0.75,0.75,1),'head':(0.75,0.75,1,1),'arm':(0.5,0.5,0.75,0.75),'leg':(0.75,0.5,1,0.75),
           'fringe':(0,0.25,0.5,0.5),'claw':(0.5,0.25,0.625,0.5),'toes':(0.625,0.25,0.75,0.5),'tail':(0.75,0.25,1,0.5),'spare':(0,0,1,0.25)}
def bei_coat(back,belly,face,fr,claw=(0.16,0.14,0.12),stripes=None):
    return {'body':streaky(back,belly,cy=5,cx=48,amt=0.4,stripes=stripes),'neck':streaky(back,belly,cy=4,cx=24,amt=0.35),
            'head':eye_head(face,tuple(min(1,x*1.1) for x in face),0.38,0.6,(0.11,0.06),beak=(0.22,(0.18,0.16,0.14)),ring=face),
            'arm':streaky(back,belly,cy=4,cx=24,amt=0.4,e0=0.5,e1=0.9),'leg':streaky(back,belly,cy=4,cx=24,amt=0.4,e0=0.55,e1=0.95),
            'fringe':feather(fr[0],fr[1]),'claw':feather(claw,tuple(min(1,x*3.2) for x in claw)),'toes':scaly((0.20,0.18,0.16),(0.09,0.08,0.07)),
            'tail':streaky(back,belly,cy=4,cx=24,amt=0.4),'spare':flat(back)}
CREATURES['beipiaosaurus']=dict(folder='beipiaosaurus',glbdir=GB,srcdir=SB,anim=('peahen','peahen_walk1'),texsize=128,rects=BEI_RECTS,
    models={'adult':beipiao(),'cub':beipiao(head=1.3,body=0.9,fluff=0.85,claw=0.65),'adult_snow':beipiao(fluff=1.45),'cub_snow':beipiao(head=1.3,body=0.9,fluff=1.25,claw=0.65)},
    coats={'blackbear.tga':('adult',bei_coat((0.36,0.27,0.19),(0.55,0.44,0.33),(0.42,0.34,0.26),((0.33,0.25,0.18),(0.52,0.42,0.30)))),
           'blackbear2.tga':('adult',bei_coat((0.18,0.14,0.12),(0.36,0.29,0.23),(0.62,0.56,0.48),((0.16,0.13,0.11),(0.40,0.33,0.26)))),
           'blackbear_cub.tga':('cub',bei_coat((0.56,0.45,0.31),(0.76,0.67,0.52),(0.62,0.52,0.38),((0.52,0.42,0.30),(0.74,0.64,0.48)),stripes=(5,0.25))),
           'blackbear_snowy.tga':('adult_snow',bei_coat((0.80,0.79,0.74),(0.95,0.94,0.90),(0.70,0.68,0.62),((0.82,0.81,0.76),(0.97,0.97,0.95)),claw=(0.22,0.20,0.18)))},
    exports={'blackbear':('adult','peahen'),'blackbear_cub':('cub','peahen'),'blackbear_snowy':('adult_snow','peahen'),'blackbear_cub_snowy':('cub_snow','peahen')},
    compare_glb='blackbear_blackbear_walk',model_tex={'cub_snow':'blackbear_snowy.tga'},orig_tex='blackbear.tga',preview_model=('adult','blackbear.tga'),pose_frame=None,gz=0,tq_dir=(0.9,-0.75,0.5),gap=0.25,
    strip_models=[('adult','blackbear.tga','walk'),('adult','blackbear.tga','idle1_claw_display','peahen_peahen_idle1'),('adult','blackbear.tga','idle2_browse','peahen_peahen_idle2')],
    variants=[('adult','blackbear.tga','adult (blackbear.tga)'),('adult','blackbear2.tga','adult dark (blackbear2.tga)'),('cub','blackbear_cub.tga','cub (blackbear_cub.tga, XML scale .75)'),
              ('adult_snow','blackbear_snowy.tga','arctic adult (blackbear_snowy model+tga)'),('cub_snow','blackbear_snowy.tga','arctic cub')])

# ================= Beipiaosaurus v2: heavy, shaggy "feathered ground sloth on two legs" (still PEAHEN skeleton)
def fuzz(back,belly,e0=0.3,e1=0.85,seed=11,amt=0.22,mott=0.26,hdir='s',dens=0.12,stripes=None,tipl=None):
    """soft mottled filament coat: low-freq mottling + many short jittered strokes. hdir='s' strokes run along s (axis1, e.g. top->belly
    on lofts), 't' along t (axis0, along tubes/tufts). tipl=(c0,c1): instead of back->belly by s, colour by t (tufts: base->tip)."""
    def f(s,t,sh):
        h,w=sh; rng=np.random.default_rng(seed+h*7+w)
        if tipl is None: col=lerp(C(back,sh),C(belly,sh),smooth(e0,e1,s))
        else: col=lerp(C(tipl[0],sh),C(tipl[1],sh),smooth(0.1,1.0,t))
        m=vnoise2(h,w,4,4,seed)*0.6+vnoise2(h,w,9,9,seed+1)*0.4
        col=col*(1-mott/2+mott*m)[...,None]
        N=int(h*w*dens); K=7
        y0=rng.uniform(0,h,N); x0=rng.uniform(0,w,N)
        ang=rng.normal(0,0.35,N)+(0 if hdir=='s' else np.pi/2)
        ln=rng.uniform(2.5,max(3.0,min(h,w)/9),N); val=rng.choice([-1.0,1.0],N)*rng.uniform(0.5,1.0,N)
        k=np.linspace(0,1,K)[None,:]
        xs=(x0[:,None]+np.cos(ang)[:,None]*ln[:,None]*k).astype(int)%w; ys=(y0[:,None]+np.sin(ang)[:,None]*ln[:,None]*k).astype(int)%h
        L=np.zeros(sh); np.add.at(L,(ys.ravel(),xs.ravel()),(val[:,None]*(1-0.5*k)).repeat(1,0).ravel() if False else np.repeat(val[:,None],K,1).ravel()*np.tile(1-0.5*k[0],N))
        L=(L*0.6+0.1*(np.roll(L,1,0)+np.roll(L,-1,0)+np.roll(L,1,1)+np.roll(L,-1,1)))
        col=col*(1+amt*np.clip(L,-1.6,1.6))[...,None]
        if stripes is not None:
            kk,a=stripes; col=col*(1-a*smooth(0.55,0.9,0.5+0.5*np.sin(t*kk*2*np.pi))*smooth(0.6,0.2,s))[...,None]
        return col
    return f

def beipiao2(head=1.0,body=1.0,fluff=1.0,claw=1.0,seed=5):
    def build(mb):
        rnd=np.random.default_rng(seed)
        root=B('Root'); d4=B('Dummy04'); d5=B('Dummy05'); d6=B('Dummy06'); d7=B('Dummy07')
        bs=body*(1+0.07*(fluff-1))
        RG=[(-4.7,2.7*bs,13.8,2.7*bs),(-2.4,4.5*bs,12.0,4.5*bs),(0.6,5.5*bs,10.6,5.3*bs),(3.4,5.3*bs,10.8,4.5*bs),(5.6,3.0*bs,11.4,2.7*bs)]
        loft(mb,RG,lambda p:'Root','body',8,cap0=(0,-5.8,14.8),cap1=(0,7.0,11.6))
        def bpt(y,th,out=0.0):
            for a,b in zip(RG,RG[1:]):
                if a[0]<=y<=b[0]: f=(y-a[0])/(b[0]-a[0]); break
            else: a=b=RG[0] if y<RG[0][0] else RG[-1]; f=0
            w=a[1]+(b[1]-a[1])*f; zc=a[2]+(b[2]-a[2])*f; hh=a[3]+(b[3]-a[3])*f
            n=V(math.sin(th)*hh,0,math.cos(th)*w).normalized()
            return V(w*math.sin(th),y,zc+hh*math.cos(th))+n*out, n
        def tuft2(base,d,side,ln,wd,bone,lift_dir,lift):   # ragged two-pronged filament tuft (3 tris)
            d=d.normalized(); side=side.normalized(); L=lambda f,o:base+d*ln*f+side*o+lift_dir*lift*f
            pts=[base+side*wd/2,L(1.0,wd*0.22),L(0.7,0.0),L(0.9,-wd*0.25),base-side*wd/2]
            bb=bone if isinstance(bone,list) else [bone]*5
            poly(mb,pts,bb,[(0,0),(0.3,1),(0.5,0.45),(0.7,0.8),(1,0)],'fringe',[(0,1,2),(0,2,4),(2,3,4)])
        def tuft1(base,d,side,ln,wd,bone,lift_dir,lift):
            d=d.normalized(); side=side.normalized()
            poly(mb,[base+side*wd/2,base+d*ln+lift_dir*lift,base-side*wd/2],[bone]*3,[(0,0),(0.5,1),(1,0)],'fringe',[(0,1,2)])
        # neck: thick shaggy base, tapering; follows the bone chain so the head stays attached
        nsegs=[('Root',root,d4),('Dummy04',d4,d5),('Dummy05',d5,d6),('Dummy06',d6,d7)]; nb=seg_bone(nsegs)
        fz=fluff**0.4
        NP=[V(0,-3.7,13.7),V(0,-5.9,16.4),V(0,-6.6,18.6),V(0,-6.9,19.9)]; NR=[2.5*bs*fz,1.6*fz,1.15*fz,0.85*head]
        tube(mb,NP,NR,nb,'neck',6,ref=V(0,1,0))
        # small head with leaf-shaped (wide, flat, slightly down-turned) beak
        hc=d6+V(0,-0.5,-0.3); hs=0.8*head
        def H(dy,w,dz,h): return (hc.y+dy*hs,w*hs,hc.z+dz*hs,h*hs)
        rings=[H(0.7,0.62,0.1,0.66),H(-0.3,0.72,0.05,0.68),H(-1.2,0.55,-0.2,0.38),H(-1.8,0.52,-0.38,0.2)]
        loft(mb,rings,lambda p:'Dummy06','head',6,cap0=(0,hc.y-2.55*hs,hc.z-0.6*hs),cap1=(0,hc.y+1.2*hs,hc.z+0.05*hs))
        # arms hang forward, shaggy upper arm, three long curved claws
        for s,wb in ((-1,'Dummy12'),(1,'Dummy14')):
            sh=V(s*3.7*bs,-3.2,13.0); el=V(s*4.5*bs,-4.5,10.0); wr=V(s*4.0*bs,-6.6,8.5)
            tube(mb,[sh,el,wr],[1.6*fz,1.05*fz,0.65],lambda p,b=wb:b,'arm',5,ref=V(0,-1,0))
            for dx in (-0.5,0.0,0.5):
                tip=wr+V(s*dx*0.9,-2.0*claw,-2.6*claw); mid=wr+V(s*dx*0.6,-1.7*claw,-0.7*claw)
                pts=[wr+V(s*dx-0.14,0.1,0.1),mid,tip,wr+V(s*dx+0.14,0.1,-0.1)]
                poly(mb,pts,[wb]*4,[(0,0),(0.5,0.6),(0.5,1),(1,0)],'claw',[(0,1,3),(1,2,3)])
            fl=fluff
            pts=[el+V(s*0.5,0.7,0.2),wr+V(s*0.4,0.6,0.0),wr+V(s*0.3,1.0,-1.6*fl),el+V(s*0.6,1.4,-2.3*fl)]
            poly(mb,pts,[wb]*4,[(0,0),(1,0),(1,1),(0,1)],'fringe',[(0,1,2,3)])
            tuft1(sh+V(s*1.0,1.0,-0.6),V(s*0.2,0.5,-1),V(0,1,0),1.8*fl,1.6,wb,V(s,0,0),0.4)   # shoulder shag
        # sturdy legs: heavy thighs, thick shins
        for b1,b2,b3,b4,s in (('Dummy08','Dummy09','Dummy10','Dummy11',-1),('Dummy16','Dummy17','Dummy18','Dummy19',1)):
            heel=B(b2); ank=B(b3); toe=B(b4)
            top=V(s*3.2*bs,1.9,9.8); knee=V(s*2.8*bs,0.5,6.2); hl=V(s*1.6,heel.y,heel.z)
            segs=[(b1,top,knee),(b1,knee,hl),(b2,hl,ank)]
            tube(mb,[top,knee,hl,V(s*1.25,ank.y-0.1,0.5)],[2.9*bs*fz,1.8*fz,1.0,0.8],seg_bone(segs),'leg',5,ref=V(0,-1,0))
            for k,(yy,zz) in enumerate(((2.2,6.6),)):   # ragged thigh "trousers"
                tuft1(V(s*(3.0*bs*fz),yy,zz),V(s*0.1,0.35,-1),V(0,1,0),1.4*fluff**0.7,1.8,b1,V(s,0,0),0.12)
            a=V(s*1.25,ank.y-0.2,0.38)
            for dx,ln in ((-0.95,2.0),(0.0,2.6),(0.95,2.0)):
                tp=V(s*1.25+dx*1.15,ank.y-0.2-ln*1.05,0.06)
                pts=[a+V(-0.38,0,0),tp,a+V(0.38,0,0),a+V(0,0,-0.32)]
                poly(mb,pts,[b3]*4,[(0,0),(0.5,1),(1,0),(0.5,0.2)],'toes',[(0,1,3),(3,1,2)])
            pts=[a+V(-0.25,0,0),V(s*1.25,ank.y+1.0,0.1),a+V(0.25,0,0)]
            poly(mb,pts,[b3]*3,[(0,0),(0.5,1),(1,0)],'toes',[(0,1,2)])
        # short tail with a shaggy end
        tube(mb,[V(0,5.6,11.7),V(0,8.4,11.1),V(0,10.0,10.7)],[1.9*bs*fz,0.95,0.35],lambda p:'tail','tail',5)
        for sx in (-0.6,0.6):
            tuft2(V(sx*0.7,8.4,11.2),V(sx*0.4,1,-0.25),V(1,0,0.0),1.3*fluff**0.6,1.9,'tail',V(0,0,1),0.1)
        # low ragged dorsal shag: neck crest + back (lies flat, slightly lifted, alternating lean)
        for i,f in enumerate((0.15,0.45,0.75,0.98)):
            seg=min(int(f*3),2); u=f*3-seg; p=NP[seg]+(NP[seg+1]-NP[seg])*u; r=NR[seg]+(NR[seg+1]-NR[seg])*u
            tg=(NP[seg+1]-NP[seg]).normalized(); dv=V(0,1,0)-tg*tg.y; dv.normalize()
            base=p+dv*r*0.9; lean=V((-1)**i*0.25,0,0)
            ln=(1.1+0.5*rnd.random())*fluff*(0.8+0.25*(1-f))
            tuft2(base-dv*0.15,-tg+lean,V(1,0,0),ln*0.8,1.4+0.5*(1-f),nb(base),dv,0.12)
        for i,y in ():   # v2: back tufts dropped (read as scutes/plates); the back shag is carried by the texture
            base,n=bpt(y,0.0,-0.18); lean=V((-1)**i*0.3,0,0)
            tuft2(base,V(0,1,-0.3)+lean,V(1,0,0),(1.1+0.4*rnd.random())*fluff**0.6,2.4,'Root',n,0.18)
        # ragged belly/flank hem
        for s in (-1,1):
            for j,y in enumerate((-1.8,0.4,2.4)):
                th=s*math.pi*(0.62+0.06*(j%2)); base,n=bpt(y,th,-0.3)
                tuft1(base,V(s*0.1,0.3,-1),V(0,1,0),(1.1+0.4*rnd.random())*fluff**0.7,2.0,'Root',n,0.15)
    return build

BEI2_RECTS={'body':(0,0.5,0.5,1),'neck':(0.5,0.75,0.75,1),'head':(0.75,0.75,1,1),'arm':(0.5,0.5,0.75,0.75),'leg':(0.75,0.5,1,0.75),
           'fringe':(0,0.25,0.5,0.5),'claw':(0.5,0.25,0.625,0.5),'toes':(0.625,0.25,0.75,0.5),'tail':(0.75,0.25,1,0.5),'spare':(0,0,1,0.25)}
def bei2_coat(back,belly,face,claw=(0.17,0.15,0.13),stripes=None,seed=11,mott=0.26,amt=0.22):
    mid=tuple(a*0.6+b*0.4 for a,b in zip(back,belly))
    return {'body':fuzz(back,belly,0.3,0.85,seed,hdir='s',stripes=stripes,mott=mott,amt=amt),'neck':fuzz(back,belly,0.5,1.0,seed+1,hdir='t',mott=mott,amt=amt),
            'head':eye_head(face,tuple(min(1,x*1.12) for x in face),0.36,0.6,(0.10,0.065),beak=(0.35,(0.30,0.27,0.22)),ring=tuple(x*0.8 for x in face)),
            'arm':fuzz(back,mid,0.4,0.95,seed+2,hdir='t',mott=mott,amt=amt),'leg':fuzz(back,mid,0.45,1.0,seed+3,hdir='t',mott=mott,amt=amt),
            'fringe':fuzz(back,belly,seed=seed+4,hdir='t',amt=amt*1.3,mott=mott,tipl=(back,tuple(min(1,x*1.08) for x in mid))),
            'claw':feather(claw,tuple(min(1,x*3.0) for x in claw)),'toes':scaly((0.22,0.20,0.17),(0.10,0.09,0.08)),
            'tail':fuzz(back,mid,0.4,0.9,seed+5,hdir='t',mott=mott,amt=amt),'spare':flat(back)}
CUBR=1/1.3   # cub XML scale 1 vs adult 1.3
CREATURES['beipiaosaurus_v2']=dict(folder='beipiaosaurus',pdir='preview_v2',glbdir=GB,srcdir=SB,anim=('peahen','peahen_walk1'),texsize=128,rects=BEI2_RECTS,
    models={'adult':beipiao2(),'cub':beipiao2(head=1.3,body=0.95,fluff=0.9,claw=0.6,seed=7),'adult_snow':beipiao2(fluff=1.5,seed=5),'cub_snow':beipiao2(head=1.3,body=0.95,fluff=1.3,claw=0.6,seed=7)},
    coats={'blackbear.tga':('adult',bei2_coat((0.30,0.22,0.15),(0.64,0.57,0.47),(0.40,0.33,0.26))),
           'blackbear2.tga':('adult',bei2_coat((0.17,0.14,0.12),(0.44,0.39,0.33),(0.32,0.28,0.24),seed=21)),
           'blackbear_cub.tga':('cub',bei2_coat((0.47,0.38,0.28),(0.75,0.69,0.58),(0.55,0.47,0.37),stripes=(5,0.22),seed=31)),
           'blackbear_snowy.tga':('adult_snow',bei2_coat((0.79,0.76,0.68),(0.94,0.92,0.86),(0.72,0.69,0.62),claw=(0.22,0.20,0.18),seed=41,mott=0.14,amt=0.14))},
    exports={'blackbear':('adult','peahen'),'blackbear_cub':('cub','peahen'),'blackbear_snowy':('adult_snow','peahen'),'blackbear_cub_snowy':('cub_snow','peahen')},
    compare_glb='blackbear_blackbear_walk',model_tex={'cub_snow':'blackbear_snowy.tga'},orig_tex='blackbear.tga',preview_model=('adult','blackbear.tga'),
    cmp_scale=1.3,cmp_caption='IN-GAME SCALE: Beipiaosaurus adult at XML scale 1.3 (left) vs original black bear at scale 1 (right)',
    extra_compares=[('cub','blackbear_cub_blackbear_walk','blackbear_cub.tga',1/0.75,'_cub','IN-GAME SCALE: Beipiaosaurus cub at XML scale 1 (left) vs original bear cub at scale .75 (right)')],
    pose_frame=None,gz=0,tq_dir=(0.9,-0.75,0.5),gap=0.25,
    strip_models=[('adult','blackbear.tga','walk'),('adult','blackbear.tga','default','peahen_peahen_default'),('adult','blackbear.tga','idle1_claw_display','peahen_peahen_idle1'),
                  ('adult','blackbear.tga','idle2_browse','peahen_peahen_idle2'),('adult_snow','blackbear_snowy.tga','walk_snow')],
    variants=[('adult','blackbear.tga','adult (blackbear.tga) x1.3'),('adult','blackbear2.tga','adult dark (blackbear2.tga) x1.3'),('cub','blackbear_cub.tga','cub (blackbear_cub.tga) x1',CUBR),
              ('adult_snow','blackbear_snowy.tga','arctic adult (blackbear_snowy) x1.3'),('cub_snow','blackbear_snowy.tga','arctic cub x1',CUBR)],
    var_caption='Variants at relative in-game scale: adult (1.3) | adult dark (1.3) | cub (1.0) | arctic adult (1.3) | arctic cub (1.0)')
