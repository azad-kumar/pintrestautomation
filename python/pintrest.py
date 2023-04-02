import files
import driver_
import time


class upload_to_pintrest:
    url = 'https://in.pinterest.com/idea-pin-builder/'
    cookies = None
    driver_obj = driver_.driver_class()

    def __init__(self):
        self.Driver = self.load_driver()


    def load_driver(self):
        self.driver_obj.load_cookies(files.get_cookies_file())
        Driver = self.driver_obj.load_driver()
        return Driver
    

    def load_pintrest(self):
        self.Driver.get(self.url)
        time.sleep(10)
        print('adding cookies')
        self.driver_obj.add_cookies()
        print('cookies added')
        print('refreshing')
        self.Driver.refresh()
        time.sleep(10)
        self.Driver.get(self.url)
        time.sleep(100)
        print('driver ready to QUIT')
        self.Driver.quit()
        print('drvier quit successfully')
    



    

if __name__ == '__main__':
    pin_obj = upload_to_pintrest()
    pin_obj.load_pintrest()
