import re,os,xml.etree.ElementTree as ET,hashlib
A='/workspace/ages-of-earth-mod/v0.1'; B='/workspace/ages-of-earth-mod/v0.2'
def skel(s):
    # blank out text nodes inside STRING elements but keep markup inside them
    def f(m):
        body=m.group(2)
        toks=re.split(r'(<!--.*?-->|<[^>]+>)',body,flags=re.S)
        return m.group(1)+''.join(t if i%2 else '§' for i,t in enumerate(toks))+m.group(3)
    return re.sub(r'(<STRING(?:\s[^>]*)?>)(.*?)(</STRING>)',f,s,flags=re.S)
ok=True
for d in ['Data','tribes']:
    for fn in sorted(os.listdir(f'{A}/{d}')):
        a=open(f'{A}/{d}/{fn}','rb').read(); b=open(f'{B}/{d}/{fn}','rb').read()
        if a==b: continue
        sa=a.decode('utf-8'); sb=b.decode('utf-8')
        same=skel(sa)==skel(sb)
        try: ET.fromstring(b); parse='ok'
        except Exception as e: parse='FAIL '+str(e); ok=False
        crlf=(a.count(b'\r\n'),b.count(b'\r\n'),a.count(b'\n'),b.count(b'\n'))
        bom=b[:3]==b'\xef\xbb\xbf'
        print(f'{d}/{fn}: changed; structure_identical={same}; parse={parse}; CRLF v0.1/v0.2={crlf[0]}/{crlf[1]} LF={crlf[2]}/{crlf[3]}; BOM={bom}')
        bareA=crlf[2]-crlf[0]; bareB=crlf[3]-crlf[1]
        print('   bare LF v0.1/v0.2:',bareA,bareB)
        ok&=same and bareA==bareB and not bom
print('ALL OK' if ok else 'PROBLEMS')
