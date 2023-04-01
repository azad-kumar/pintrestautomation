from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import files


class driver_class:
    download_dir = None
    cookies = None

    chrome_options = Options()

    def __init__(self):
        pass

    def load_driver(self): 
        driver_path = files.get_driver_path()
        Driver = webdriver.Chrome(executable_path=driver_path , options=self.chrome_options)
        return Driver

    
    def add_features(self):
        # lol no idea why i created this function
        pass


    def change_download_loc(self, download_dir):
        self.download_dir = download_dir
        self.chrome_options.add_experimental_option('prefs', {'download.default_directory': download_dir})
        return True
    
    def add_cookies(self,cookies):
        self.cookies = cookies 
        for cookie in cookies:
            self.driver.add_cookie(cookie)

