from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import files


class driver_class:

    chrome_options = None
    def __init__(self):
        self.Driver = self.load_driver()


    def load_driver(self): 
        options = self.add_options()
        driver_path = files.get_driver_path()
        Driver = webdriver.Chrome(executable_path=driver_path , options= options)
        return Driver


    def add_options(self):
        chrome_options = Options()
        self.change_download_loc()
        return True


    def change_download_loc(self):
        download_dir  = files.get_video_dir()
        self.chrome_options.add_experimental_option('prefs', {'download.default_directory': download_dir})
        return True

