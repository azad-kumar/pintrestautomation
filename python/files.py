import os
import constants as const


def get_parent_dir(dir):
    return os.path.dirname(dir)


def get_driver_dir():
    parent_dir = get_parent_dir(os.getcwd())
    driver_dir = os.path.join(parent_dir,const.DRIVER_DIR_NAME)
    return driver_dir


def get_driver_path():
    return os.path.join(get_driver_dir(),const.DRIVER_NAME)





