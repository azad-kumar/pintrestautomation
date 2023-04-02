from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import files
import json


class driver_class:
    download_dir = None
    cookies = None
    Driver = None
    chrome_options = Options()

    def __init__(self):
        pass


    def load_driver(self): 
        driver_path = files.get_driver_path()
        Driver = webdriver.Chrome(executable_path=driver_path , options=self.chrome_options)
        self.Driver = Driver
        return Driver

    
    def add_features(self):
        # lol no idea why i created this function
        pass

    # function should be called before loading the driver
    def change_download_loc(self, download_dir):
        self.download_dir = download_dir
        self.chrome_options.add_experimental_option('prefs', {'download.default_directory': download_dir})
        return True
    
    # function should be called after loading the driver
    def add_cookies(self,cookies):
        self.cookies = cookies 
        for cookie in cookies:
            self.Driver.add_cookie(cookie)

    # function should be called before loading the driver
    def load_cookies(self, cookies_file):
        with open(cookies_file, 'r') as f:
            cookies = json.load(f)
        return cookies
