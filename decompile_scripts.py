import os

from decompilation_method import S4PyDecompilationMethod
from settings import custom_scripts_for_decompile_source, game_folder, decompile_method_name, custom_scripts_for_decompile_destination, should_decompile_ea_scripts, should_decompile_custom_scripts


def _remove_files_conflicting_with_decompile(decompile_ea_scripts: bool=False):
    ea_folder = 'EA'
    if not os.path.exists(ea_folder):
        os.mkdir(ea_folder)

    if decompile_ea_scripts:
        print('Removing EA decompiled files before decompiling it again.')
        to_remove_before_compile = (
            'base',
            'base.zip',
            'core',
            'core.zip',
            'generated',
            'generated.zip',
            'simulation',
            'simulation.zip',
        )

        def _remove_directory_recursive(directory_path: str):
            for _file_in_dir in os.listdir(directory_path):
                _to_remove_path = os.path.join(directory_path, _file_in_dir)
                if os.path.isdir(_to_remove_path):
                    # noinspection PyBroadException
                    try:
                        os.rmdir(_to_remove_path)
                    except:
                        _remove_directory_recursive(_to_remove_path)
                        os.rmdir(_to_remove_path)
                else:
                    os.remove(_to_remove_path)

        for to_remove in to_remove_before_compile:
            to_remove_path = os.path.join(os.getcwd(), ea_folder, to_remove)
            if not os.path.exists(to_remove_path):
                print(f'Did not exist \'{to_remove_path}\'')
                continue
            if os.path.isdir(to_remove_path):
                # noinspection PyBroadException
                try:
                    os.rmdir(to_remove_path)
                except:
                    _remove_directory_recursive(to_remove_path)
                    os.rmdir(to_remove_path)
            else:
                os.remove(to_remove_path)
    else:
        print('Renaming enum.py to enum.py_renamed')

        to_fix_before_decompile = (
            os.path.join('core', 'enum.py'),
            os.path.join('core', 'enum.pyc'),
        )

        for to_fix in to_fix_before_decompile:
            to_fix_path = os.path.join(os.getcwd(), ea_folder, to_fix)
            if not os.path.exists(to_fix_path):
                print(f'Did not exist \'{to_fix_path}\'')
                continue
            if os.path.isdir(to_fix_path):
                os.rename(to_fix_path, to_fix_path + '_renamed')
            else:
                os.rename(to_fix_path, to_fix_path + '_renamed')


def _replace_renamed_files(decompile_ea_scripts: bool=False):
    if decompile_ea_scripts:
        return

    print('Renaming enum.py_renamed to enum.py')

    ea_folder = 'EA'
    to_fix_after_decompile = (
        os.path.join('core', 'enum.py_renamed'),
        os.path.join('core', 'enum.pyc_renamed'),
    )

    for to_fix in to_fix_after_decompile:
        to_remove_path = os.path.join(os.getcwd(), ea_folder, to_fix)
        if not os.path.exists(to_remove_path):
            print(f'Did not exist \'{to_remove_path}\'')
            continue
        if os.path.isdir(to_remove_path):
            os.rename(to_remove_path, to_remove_path.rstrip('_renamed'))
        else:
            os.rename(to_remove_path, to_remove_path.rstrip('_renamed'))


def _decompile_using_unpyc3(decompile_ea_scripts: bool=False, decompile_custom_scripts: bool=False):
    output_folder = 'EA'
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    _remove_files_conflicting_with_decompile(decompile_ea_scripts=decompile_ea_scripts)

    from Utilities.unpyc3_decompiler import Unpyc3PyDecompiler

    if decompile_custom_scripts:
        Unpyc3PyDecompiler.decompile_folder(custom_scripts_for_decompile_source)

    if decompile_ea_scripts:
        gameplay_folder_data = os.path.join(game_folder, 'Data', 'Simulation', 'Gameplay')
        if os.name != 'nt':
            gameplay_folder_game = os.path.join(game_folder, 'Python')
        else:
            gameplay_folder_game = os.path.join(game_folder, 'Game', 'Bin', 'Python')

        Unpyc3PyDecompiler.extract_folder(output_folder, gameplay_folder_data)
        Unpyc3PyDecompiler.extract_folder(output_folder, gameplay_folder_game)

    _replace_renamed_files(decompile_ea_scripts=should_decompile_ea_scripts)


def _decompile_using_py37dec() -> None:
    _remove_files_conflicting_with_decompile(decompile_ea_scripts=should_decompile_ea_scripts)

    from py37_decompiler import Py37PythonDecompiler
    Py37PythonDecompiler().decompile(
        custom_scripts_for_decompile_source,
        custom_scripts_for_decompile_destination
    )
    _replace_renamed_files(decompile_ea_scripts=should_decompile_ea_scripts)


if decompile_method_name == S4PyDecompilationMethod.UNPYC3:
    _decompile_using_unpyc3(decompile_ea_scripts=should_decompile_ea_scripts, decompile_custom_scripts=should_decompile_custom_scripts)
elif decompile_method_name == S4PyDecompilationMethod.PY37DEC:
    _decompile_using_py37dec()
