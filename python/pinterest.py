import files
import driver_
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class upload_to_pinterest:
    url = 'https://in.pinterest.com/idea-pin-builder/'
    cookies = None
    create_new_btn = '/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div/div[3]/div/button'
    file_input_field = '/html/body/div[4]/div/div/div[2]/div/div[3]/div/div[1]/div/input'
    publish_btn = '/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div/div[1]/div[3]/div[3]/div/button'
    stat_class ='zI7 iyn Hsu'
    driver_obj = driver_.driver_class()

    def __init__(self):
        self.Driver = self.load_driver()


    def load_driver(self):
        self.driver_obj.load_cookies(files.get_cookies_file())
        Driver = self.driver_obj.load_driver()
        return Driver
    

    def create_new(self):
        self.Driver.find_element(By.XPATH,self.create_new_btn).click()
        return True
    
    def input_video(self):
        video_files = files.get_video_files()
        # fetching only one video
        video_file = video_files[0]
        self.Driver.find_element(By.XPATH, self.file_input_field).send_keys(video_file)
        return True
    
    def publish_video(self):
        self.Driver.find_element(By.XPATH,self.publish_btn).click()
        return True
    
    def wait_for_upload(self):
        while True:
            try:
                self.Driver.find_elements(By.CLASS_NAME,self.stat_class)
                break
            except:
                pass
        return True
    

    def load_pinterest(self):
        self.Driver.get(self.url)
        sleep(10)
        print('adding cookies')
        self.driver_obj.add_cookies()
        print('cookies added')
        print('refreshing')
        self.Driver.refresh()
        sleep(10)
        self.Driver.get(self.url)
        sleep(30)

    def start_upload(self):
        self.create_new()
        sleep(20)
        self.input_video()
        sleep(20)
        self.publish_video()
        sleep(20)
        print('waiting for upload to complete')
        self.wait_for_upload()
        print('uploding completed')
        print('driver quitting in 30 seconds')
        sleep(30)
        self.Driver.quit()
        print('driver quit ')
    

# if __name__ == '__main__':
#     pin_obj = upload_to_pinterest()
#     pin_obj.load_pinterest()
#     pin_obj.start_upload()
