# Asteroids Deluxe for Analogue Pocket

+ FPGA implementation of Arcade _Asteroids Deluxe_ (Atari, 1981) for Analogue Pocket.
+ Ported from the [original MiSTer implementation.](https://github.com/MiSTer-devel/Arcade-AsteroidsDeluxe_MiSTer) 
+ Template and pocket core integration based on the Analogue Pocket port of [Asteroids by ericlewis](https://github.com/ericlewis/openfpga-asteroids).
+ Multiplayer support via dock.

## ROM Instructions

ROM files are not included, you must use [mra-tools-c](https://github.com/sebdel/mra-tools-c/) to convert to a singular `astdelux.rom` file, then place the ROM file in `/Assets/astdelux/obsidian.AsteroidsDeluxe`.