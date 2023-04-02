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
        print('sleeping for 10 seconds')
        time.sleep(10)
        print('adding cookies')
        self.driver_obj.add_cookies()
        print('cookies added')
        print('refreshing')
        self.Driver.refresh()
        print('sleeping for 100 seonds')
        time.sleep(100)
        print('driver will be closed in 10 seconds')
        time.sleep(10)
        self.Driver.quit()
    



    

if __name__ == '__main__':
    pin_obj = upload_to_pintrest()
    pin_obj.load_pintrest()
