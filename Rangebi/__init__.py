import os
import platform
import colorama


class Rangebi:

    if platform.system() == 'Windows':
        colorama.init()

    # colour constants
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def text_danger(self, message):
        return Rangebi.FAIL + str(message) + Rangebi.ENDC

    def text_warning(self, message):
        return Rangebi.WARNING + str(message) + Rangebi.ENDC

    def text_bold(self, message):
        return Rangebi.BOLD + str(message) + Rangebi.ENDC

    def text_success(self, message):
        return Rangebi.OKGREEN + str(message) + Rangebi.ENDC

    def text_info(self, message):
        return Rangebi.OKBLUE + str(message) + Rangebi.ENDC
