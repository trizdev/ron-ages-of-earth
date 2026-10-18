# mod

Mod files follow the game's mods folder layout (`Data/*.xml`, `tribes/*.xml`, `art/`).

## Current content: v0.2 text + scenery animal art

Copies of game files where only display text was changed (hashes, IDs and structure untouched; CRLF, no BOM):

- `Data/typenames.xml`, `Data/string_lookup.xml`, `Data/translated_strings.xml`, `Data/alternatenames.xml`, `Data/help.xml`: eras, units, buildings, wonders, resources, technologies, governments, biomes and scenery animals. v0.2 adds themed help and tips, era descriptions and the themed unit-class glossary (see `../docs/v0.2/`).
- `tribes/*.xml` and `*.xml.9`: short nation names for the nation list (unchanged since v0.1).

Art (overrides by file name, same case as the game's files):

- `art/`: 50 new model (`.BH3`) and texture (`.tga`) files for the 13 scenery animals. Each model keeps the original skeleton, so the game's animations still apply.
- `Data/unit_graphics.xml`: Wild Meso-herd scale 0.55, Bait Shoal belemnite/ammonite models per tileset, Steno-pod without the blowhole spout, Feather-bear on the peahen skeleton and animations, and the new snow models.

v0.1 text was tested in game on 2026-10-18. v0.2 text and the new art are not yet tested in game.

To test locally, copy `Data`, `tribes` and `art` into `Rise of Nations/mods/Ages of Earth/` and enable it under Tools & Extras > Steam Workshop. Restart the game after changes.

The RoN File Converter is not part of this mod.

Rise of Nations: Ages of Earth was created under Microsoft's "Game Content Usage Rules" using assets from Rise of Nations, © Microsoft Corporation.
