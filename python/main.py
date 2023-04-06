from . videodownload import video_download_from_link
from . pinterest import upload_to_pinterest_class
from . files  import delete_video
from . links import links
from time import sleep


def get_links():
    try:
        link_obj = links()
        link_obj.connect()
        if link_obj.fetch_links():
            print('links fetched successfully')
            link_obj.clear_links()
        else:
            link_obj.disconnect()
            return False
        link_obj.disconnect()
        return link_obj.links
    except Exception as e:
        print(f'failed to fetch links reason : {e}')
        return False



def download_video(video_link):
    driver_obj = video_download_from_link(video_link)
    driver_obj.download_video()
    print(f'video {video_link} downloded successfully')
    return True
    # except Exception as e:
    #     print(f'failed to download video reason : {e}')
    #     return False
    

def upload_video():
    try:
        pin_obj = upload_to_pinterest_class()
        pin_obj.load_pinterest()
        pin_obj.start_upload()
        print('video uploding  complete')
        return True
    except Exception as e:
        print(f'uploding video to pintrest failed reasnon : {e}')
        return False
    

def download_upload(link):
    status_download_video = download_video(link)
    if status_download_video:
        upload_video()
        delete_video()
        return True
    else:
        return True
    
def main():
    links_list = get_links()
    if links_list:
        pass
    else:
        print('error occured while fetchign links')
        exit()
    if len(links_list) == 0:
        print('please upload links to database')
        exit()
    else:
        for link in links_list:
            download_upload(link)
            sleep(3600)
            # except:
            #     print('for loop error')
            #     exit()
        print('uploding vidoe complete')
        return main()
    

# final part of execution
# if __name__ == '__main__':
#     print('execution started')
#     main()
        

        
        


    




