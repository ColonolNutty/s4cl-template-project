from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    """ Mod info for the S4CL Sample Mod. """
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        return 'S4CLSampleMod'

    @property
    def _author(self) -> str:
        return 'ColonolNutty'

    @property
    def _base_namespace(self) -> str:
        return 's4cl_sample_mod_scripts'

    @property
    def _file_path(self) -> str:
        return ModInfo._FILE_PATH
