# Info

This script is used to create .scummvm files.

These files are used by Libretro's ScummVM core to run the ScummVM games.
More information about this in the [ScummVM section of Libretro Docs](https://docs.libretro.com/library/scummvm/).

# Usage

## Pre-requisites

Your scummvm.ini file should have all the desired games listed.

To do this just open the ScummVM core in Retroarch and add all the games from there, then exit.
*Hint: press the Shift key to "Mass Add" games from a parent folder.*

There is an example of this configuration file in this repository.

## Executing the script

You must run the script with one argument. This argument must be your "scummvm.ini" file, with full path. Like this:

```
python LB_scummvm.py "D:\LaunchBox\Emulators\RetroArch-Win64\system\scummvm.ini"
```

# Importing to LaunchBox

Import the *.scummvm files to your LaunchBox as ROM Files.

Selecting the ScummVM platform and Retroarch emulator should be enough to make the games run correctly.

Of course, you should make sure that your Retroarch emulator has the "scummvm_libretro" core associated to the ScummVM platform.
