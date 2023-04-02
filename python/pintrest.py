import files
import driver_
import time


class upload_to_pintrest:
    url = 'https://in.pinterest.com/idea-pin-builder/'
    cookies = None

    def __init__(self):
        self.Driver = self.driver()

    def load_driver(self):
        driver_obj = driver_.driver_class()
        driver_obj.load_cookies()
        Driver = driver_obj.load_driver()
        driver_obj.add_cookies()
    
    def load_pintrest(self):
        self.Driver.get(self.url)
        time.sleep(100)
    



    

if __name__ == '__main__':
    pin_obj = upload_to_pintrest()
    pin_obj.load_pintrest()
