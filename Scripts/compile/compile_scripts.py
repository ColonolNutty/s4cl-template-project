from Utilities.unpyc3_compiler import Unpyc3PythonCompiler

# This function invocation will compile the files found within Scripts/s4cl_sample_mod_scripts, put them inside of a file named s4cl_sample_mod.ts4script, and it will finally place that ts4script file within <Project>/Release/S4CLSampleMod.
Unpyc3PythonCompiler.compile_mod(
    names_of_modules_include=('s4cl_sample_mod_scripts',),
    folder_path_to_output_ts4script_to='..\\..\\Release\\S4CLSampleMod',
    output_ts4script_name='s4cl_sample_mod'
)