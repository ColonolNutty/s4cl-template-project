This folder will be where the decompiled EA python scripts will be placed when running `decompile_scripts.py` with `should_decompile_ea_scripts` set to `True`

# Decompile EA Python Scripts.

1. Inside `<Project>/settings.py`, change `should_decompile_ea_scripts` to `True`
2. If it does not exist, create a folder in your project with the name `EA`. i.e. <Project>/EA
3. Run the `decompile_scripts.py` script
4. The script will decompile the EA python scripts and put them inside of this folder: `<Project>/EA/...`
5. After the script finishes running, look inside of the `<Project>/EA` folder, you should see four folders (`base`, `core`, `generated`, `simulation`) and four zip files (`base.zip`, `core.zip`, `generated.zip`, `simulation.zip`)
6. In PyCharm, highlight all four folders (Not Zip files) (`base`, `core`, `generated`, `simulation`) and Right Click them -> `Mark Directory as...` -> `Sources Root`
7. The folders should now be `BLUE` in color, if they are not `BLUE`, repeat step the previous step.
8. Delete the `<Project>/EA/core/enum.py` file, it causes issues when attempting to compile the scripts of your own mod using `compile_scripts.py`.