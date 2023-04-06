# required packages
from . import driverr
from time import sleep
from selenium.webdriver.common.by import By
from . import files


class video_download_from_link:
    # declaring and initilizing variable to be used repeatedly
    site_url = 'https://saveinsta.app/en/instagram-reels-video-download'
    input_field_x_path = '/html/body/div[1]/div[1]/div/div/form/div/input'
    load_video_btn = '/html/body/div[1]/div[1]/div/div/form/div/div/button'
    ads_btn = '/html/body/div[2]/div/div[2]/button'
    links = []

    def __init__(self, reels_url):
        self.reels_url = reels_url
        self.Driver = self.load_driver()

    def load_driver(self):
        driver_obj = driverr.driver_class()
        download_loc = files.get_video_dir()
        driver_obj.change_download_loc(download_dir=download_loc)
        Driver = driver_obj.load_driver()
        return Driver

    # loading instagram reels downloder
    def load_site(self):
        self.Driver.get(self.site_url)
        return True

    def input_url(self):
        # finding input field by x-path
        input_field = self.Driver.find_element(By.XPATH,
                                               self.input_field_x_path)
        input_field.send_keys(self.reels_url)

    def load_video(self):
        download_btn = self.Driver.find_element(By.XPATH, self.load_video_btn)
        download_btn.click()

    def close_ad(self):
        close_ad_btn = self.Driver.find_element(By.XPATH, self.ads_btn)
        close_ad_btn.click()

    def fetch_download_link(self):
        # Find all elements with class name 'download-items__btn'
        elements = self.Driver.find_elements(By.CLASS_NAME,
                                             "download-items__btn")

        # Print the links inside the anchor tags for each element
        for element in elements:
            link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            self.links.append(link)

    def start_download(self):
        for i in self.links:
            self.Driver.get(i)

    def download_video(self):
        self.input_url()
        sleep(3)
        self.load_video()
        print('sleeping for 10 seconds')
        sleep(10)
        print('closing ads')
        self.close_ad()
        print('ads closed successfully')
        self.fetch_download_link()
        sleep(20)
        self.start_download()
        # sleep(20)
        print('driver ready to quit')
        print('sleepig for 300 seconds')
        sleep(30)
        print('sleping complete')
        self.Driver.quit()
        print('driver quit succeessfully')
        print('video download complete')
        return True


# test code
# if __name__ == '__main__':
#     reels_url = 'https://www.instagram.com/reel/CqS3YvEIDTO/?utm_source=ig_web_copy_link'
#     driver_obj = video_download_from_link(reels_url)
#     driver_obj.download_video()
