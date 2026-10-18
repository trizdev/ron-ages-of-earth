#!/usr/bin/env python3
"""Ages of Earth v0.2 text proposal: patches a COPY of v0.1 (never rebuilds v0.1)."""
import re, csv, shutil, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from help_rules import R, T
from ts_map import TS

V01='/workspace/ages-of-earth-mod/v0.1'
V02='/workspace/ages-of-earth-mod/v0.2'
for sub in ('Data','tribes'):
    if os.path.exists(f'{V02}/{sub}'): shutil.rmtree(f'{V02}/{sub}')
shutil.copytree(V01+'/Data', V02+'/Data'); shutil.copytree(V01+'/tribes', V02+'/tribes')
changes=[]

def rd(p): return open(p,encoding='utf-8',newline='').read()
def wr(p,s): open(p,'w',encoding='utf-8',newline='').write(s)

# ---------------- era descriptions (LIBRARY/AGES + AGETECH) ----------------
LEAD="{Age} advances carry your lineage through deep time; each one unlocks new creatures and habitats."
AGE_TEXT={
'AGETECH':"{Age} advances carry your lineage through deep time; they make new units and buildings\navailable. To advance in Age, click the buttons with roman numerals in the top row of your Fossil Record.",
'AGE0':LEAD+"\nMost games begin in the {Primordial Age}: soft-bodied life drifts and crawls over microbial mats in warm, shallow seas. Research at the Fossil Record to evolve onward.",
'AGE1':LEAD+"\nAdvancing to the #ICON28 {Cambrian Explosion}: shells, eyes and claws appear almost at once, and predator and prey race to outgrow each other. New resources become available (#ICON4 Instinct and #ICON5 Minerals), along with the Herd Senate for government powers, Reef Forts for defense, and Stampede Pens and Rockfall Works for powerful new kinds of units.",
'AGE2':LEAD+" Advancing to the #ICON29 {Age of Fins}: jawed fish rule the seas while the first forests and four-limbed pioneers reach the shore. Your creatures gain stronger jaws and armor, and you can raise Horseshoe Supply Wagons to support them and Chamele-spies to subvert your enemies.",
'AGE3':LEAD+"\nAdvancing to the #ICON30 {Coal Forest Age}: steaming swamps of giant ferns, oxygen-rich air, metre-long dragonflies and the first reptiles. Powerful spine-shooting creatures become available.",
'AGE4':LEAD+"\nAdvancing to the #ICON31 {Triassic Dawn}: life rebuilds after the Great Dying; early dinosaurs, mammal ancestors and sea reptiles spread across one supercontinent. New spine-shooters and heavy siege beasts become available.",
'AGE5':LEAD+"\nAdvancing to the #ICON32 {Jurassic Heights}: long-necked giants browse conifer forests, while the first birds take to the air. Gives you access to a new resource #ICON12 (Oil) and brings Armorbacks and Flyers for the first time.",
'AGE6':LEAD+"\nAdvancing to the #ICON33 {Cretaceous Bloom}: flowers spread across the land, horned and armored giants roam, and the skies fill with wings, until the sky falls. Unlocks powerful late-age creatures and habitats, including the power to call down Extinction Events.",
'AGE7':LEAD+"\nAdvancing to the #ICON34 {Cenozoic Rise}: the survivors inherit the Earth, with grasslands, ice sheets, giant mammals and terror birds. The game's most powerful units and buildings at last become available.",
}
# whole-entry text overrides for other sections: key -> list of (old, new) literal replacements
LITERAL={
 'ACHIEVECHART/CLASSICAL_AGE':[('the Classical Age','the Cambrian Explosion')],
 'ACHIEVECHART/MEDIEVAL_AGE':[('the Medieval Age','the Age of Fins')],
 'ACHIEVECHART/GUNPOWDER_AGE':[('the Gunpowder Age','the Coal Forest Age')],
 'ACHIEVECHART/ENLIGHTENMENT_AGE':[('the Enlightenment Age','the Triassic Dawn')],
 'ACHIEVECHART/INDUSTRIAL_AGE':[('the Industrial Age','the Jurassic Heights')],
 'ACHIEVECHART/MODERN_AGE':[('the Modern Age','the Cretaceous Bloom')],
 'ACHIEVECHART/INFORMATION_AGE':[('the Information Age','the Cenozoic Rise')],
 'ACHIEVECHART/LIBRARY_RESEARCH':[('Library research','Fossil Record research')],
 'ACHIEVECHART/MISC_RESEARCH':[('non-Library research','non-Fossil Record research')],
 'STATS/ARMAGEDDONCLOCK':[('Whenever a nuclear weapon detonates','Whenever an Extinction Event strikes')],
}
# literal replacements applied to every STRING of a section
LITERAL_SEC={
 'GAMESPYQM':[('begin in the Ancient Age','begin in the Primordial Age'),('an Information Age Deathmatch','a Cenozoic Rise Deathmatch'),('No nuclear weapons or','No Extinction Events or')],
}
RULE_SECTIONS={'UNITS','BUILDINGS','TRIBES','LIBRARY','GOODS'}

def apply_rules(txt, rules):
    for p,r in rules: txt=p.sub(r,txt)
    return txt

def patch_help():
    p=V02+'/Data/help.xml'; s=rd(p)
    nl='\r\n' if '\r\n' in s else '\n'
    # top-level sections: lines "\t<NAME ...>"
    secs=[(m.start(),m.group(1)) for m in re.finditer(r'(?m)^\t<([A-Z0-9_]+)(?:\s[^>]*)?>\r?$',s)]
    ents=[(m.start(),m.group(1)) for m in re.finditer(r'<ENTRY name="([^"]*)"',s)]
    import bisect
    sp=[a for a,_ in secs]; ep=[a for a,_ in ents]
    out=[]; last=0; nstr=0
    for m in re.finditer(r'<STRING>(.*?)</STRING>',s,re.S):
        nstr+=1
        sec=secs[bisect.bisect_right(sp,m.start())-1][1]
        ent=ents[bisect.bisect_right(ep,m.start())-1][1]
        key=f'{sec}/{ent}'
        body=m.group(1)
        toks=re.split(r'(<!--.*?-->|<[^>]+>)',body,flags=re.S)
        new=list(toks)
        if sec=='LIBRARY' and ent in AGE_TEXT:
            # main text token = longest text token
            i=max(range(0,len(toks),2),key=lambda k: len(toks[k].strip()))
            t=toks[i]; lead=re.match(r'^\s*',t).group(0); trail=re.search(r'\s*$',t).group(0)
            new[i]=lead+AGE_TEXT[ent].replace('\n',nl)+trail
        else:
            for i in range(0,len(toks),2):
                t=toks[i]
                if sec in RULE_SECTIONS: t=apply_rules(t,R)
                if sec=='TIPS': t=apply_rules(apply_rules(t,R),T)
                for a,b in LITERAL.get(key,[])+LITERAL_SEC.get(sec,[]): t=t.replace(a,b)
                new[i]=t
        nb=''.join(new)
        if nb!=body:
            assert new[1::2]==toks[1::2]
            out.append(s[last:m.start(1)]); out.append(nb); last=m.end(1)
            changes.append(('help.xml',key,body,nb,'v0.2 help'))
    out.append(s[last:]); wr(p,''.join(out))
    # sanity: every LITERAL key hit
    hit={c[1] for c in changes}
    for k in LITERAL:
        if k not in hit: print('WARN literal not applied',k)

def patch_hash_file(fn, mapping, cat):
    p=V02+'/Data/'+fn; s=rd(p); seen=set()
    def f(m):
        h=m.group(2)
        if h in mapping:
            seen.add(h); old=m.group(4)
            new=mapping[h].replace('&','&amp;') if '&' in mapping[h] and '&amp;' not in mapping[h] else mapping[h]
            if new!=old: changes.append((fn,h,old,new,cat))
            return m.group(1)+new+m.group(5)
        return m.group(0)
    s=re.sub(r'(<STRING hash="(\d+)"([^>]*)>)([^<]*)(</STRING>)',f,s)
    wr(p,s)
    miss=set(mapping)-seen
    if miss: print('WARN missing hashes',fn,miss)

patch_help()
patch_hash_file('translated_strings.xml',TS,'v0.2 ui text')

with open(V02+'/changes-v0.2.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['file','id_or_hash','old_text','new_text','category'])
    for c in changes: w.writerow([c[0],c[1],c[2].replace('\r',''),c[3].replace('\r',''),c[4]])
print('changes',len(changes))
