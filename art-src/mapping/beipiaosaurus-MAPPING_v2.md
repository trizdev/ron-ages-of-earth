# Beipiaosaurus v2 ("Feather-bear"): PREVIEW ONLY, nothing installed
This is still option (c): the model is on the PEAHEN skeleton and HERDBLACKBEAR is pointed at the Peahen animations. The XML plan is the same as v1.
Exports are in beipiaosaurus/export/ (the v1 files were moved to export_v1/, tex_v1/). Each was verified by re-reading the BH3:
bone names and order are the same as peahen, max rest-pose difference is 1.1e-5, there is 1 bone per vertex (multi_weight 0), and the mesh is triangulated.

| Game file (art\) | Box source | Tris | Notes |
|---|---|---|---|
| blackbear.bh3 | export/blackbear.BH3 | 400 | adult |
| blackbear_cub.bh3 | export/blackbear_cub.BH3 | 400 | cub: head x1.3, slimmer, shorter claws, fuzzier; XML scale 1 |
| blackbear_snowy.bh3 (NEW) | export/blackbear_snowy.BH3 | 400 | arctic adult, thicker coat (fluff 1.5) |
| blackbear_cub_snowy.bh3 (NEW) | export/blackbear_cub_snowy.BH3 | 400 | arctic cub (uses blackbear_snowy.tga) |
| blackbear.tga / blackbear2.tga / blackbear_cub.tga / blackbear_snowy.tga | export/ | - | 128x128 RLE TGA (each about 50-58 KB) |
Original poly counts for reference: bear 168 tris, peahen 134. v1 was 291.

XML: xml_v2/unit_graphics.xml and xml_v2/unit_graphics.diff are built on /workspace/herds-install/Data/unit_graphics.xml as it is now (mtime 18:28).
The result is byte-identical to the v1 XML because the base file has not changed. 27 lines change, all inside HERDBLACKBEAR-TYPE0..2: ANIM BlackBear Default/Idle1/Idle2/Idle3/Walk ->
Peahen Default/Idle1/Idle2/Idle1/Walk; ARCTIC models -> blackbear_cub_snowy.bh3 / blackbear_snowy.bh3; scale .75->1 (cub) and 1->1.3 (adults); Horse Shadow -> Biped Shadow.
The file parses, quotes are balanced, there are no curly quotes, and CRLF line endings are kept. anim_graphics.xml needs no change.

Changes since v1: there is a new soft, mottled filament coat made of short jittered strokes (no long grain). The back is dark brown and fades to a tan-grey belly; the snow coat is pale cream-grey.
The back spikes are gone. Shag now comes from the texture, a few low, flat, ragged tufts along the neck, a short shaggy tail end, and low hem tufts on the belly, thighs and shoulders.
The body is bigger and pot-bellied, with wider hips, heavy thighs and thick shins. The neck is thick at the base and the head is small, with a flat, leaf-shaped, down-turned horn beak.
The arms hang forward with shaggy upper arms and three long curved claws. The tail is short.
Code: skysea/scripts/bipeds.py (beipiao2, fuzz, bei2_coat, CREATURES['beipiaosaurus_v2']); a snapshot is in v2_src.tgz.
