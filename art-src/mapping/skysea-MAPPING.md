# Sky & sea critters — file mapping (preview batch, nothing installed)
Source art: laptop `.../steamapps/common/Rise of Nations/art` (read-only tar `~/ron-model-test/skysea_src.tgz`, copied to `skysea/src/`).
All exports were converted with the RoN File Converter on the box (rebuilt from ptasev/Rise-of-Nations source into ~/opt/rfc, not redistributed)
and verified: converts OK, re-reads OK, same bone names and depth-first order as the original, rest-pose diff ≤ 4e-6, 1 bone per vertex.

| Game unit | New art file -> art/ | Built from | Tris (orig) | Texture -> art/ |
|---|---|---|---|---|
| WILDBIRD dirty + jungle | pterowing/export/bird_dirty.BH3 | bird_dirty skeleton | 122 (50) | bird_dirty.tga (brown), bird_amer.tga (green) |
| WILDBIRD snowy/arctic | pterowing/export/bird_snow.BH3 (same mesh) | bird_snow skeleton | 122 (50) | bird_snow.tga (light grey) |
| WILDBIRD savannah/GS | pterowing/export/bird_african.BH3 (same mesh) | bird_african skeleton | 122 (50) | bird_african.tga (sand) |
| FLOCKBIRD | ptero_flock/export/flock.BH3 | flock | 144 (64) | flock.tga, flock_african.tga |
| GULLBIRD | anhanguera/export/bird_gul.BH3 | bird_gul | 146 (50) | bird_gul.tga |
| HERDFISH Leptolepis | bait_shoal/export/fish1.BH3 + fish2.BH3 (same mesh) | fish1/fish2 | 160 (60) | fishherd.tga |
| HERDFISH belemnites | bait_shoal/export/fish_belem.BH3 (NEW file name) | fish skeleton | 180 (60) | fishherd_salmon.tga |
| HERDFISH ammonites | bait_shoal/export/fish_coil.BH3 (NEW file name) | fish skeleton | 130 (60) | fishherd_mahi.tga |
| HERDWHALES | stenopterygius/export/whale.BH3 | whale | 194 (140) | whale.tga (128²) |
| HERDSEALS | skipped: no unitrules.xml entry (TYPE2 even points texture at sealbrown.bh3) | | | |

Animations untouched (bird_flap/bird_soar, flock_move1/2, fish_swim1-3, whale_walk3 all play on the unchanged skeletons).

## Required unit_graphics.xml change for the fish (mod Data override)
Original fish1.bh3 and fish2.bh3 are identical meshes shared by all three fish textures, so belemnites/ammonites need their own models.
In HERDFISH-TYPE0, TYPE1 and TYPE2, set the model per tileset:
- DIRTY and the default: keep fish1.bh3 / fish2.bh3 (Leptolepis, fishherd.tga)
- SNOWY and ARCTIC: model=".\art\fish_belem.bh3" (texture stays fishherd_salmon.tga)
- AFRICAN_SAVANNAH, GS_DESERT and JUNGLE: model=".\art\fish_coil.bh3" (texture stays fishherd_mahi.tga)
Without this change, the salmon/mahi textures would land on the Leptolepis UVs and look scrambled.

## Optional XML notes
- HERDWHALES has PARTICLEEVENT WHALE_BLOWHOLE_BLOW (a spout). Ichthyosaurs had no blowhole; drop the line if the spout looks wrong.
- Scale is unchanged: WILDBIRD 1, GULLBIRD .5, whale 1.25.
