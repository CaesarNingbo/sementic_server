from os import getcwd, makedirs
from os.path import abspath, join, exists


class SystemInfo(object):
    """
    系统内部配置信息
    """

    _instance = None  # 单例模式-用来存放实例

    def __init__(self, is_test=False):
        if is_test:
            self.base_path = join(abspath(getcwd()), "..", "..")
        else:
            self.base_path = join(abspath(getcwd()), "sementic_server")

        self.base_log_path_corr = join(self.base_path, "output", "correction_record")
        if not exists(self.base_log_path_corr):
            makedirs(self.base_log_path_corr)
        self.log_path_corr = join(self.base_log_path_corr, "record.log")
