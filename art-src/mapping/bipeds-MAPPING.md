# Bipeds batch – Mei long / Caudipteryx / Beipiaosaurus (PREVIEW ONLY, nothing installed)

All exports: original skeleton kept (bone names, order, rest pose verified by BH3 re-read; max rest diff <=1.2e-5),
1 bone per vertex (multi_weight 0), single 128x128 RLE TGA, triangulated.

| Game file (art\) | Source on box | Skeleton | Tris (orig) |
|---|---|---|---|
| hen.bh3 | mei_long/export/hen.BH3 | hen | 166 (36) |
| rooster.bh3 | mei_long/export/rooster.BH3 | rooster | 168 (38) |
| fowls.tga | mei_long/export/fowls.tga (hen left half, rooster right half) | – | 128² (orig 64²) |
| peacock.bh3 | caudipteryx/export/Peacock.BH3 (male) | peacock | 186 (135) |
| peahen.bh3 | caudipteryx/export/Peahen.BH3 (female) | peahen | 186 (134) |
| peafowl.tga | caudipteryx/export/peafowl.tga (male left, female right) | – | 128² (orig 128²) |
| blackbear.bh3 | beipiaosaurus/export/blackbear.BH3 | **PEAHEN** | 291 (bear 168) |
| blackbear_cub.bh3 | beipiaosaurus/export/blackbear_cub.BH3 | **PEAHEN** | 291 |
| blackbear_snowy.bh3 (NEW) | beipiaosaurus/export/blackbear_snowy.BH3 | **PEAHEN** | 291 |
| blackbear_cub_snowy.bh3 (NEW) | beipiaosaurus/export/blackbear_cub_snowy.BH3 | **PEAHEN** | 291 |
| blackbear.tga / blackbear2.tga / blackbear_cub.tga / blackbear_snowy.tga | beipiaosaurus/export/ | – | 128² (orig 64²) |

No XML change is needed for FARMCHICKEN and HERDPEACOCKS (same file names and animations).

## HERDBLACKBEAR XML (required; the models are on the peahen skeleton)
Built on /workspace/herds-install/Data/unit_graphics.xml (current mod version). Result: bipeds/xml/unit_graphics.xml; diff: bipeds/xml/unit_graphics.diff.
Parses as XML, quotes balanced on every line, no curly quotes, CRLF line endings and byte count otherwise unchanged. 27 lines changed, all inside HERDBLACKBEAR-TYPE0..2:
- ANIM: BlackBear Default→Peahen Default, Idle1→Peahen Idle1, Idle2→Peahen Idle2, Idle3→Peahen Idle1, Walk→Peahen Walk.
  The existing CHAR_* slots are kept, so: IDLE1 = browse (Peahen Idle2), IDLE2/IDLE3 = arm/claw threat display (Peahen Idle1 wing-flap), SLOG/WALK/JOG = Peahen Walk.
- ARCTIC model: TYPE0 → blackbear_cub_snowy.bh3, TYPE1/2 → blackbear_snowy.bh3 (texture stays blackbear_snowy.tga).
- scale: TYPE0 .75→1, TYPE1/2 1→1.3. The peahen-sized body is about 22 units long against the bear's 36; at 1.3 it is about 29 long and 29 tall.
- shadowtype Horse Shadow→Biped Shadow (same width/height).
anim_graphics.xml: no change (the Peahen entries already exist).

## Bear option decision
- (a) Bear skeleton: rejected. The bear walk is quadrupedal, so a biped therizinosaur would walk on all fours with its arms as legs.
  It looked wrong in analysis, so I didn't build a full prototype of it.
- (b) New skeleton plus new BHa: technically possible (the converter writes BHa from glTF), but it would mean hand-animating 5 clips. Not done.
- (c) CHOSEN: rebuild the model on the peahen skeleton and point HERDBLACKBEAR at the existing Peahen animations. The result is a true biped with a real walk, browse and an arm display.

## Compromises / risks (need an in-game test)
- Bear→peahen animation swap: animations are bone-order based and the unit has no skeleton= attribute, so it should work, but this is not yet tested in-game.
- Foot sliding is possible: the peahen stride x1.3 against the bear's move speed.
- The walk is bird-like: fast, with a level body.
- Bird skeletons force long necks (the rooster head bone is about 8 units above the body). Moving the head lower detached it during peck animations, so the head stays at the bone. Mei long and Caudipteryx necks are longer than real.
- Poly counts are above the originals: Mei long is about 4.5x the original (166-168 against 36-38); still small.
- The cub shares the adult UV layout (it only uses a different texture and proportions). The snow models are new files.
- The fan feathers are separate planes, and they spread nicely in peacock idle3.
- Bear textures are 128² instead of 64².
