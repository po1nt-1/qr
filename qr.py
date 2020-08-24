import inspect
import os
import sys

import pyqrcode
import matplotlib
from matplotlib import pyplot


def get_script_dir(follow_symlinks=True):
    '''получить директорию со исполняемым скриптом'''
    # https://clck.ru/P8NUA
    if getattr(sys, 'frozen', False):  # type: ignore
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


if __name__ == "__main__":
    try:
        PATH = os.path.join(get_script_dir(), "QRCode.png")
        DATA = sys.argv
        if len(DATA) == 2:
            code = pyqrcode.create(DATA[1], encoding="utf-8")
            code.png(PATH, scale=15, quiet_zone=1)

            matplotlib.rcParams['toolbar'] = 'None'
            pyplot.imshow(pyplot.imread(PATH))
            pyplot.show()

            os.remove(PATH)
        else:
            DATA = input(":")
            if DATA == "":
                sys.exit("No output")
            code = pyqrcode.create(DATA, encoding="utf-8")
            code.png(PATH, scale=15, quiet_zone=1)

            matplotlib.rcParams['toolbar'] = 'None'
            pyplot.imshow(pyplot.imread(PATH))
            pyplot.show()

            os.remove(PATH)
    except KeyboardInterrupt:
        sys.exit("\nNo output")
        if os.path.exists(PATH):
            os.remove(PATH)

