# art-src

Working sources for the 13 scenery animals in `mod/art/`.

- `scripts/herds/`: headless Blender build scripts for Diictodon, Mesohippus, Leptoceratops and the Kannemeyeria bull (`bison2.py`).
- `scripts/skysea-bipeds/`: build scripts for the pterosaurs, fish shoals, Stenopterygius, Mei long, Caudipteryx and Beipiaosaurus (`bipeds.py`).
- `scripts/kannemeyeria/`: build, render and export scripts for the first Kannemeyeria.
- `mapping/`: which new file replaces which game file, verification results, and the required `unit_graphics.xml` changes.
- `<animal>/tex/`: source textures; `<animal>/export/`: Blender glTF exports and verification results; `<animal>/preview/`: final approved previews.

Run Blender headless: `blender -b --python <absolute path to script>`. Paths in the scripts are hard-coded to the original build machine (`/workspace/...`, `/home/box/opt/...`) and need adjusting.

The scripts call the RoN File Converter (ptasev) to turn glTF into BH3. The converter is **not** included here; download and build it yourself from its official source. Original game files (models, animations, textures) are not included either; extract them from your own game install.

Not included: Blender `.blend` work files (they embed original game meshes and textures for comparison), intermediate re-read files, and v1 drafts.
