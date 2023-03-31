import driver
from time import sleep
from selenium.webdriver.common.by import By

class instagram:
    # declaring and initilizing variable to be used repeatedly
    site_url = 'https://saveinsta.app/en/instagram-reels-video-download'
    input_field_x_path = '/html/body/div[1]/div[1]/div/div/form/div/input'
    load_video_btn = '/html/body/div[1]/div[1]/div/div/form/div/div/button'
    ads_btn = '/html/body/div[2]/div/div[2]/button'

    def __init__(self,reels_url):
        self.reels_url = reels_url
        self.Driver = self.load_site()
        

    def load_site(self):
        Driver = driver.load_driver()
        # navigatet to the instagram reels downloder website
        Driver.get(self.site_url)
        return Driver

    def input_url(self):
        # finding input field by x-path
        input_field = self.Driver.find_element(By.XPATH,self.input_field_x_path)
        input_field.send_keys(self.reels_url)

    def load_video(self):
        download_btn = self.Driver.find_element(By.XPATH,self.load_video_btn)
        download_btn.click()

    
    def close_ad(self):
        close_ad_btn = self.Driver.find_element(By.XPATH,self.ads_btn)
        close_ad_btn.click()


    def run_download(self):
        self.input_url()
        sleep(3)
        self.load_video()
        print('sleeping for 10 seconds')
        sleep(10)
        print('closing ads')
        self.close_ad()
        print('ads closed successfully')
        sleep(20)
        self.Driver.quit()
        print('driver quit succeessfully')

        

if __name__ == '__main__':
    reels_url = 'https://www.instagram.com/reel/CqS3YvEIDTO/?utm_source=ig_web_copy_link'
    main_obj = instagram(reels_url)
    main_obj.run_download()