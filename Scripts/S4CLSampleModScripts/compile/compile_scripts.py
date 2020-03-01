from Utilities.compiler import compile_module


# This will compile the files found within S4CLSampleModScripts/s4cl_sample_mod_scripts and put them inside of a file named s4cl_sample_mod.ts4script
compile_module(
    root='..\\..\\..\\Release\\S4CLSampleMod',
    mod_scripts_folder='..',
    include_folders=('s4cl_sample_mod_scripts',),
    mod_name='s4cl_sample_mod'
)
