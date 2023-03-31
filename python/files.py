import os
import constants as const


def get_parent_dir(dir):
    full_path = os.path.dirname(dir)
    relative_path = convert_to_relative_path(full_path)
    return relative_path


def get_driver_dir():
    parent_dir = get_parent_dir(os.getcwd())
    driver_dir = os.path.join(parent_dir,const.DRIVER_DIR_NAME)
    return driver_dir


def get_driver_path():
    return os.path.join(get_driver_dir(),const.DRIVER_NAME)


def convert_to_relative_path(path):
    dir_path = os.path.dirname(path)
    relative_path = os.path.relpath(path, dir_path)
    return relative_path
