# Asteroids Deluxe for Analogue Pocket

+ FPGA implementation of Arcade _Asteroids Deluxe_ (Atari, 1981) for Analogue Pocket.
+ Ported from the [original MiSTer implementation.](https://github.com/MiSTer-devel/Arcade-AsteroidsDeluxe_MiSTer) 
+ Template and pocket core integration based on the Analogue Pocket port of [Asteroids by ericlewis](https://github.com/ericlewis/openfpga-asteroids).
+ Multiplayer support via dock.

Note:  File bugs for issues you encounter on the Github tracker.  Any issues are most likely with my integration, and not with the cores themselves.  Please do not engage the original core authors for support requests related to this port.

## Release Notes
v0.9.2
- Remove duplicate "Bonus" menu item in interact.json.

v0.9.1
- Added background image support, with toggle on/off from interact menu.

v0.9.0
- Initial Release

## ROM Instructions

ROM files are not included, you must use [mra-tools-c](https://github.com/sebdel/mra-tools-c/) to convert to a singular `astdelux.rom` file, then place the ROM file in `/Assets/astdelux/obsidian.AsteroidsDeluxe`.