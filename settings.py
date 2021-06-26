import os

# This name will be appended to the front of compiled scripts
# Example:
# If I set the value to "ColonolNutty"
# compiling my scripts would output a file with the name "ColonolNutty_<script_name>.ts4script"
creator_name = ''

# If this path is not correct, change it to your Mods folder location instead.
if os.name != 'nt':
    # Mac
    mods_folder = os.path.join(os.environ['HOME'], 'Documents', 'Electronic Arts', 'The Sims 4', 'Mods')
    print('Mods folder path: {}'.format(mods_folder))
else:
    # Windows
    mods_folder = os.path.join(os.environ['USERPROFILE'], 'Documents', 'Electronic Arts', 'The Sims 4', 'Mods')
    print('Mods folder path: {}'.format(mods_folder))

# Location of the game's zipped binary scripts (base.zip, core.zip and simulation.zip)
# If this path is not found properly when trying to decompile, change it to the location where you have installed The Sims 4 at, this would be the folder that contains the GameVersion.txt file
if os.name != 'nt':
    # Mac
    game_folder = os.path.join(os.environ['HOME'], 'Applications', 'The Sims 4.app', 'Contents', 'Data', 'Simulation', 'Gameplay')
    print('Mods folder path: {}'.format(mods_folder))
else:
    # noinspection PyBroadException
    try:
        # Windows
        import winreg as winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Maxis\\The Sims 4")
        (game_folder, _) = winreg.QueryValueEx(key, "Install Dir")
        print('Installation path: {}'.format(game_folder))
    except:
        game_folder = ''

# Set to either 'unpyc3' or 'py37dec' (py37dec is the default, however if it fails to decompile some files, feel free to change this to 'unpyc3' and try to decompile using that decompiler instead)
compiler_name = 'py37dec'

# If you want to decompile the EA Python Scripts:
# 1. Change include_ea_decompile to True
# 2. Create a folder in your project with the name EA. i.e. <Project>/EA
# 2. Run the decompile_all.py script
# 3. It will decompile the EA scripts and put them inside of the folder: <Project>/EA/...
# 4. Inside of the <Project>/EA folder, you should see four folders (base, core, generated, simulation)
# 5. Highlight all four of those folders and right click them. Then do Mark Directory as... Sources Root
# 6. Delete the <Project>/EA/core/enum.py file because it causes issues when attempting to compile the scripts of your own mod.
include_ea_decompile = True

# If you want to decompile scripts from another authors mod
# 1. Create a folder in your project with the name decompiled. i.e. <Project>/decompiled
# 1. Put the script files (.pyc) of the mod you wish to decompile, inside of the "decompiled" folder. (Every ts4script file is a zip file and can be opened like one!)
# 2. Change include_decompile_dir to True
# 3. Run the decompile_all.py script
# 4. It will decompile the custom scripts and put them inside of the folder: <Project>/decompiled/...
include_decompile_dir = True
if include_ea_decompile:
    compiler_name = 'unpyc3'
    include_decompile_dir = False

decompile_src = './decompiled'
decompile_destination = './decompiled'
