import files
import driver_
import json
import time

class get_cookies:
    url = 'https://in.pinterest.com/idea-pin-builder/'

    def __init__(self):
        self.Driver = self.load_pintrest()

    def load_pintrest(self):
        print('loading driver please wait until login page appears and then login ')
        driver_obj = driver_.driver_class()
        Driver = driver_obj.load_driver()
        Driver.get(self.url)
        return Driver
    
    def download_cookies(self):
        cookies = self.Driver.get_cookies()
        cookies_file = files.get_cookies_file()
        with open(cookies_file, 'w') as f:
            json.dump(cookies, f)

    def login(self):
        permission = input('should we start downloding cookies  (0/1) :')
        if permission == 'y':
            self.download_cookies()
            time.sleep(10)
            self.Driver.quit()
        else:
            self.Driver.quit()


if __name__ == '__main__':
    cookies_obj = get_cookies()
    cookies_obj.load_pintrest()
        
