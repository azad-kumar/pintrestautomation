import os
from  . import constants as const
import shutil


def get_parent_dir(dir):
    full_path = os.path.dirname(dir)
    relative_path = convert_to_relative_path(full_path)
    return relative_path


def get_driver_dir():
    parent_dir = get_parent_dir(os.getcwd())
    return os.path.join(parent_dir,const.DRIVER_DIR_NAME)


def get_driver_path():
    return os.path.join(get_driver_dir(),const.DRIVER_NAME)


def get_video_dir():
    parent_dir = os.path.dirname(os.getcwd())
    video_dir = os.path.join(parent_dir, const.VIDEO_DIR)
    return video_dir


def get_video_files():
    videos = []
    files = os.listdir(get_video_dir())
    for i in files:
        videos.append(os.path.join(get_video_dir(),i))
    return videos

def get_cookies_dir():
    parent_dir = os.path.dirname(os.getcwd())
    cookies_dir = os.path.join(parent_dir, const.COOKIES_DIR)
    return cookies_dir


def get_cookies_file():
    cookies_dir = get_cookies_dir()
    return os.path.join(cookies_dir,const.COOKIES_FILE)


def convert_to_relative_path(path):
    dir_path = os.path.dirname(path)
    relative_path = os.path.relpath(path, dir_path)
    return relative_path


def give_next_file(directory):
    def get_last_file(directory):
        files = os.listdir(directory)
        if len(files) == 0:
            return False
        files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)))
        last_file_name = files[-1]
        return os.path.splitext(last_file_name)[0]
    
    last_file = get_last_file(directory)
    if last_file:
        last_file = last_file + "1"
    else:
        last_file = os.path.basename(directory)
        
    return last_file
    
    
def clear_directory(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
    
def delete_video():
    clear_directory(get_driver_dir())

