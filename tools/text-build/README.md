# text-build

Scripts that produced the v0.2 text (`mod/Data`, `mod/tribes`) from v0.1.

- `build_v02.py`: copies v0.1 `Data/` and `tribes/` and applies the rules in `help_rules.py` and `ts_map.py`. Rerunning it rebuilds v0.2 from v0.1, so manual edits made directly in the v0.2 files would be lost.
- `verify.py`: checks XML parsing, byte-identity outside `<STRING>` text, CRLF, no BOM and preserved `$`/`#ICON`/`%` tokens.
- `source-v0.1-sha256.txt`: hashes of the v0.1 inputs.

Note: the paths are hard-coded to the original build machine (`/workspace/ages-of-earth-mod/v0.1` and `/workspace/ages-of-earth-mod/v0.2`). Adjust them before running elsewhere.
