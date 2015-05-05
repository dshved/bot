import random
import time
from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError

arrayToken = ['YOUR_TOKEN_1',
              'YOUR_TOKEN_2',
              'YOUR_TOKEN_3',
              'YOUR_TOKEN_4',
              'YOUR_TOKEN_5']

arrayTag = ['spb','vcocam','vcorussia','love','TFLers', 'tweegram',
            'photooftheday', '20likes', 'amazing', 'smile', 'follow4follow',
            'like4like', 'look', 'instalike', 'igers', 'picoftheday', 'food',
            'instadaily', 'instafollow', 'followme', 'girl', 'iphoneonly',
            'instagood', 'bestoftheday', 'instacool', 'instago', 'all_shots',
            'follow', 'webstagram', 'colorful', 'style', 'swag']

timeDelay = 3600 / (len(arrayToken) * 30)

while True:
    for i in arrayToken:
        random_tag = random.choice(arrayTag)
        access_token = i
        client_secret =""
        api = InstagramAPI(access_token=access_token,client_secret=client_secret)
        recent_media, next_ = api.tag_recent_media(count=30, tag_name=random_tag)
        photos = []
        print random_tag
        for media in recent_media:
            try:
                time.sleep(timeDelay)
                print api.like_media(media.id)
            except InstagramAPIError as e:
                if (e.status_code == 400):
                    print "You can not like this media"
