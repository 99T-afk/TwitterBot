# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tweepy
import schedule
import time
import praw
import requests
from passwrd import *

#
#
reddit = praw.Reddit(
    client_id = redclient_id,
    client_secret = redclient_secret,
    password = redpassword,
    user_agent = reduser_agent,
    username = redusername,
)

print(reddit.user.me())


#config
urlList = []
validURLList = []
global nextImgToPostIdx
nextImgToPostIdx = 0

def config():
    global nextImgToPostIdx
    nextImgToPostIdx = 0
    global validURLList
    validURLList = []

config()


def getImageList():
    # return a list of local images
    print("Indexing local images...")

auth = tweepy.OAuthHandler(notMyAPIKey, notMyAPIKeySecret)
auth.set_access_token(notMyAccessToken, notMyAccessTokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def connectToTwitter():
    print("Connecting to twitter")
    #auth = tweepy.OAuth1UserHandler(notMyAPIKey,notMyAPIKeySecret,notMyAccessToken,notMyAccessTokenSecret)

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(notMyAPIKey, notMyAPIKeySecret)
    auth.set_access_token(notMyAccessToken, notMyAccessTokenSecret)

    api = tweepy.API(auth, wait_on_rate_limit=True)


    return api



def postAStatus(api, statusIn):
    print("Tweeted: " + str(statusIn))
    api.update_status(status=statusIn)






#imagePath = "C:/Users/Tom/Desktop/DEVELOPMENT/TwitterBot/TwitterBot/cute0.jpg"
#api.update_status_with_media("", imagePath)

def getImages():
    print("getting new images!")
    #scrapes images
    subreddit = reddit.subreddit("cats")
    posts = subreddit.top("day") #can also do hour, day, week, month
    # Scraping the top posts of the current month
    
    #posts_dict = {"Title": [], "Post Text": [], "ID": [], "Score": [], "Total Comments": [], "Post URL": []}
    posts_dict = {"Post URL": []}
    
    """for post in posts:
        # Title of each post
        posts_dict["Title"].append(post.title)
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
        # Unique ID of each post
        posts_dict["ID"].append(post.id) 
        # The score of a post
        posts_dict["Score"].append(post.score)    
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)    
        # URL of each post
        posts_dict["Post URL"].append(post.url)"""

    for post in posts:
        posts_dict["Post URL"].append(post.url)
        urlList.append(post.url)

    #print(str(posts_dict))


    imgCount = 0
    maxImg = 15  #zero indexed

    for imgIdx, image_url in enumerate(urlList):

        #print(str(image_url[-3:]))

        if(image_url[-3:] == 'jpg' or image_url[-3] == 'png'):
            img_data = requests.get(image_url).content
            inputName = "cute" + str(imgCount) + image_url[-4:]
            with open(inputName, 'wb') as handler:
                handler.write(img_data)

            validURLList.append(image_url)

            if imgCount == maxImg:
                nextImgToPostIdx = 0
                break
            else:
                imgCount += 1

    return validURLList, nextImgToPostIdx


def postAnImage(postIdx,validURLList):

    #print("list: " + str(validURLList))
    imagePath = "C:/Users/Tom/Desktop/DEVELOPMENT/TwitterBot/TwitterBot/cute" + str(postIdx) + validURLList[postIdx][-4:]
    status = ""

    api.update_status_with_media(status, imagePath)
    print("Tweeted an image: cute" + str(postIdx) + validURLList[postIdx][-4:])
    
    #nextImgToPostIdx += 1



if __name__ == '__main__':
    #api = connectToTwitter()
    #nextImgToPostIdx = 0
    #validURLList, nextImgToPostIdx = getImages()
    #postAnImage(nextImgToPostIdx,validURLList)
    while True:
        validURLList, nextImgToPostIdx = getImages()
        print("validURL: " + str(validURLList))
        for postIdx, post in enumerate(validURLList):
            postAnImage(postIdx,validURLList)
            time.sleep(60 * 120)

        #schedule.run_pending()
        time.sleep(1)
    #statusIn = "Hello Twitter"
    #postAStatus(api, statusIn)
    #postAnImage(api)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
