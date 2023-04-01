
# required packages
import driver_ as driver
from time import sleep
from selenium.webdriver.common.by import By


class video_download_link:
    # declaring and initilizing variable to be used repeatedly
    site_url = 'https://saveinsta.app/en/instagram-reels-video-download'
    input_field_x_path = '/html/body/div[1]/div[1]/div/div/form/div/input'
    load_video_btn = '/html/body/div[1]/div[1]/div/div/form/div/div/button'
    ads_btn = '/html/body/div[2]/div/div[2]/button'
    links = []

    def __init__(self,reels_url):
        self.reels_url = reels_url
        self.Driver = self.load_site()
        

    def load_site(self):
        driver_obj  = driver.driver_class()
        Driver = driver_obj.load_driver()
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

    def fetch_download_link(self):
        # Find all elements with class name 'download-items__btn'
        elements = self.Driver.find_elements(By.CLASS_NAME, "download-items__btn")

        # Print the links inside the anchor tags for each element
        for element in elements:
            link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            self.links.append(link)

    def start_download(self):
        for i in self.links:
            self.Driver.get(i)


    def get_video_download_links(self):
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
        sleep(20)
        print('driver ready to quit')
        sleep(30)
        self.Driver.quit()
        print('driver quit succeessfully')
        print('video download complete')
        return self.links



if __name__ == '__main__':
    reels_url = 'https://www.instagram.com/reel/CqS3YvEIDTO/?utm_source=ig_web_copy_link'
    driver_obj = video_download_link(reels_url)
    links = driver_obj.get_video_download_links()
    # links = ['https://download.i-7-cdn.xyz/ig/1680248789/3d0be84d078fa4a8924db0d193b40958dc3020f803f1659832da7e9806c5a47e?file=aHR0cHM6Ly9zY29udGVudC5jZG5pbnN0YWdyYW0uY29tL3YvdDY2LjMwMTAwLTE2LzMxODE4MDEwN183NDU0NjY5MDcwNTUyNDJfNjU1NzE1NTk1ODc2MTcwMTA0OV9uLm1wND9fbmNfaHQ9c2NvbnRlbnQuY2RuaW5zdGFncmFtLmNvbSZfbmNfY2F0PTEwNiZfbmNfb2hjPWJTWDVQMTZVSnR3QVg5bHBVaE0mZWRtPUFQczE3Q1VCQUFBQSZjY2I9Ny01Jm9oPTAwX0FmQ25ZcnRiRmZNVXdKSWtVNThPbGNNdlVBTTM2VjNfYnRObjlzU2dVNlF2UGcmb2U9NjQyN0VBOUQmX25jX3NpZD05NzhjYjkmbmFtZT1TYXZlSW5zdGEuQXBwIC0gMzA2Nzc1Nzg4ODU1MzM2NjczNC5tcDQ']
    # download_obj = download_video(links)
    # download_obj.start_download()