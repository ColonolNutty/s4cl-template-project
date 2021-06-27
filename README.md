# S4CL Template Project
This repository is meant to be a basic template you may use to start working with the [Sims 4 Community Library](https://github.com/ColonolNutty/Sims4CommunityLibrary) API.

A Basic Mod (S4CL Sample Mod) is included. If installed into your Mods folder, it will display a notification upon loading a household.

If a question has not been answered by the Wiki or you have further questions on how to setup the Template project, how to use S4CL, or how to make your own mod, feel free to join the [discord](https://discord.gg/fdCgyXkDZb)

Take a look at how to setup the Template Project to start working with it in the wiki [here](https://github.com/ColonolNutty/s4cl-template-project/wiki/Project-Setup)!

## Decompile EA Python Scripts.

1. Inside `<Project>/settings.py`, change `should_decompile_ea_scripts` to `True`
2. If it does not exist, create a folder in your project with the name `EA`. i.e. <Project>/EA
3. Run the `decompile_scripts.py` script
4. It will decompile the EA scripts and put them inside of the folder: `<Project>/EA/...`
5. Inside of the <Project>/EA folder, you should see four folders (base, core, generated, simulation)
6. In PyCharm, highlight all four folders (Not Zip files) (`base`, `core`, `generated`, `simulation`) and Right Click them -> `Mark Directory as...` -> `Sources Root`


## Decompile Scripts From Other Mods.

1. Inside `<Project>/settings.py`, change `should_decompile_ea_scripts` to `False`
2. Inside `<Project>/settings.py`, change `should_decompile_custom_scripts` to `True`
3. If it does not exist, create a folder in your project with the name `custom_scripts_for_decompile`. i.e. `<Project>/custom_scripts_for_decompile`
4. Put the script files (.pyc) of the mod you wish to decompile, inside of the `custom_scripts_for_decompile` folder. (Every ts4script file is a zip file and can be opened and extracted like one!)
5. Run the `decompile_scripts.py` script
6. It will decompile the custom scripts and put them inside of the folder: `<Project>/custom_scripts_for_decompile/_decompiled/...`