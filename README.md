## S4CL Sample Mod
This is a basic mod utilizing the Sims 4 Community Library by ColonolNutty: https://github.com/ColonolNutty/Sims4CommunityLibrary

If installed into your Mods folder, it will display a notification upon loading a household.

This project may be used as a template for which you may create your own mods (If you have any questions, feel free to join the [discord](https://discord.gg/p9Kc287) and ask them there!)

In order to set the project up for use as a template for your own mod, take the following steps:
1. Remove the the `Scripts/S4CLSampleModScripts/s4cl_sample_mod_scripts` python package and create your own python package in its place.
2. Update the `Scripts/S4CLSampleModScripts/compile_scripts.py` file to point at your newly created python package.
3. Rename the `Scripts/S4CLSampleModScripts` folder however you'd like (Be sure to update the `/compile_scripts.py` file from step 2 AND set the new folder as a Source Root (Right-click -> Mark directory as... Source Root))
4. Remove the `Release/S4CLSampleMod` folder and create a folder with a name that matches the name used inside `/compile_scripts.py` from step 2
5. Copy the [S4CL scripts](https://github.com/ColonolNutty/Sims4CommunityLibrary/tree/master/Scripts/sims4communitylib) and place them inside the `Scripts/ScriptLibrary` folder overwrite if it exists already.
6. Update the `settings.py` file with details about your mod and the location of your The Sims 4 directory.