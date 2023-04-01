import files
import driver_
import json

class upload_to_pintrest:
    url = 'https://in.pinterest.com/idea-pin-builder/'

    def __init__(self):
        self.Driver = self.load_driver()

    def load_pintrest(self):
        driver_obj = driver_.driver_class()
        Driver = driver_obj.load_driver()
        Driver.get(self.url)
        return Driver
    
    def load_cookies(self):
        cookies = self.Driver.get_cookies()
        cookies_file = files.get_cookies_file()
        with open(cookies_file, 'w') as f:
            json.dump(cookies, f)