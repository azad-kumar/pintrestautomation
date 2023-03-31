import os
import constants as const
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
    cwd = os.getcwd()
    print(cwd)


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
    

if __name__ == '__main__':
    print(get_driver_dir())