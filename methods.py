
# Import instascrape module
from instascrape import Reel 
# Import time for the file name
import time

# session id 
SESSIONID = "17edb06b505-8cae27"

# we need header 
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
"cookie":f'sessionid={SESSIONID};'
}

def typeFile(url):
    urlist = url.split('/')
    if urlist[2]=='www.instagram.com':
        if urlist[3]=='reel':
            return 'mp4'
        elif urlist[3]=='p':
            return 'png'
        else:
            return 'None'
    else:
            return 'None'
        

def downloadFile(url):
    
        if typeFile(url)!='None':
            insta_reel = Reel(url)
            insta_reel.scrape(headers=headers)
            type = typeFile(url)

            if type=='mp4':
                insta_reel.download(fp=f"Downloads/videos/reel{int(time.time())}.{type}")
                print('Video downloaded successfuly!!')
            elif type=='png':
                insta_reel.download(fp=f"Downloads/images/img{int(time.time())}.{type}")
                print('Image downloaded successfuly!!')
        else:
            print('Error del link')



# img = 'https://www.instagram.com/p/CZnkclZPPfm/?utm_source=ig_web_copy_link'
# vid = 'https://www.instagram.com/reel/CZsaAycrEfE/?utm_source=ig_web_copy_link'
