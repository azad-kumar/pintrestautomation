from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import os


class driver_class:
    download_dir = None
    cookies = None
    Driver = None
    chrome_options = Options()

    def __init__(self):
        pass


    def load_driver(self): 
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        Driver = webdriver.Chrome(options = self.chrome_options)
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

    # function should be called before loading the driver
    def load_cookies(self, cookies_file):
        self.cookies = json.loads(os.getenv('cookies'))
        return True

    # function should be called after loading the driver
    def add_cookies(self):
        for cookie in self.cookies:
            self.Driver.add_cookie(cookie)



