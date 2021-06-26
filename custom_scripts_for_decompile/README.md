This folder is where you place `.pyc` files to be decompiled when running `decompile_scripts.py`

## Decompile Scripts From Other Mods.

1. Inside `<Project>/settings.py`, change `should_decompile_ea_scripts` to `False`
2. Inside `<Project>/settings.py`, change `should_decompile_custom_scripts` to `True`
2. If it does not exist, create a folder in your project with the name `decompiled`. i.e. `<Project>/custom_scripts_for_decompile`
3. Put the script files (.pyc) of the mod you wish to decompile, inside of the `decompiled` folder. (Every ts4script file is a zip file and can be opened and extracted like one!)
4. Change should_decompile_custom_scripts to True
5. Run the `decompile.py` script
6. It will decompile the custom scripts and put them inside of the folder: `<Project>/custom_scripts_for_decompile/...`