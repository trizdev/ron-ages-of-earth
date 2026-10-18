import sys,json,os
from PIL import Image, ImageDraw
R='/workspace/prehistoric-herds/'+sys.argv[1]
info=json.load(open(R+'/_frames/info.json'))
PF=info.get('prefix',''); PD=info.get('pdir','preview')
for lab,an in (info['strips'] if 'strips' in info else [[l,info['anim']] for l in info['labels']]):
    ims=[Image.open(R+f'/_frames/anim_{lab}_{k}.png') for k in range(len(info['frames']))]
    cols=3; rows=(len(ims)+cols-1)//cols; w,h=ims[0].size
    st=Image.new('RGB',(w*cols,h*rows),'white'); d=ImageDraw.Draw(st)
    for k,im in enumerate(ims):
        x=(k%cols)*w; y=(k//cols)*h; st.paste(im,(x,y)); d.text((x+6,y+4),f"{an} {k+1}/{len(ims)} {lab}",fill=(0,0,0))
    st.save(R+'/'+PD+'/'+PF+'03_anim_strip'+('_'+lab if lab else '')+'.png')
tv=R+'/'+PD+'/'+PF+'06_top_view.png'
if os.path.exists(tv):
    Image.open(tv).rotate(180).save(tv)
out=json.load(open(R+'/tex/outtex.json'))
for tga,png in out.items():
    im=Image.open(png).convert('RGBA'); im.save(R+'/export/'+tga,compression='tga_rle')
    k=max(1,512//im.width)
    im.resize((im.width*k,im.height*k),Image.NEAREST).save(R+'/'+PD+'/05_texture_'+tga.replace('.tga','')+f'_x{k}.png')
for fn,cap in info.get('captions',{}).items():
    fp=R+'/'+PD+'/'+PF+fn
    if os.path.exists(fp):
        im=Image.open(fp).convert('RGB'); d=ImageDraw.Draw(im); from PIL import ImageFont; fnt=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18); d.rectangle((0,0,im.width,28),fill=(235,232,220)); d.text((8,4),cap,fill=(0,0,0),font=fnt); im.save(fp)
print('post ok')
