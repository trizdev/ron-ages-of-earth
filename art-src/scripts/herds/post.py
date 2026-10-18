import sys, json, os
from PIL import Image, ImageDraw
R='/workspace/prehistoric-herds/'+sys.argv[1]
PV=sys.argv[3] if len(sys.argv)>3 else 'preview'
fr=json.load(open(R+'/_frames/frames.json')); anim=sys.argv[2]
ims=[Image.open(R+'/_frames/walk_%03d.png'%f).convert('RGB') for f in fr]
w,h=ims[0].size; cw,ch=int(w*0.96),int(h*0.92)
st=Image.new('RGB',(cw*2,ch*2),'white')
for i,(im,f) in enumerate(zip(ims,fr)):
    c=im.crop(((w-cw)//2,(h-ch)//2,(w-cw)//2+cw,(h-ch)//2+ch)); ImageDraw.Draw(c).text((10,8),'%s frame %d'%(anim,f),fill=(20,20,20))
    st.paste(c,((i%2)*cw,(i//2)*ch))
st.save(R+'/'+PV+'/05_walk_test_strip.png')
for src,dst in json.load(open(R+'/tex/outtex.json')):
    im=Image.open(src).convert('RGBA'); im.save(R+'/export/'+dst,compression='tga_rle')
    im.resize((im.width*4,im.height*4),Image.NEAREST).save(R+'/'+PV+'/07_texture_'+dst.replace('.tga','')+'_x4.png')
print('post ok')
