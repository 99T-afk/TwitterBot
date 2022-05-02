# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tweepy
import schedule
import time
import praw
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

subreddit = reddit.subreddit("awww")

posts = subreddit.top("month")
# Scraping the top posts of the current month
 
posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }
 
for post in posts:
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
    posts_dict["Post URL"].append(post.url)

print(str(posts_dict))

def getImageList():
    # return a list of local images
    print("Indexing local images...")

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



def postAnImage(api):

    imagePath = "C:/Users/Tom/PycharmProjects/TwitterBot/cat0.webp"
    status = "Cat!"

    api.update_status_with_media(status, imagePath)
    print("Tweeted an image: " + str(status))



def getImages():
    #scrape images
    print("scraped!")

schedule.every(2).seconds.do(getImages)
#schedule.every(2).hour.do(getImages())
#schedule.every(2).hour.do(getImages())

if __name__ == '__main__':
    api = connectToTwitter()
    while True:
        schedule.run_pending()
        time.sleep(1)
    #statusIn = "Hello Twitter"
    #postAStatus(api, statusIn)
    #postAnImage(api)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
