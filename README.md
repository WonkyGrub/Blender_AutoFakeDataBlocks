# Blender_AutoFakeDataBlocks
Barebones blender add-on to automatically create fake user for chosen data types on save, or with a command.

Confirmed Working in Blender Alpha 4.2.0

**All datablock types are on by defualt, as well as set fake user on save. This add on will cause blender files to be larger due to more data being kept that would be purged otherwise. The amount of increase depends on an individuals usage.**

Heavily based on an amalgomation of code by [[https://blender.stackexchange.com/users/1363/codemanx|CodeManX]] [[https://blender.stackexchange.com/questions/9289/fake-user-on-by-default-in-blender-materials-and-textures|here]]. And [[https://github.com/TheKenetics|TheKinetics]] addon [[https://github.com/TheKenetics/SetAllFakeUsers2.8|here]].

# Why
Because I got annoyed manually doing it to prevent data from being lost. 

# Features

Setting fake users for these datablocks:

- Brush
- Camera
- Curve
- Font
- Image
- Light
- Lattice
- Mask
- Material
- Mesh
- Metaball
- Movieclip
- Node Group
- Object
- Particle
- Texture
- World

Toggleable auto set fake user feature, with preferences options to choose which datablocks, as well as a command to set fake users using your preferences, or manually choosing.

# Installation

Download python file, go into blender settings > add-ons in preferences, install from file and choose the python file you just downloaded.

Enable the add on, add on preferences can be found within its add-on dropdown panel, all datablocks are on by default, along with running on auto save. 


#Note

When an action to fake user data blocks is run, the visual indicators will not automatically update - simply move the cursor or interact with UI where it would appear, and it should update to show.
