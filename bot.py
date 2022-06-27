import tweepy
import time
import random
import logging
from config import *

ERROR_ALREADY_FAVED = 139
ERROR_FOLLOW_TO_MANY_PEOPLE = 161


logging.basicConfig(filename = 'bot.log', level = logging.INFO, format = '%(asctime)s %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit = True)

def sleepForRnd(minValue, maxValue = None):
    if(maxValue is not None):
        rnd = random.randint(minValue, maxValue)
        time.sleep(rnd)
    else:
        time.sleep(minValue)


logging.info("Twitter bot started ")
ctrFavored = 0

for tweet in tweepy.Cursor(api.search_tweets, search_query, result_type = 'recent').items(AMT_TWEETS):
    try:

        sleepForRnd(MIN_WAIT_BETWEEN_ACTION, MAX_WAIT_BETWEEN_ACTION)
    
        followersCount = tweet.user.followers_count 
        
        #Favorite tweet when user follower amount is in specific range
        if (followersCount <= MAX_FOLLOWER_TO_FAVORITE and followersCount >= MIN_FOLLOWER_TO_FAVORITE):
                tweet.favorite()
                ctrFavored = ctrFavored + 1
                logging.info("faved tweet from: " + tweet.user.name)
                    
                sleepForRnd(MIN_WAIT_BETWEEN_ACTION, MAX_WAIT_BETWEEN_ACTION)
            
        
        #Follow user if user follower amount is in specific range
        if followersCount < MAX_FOLLOWER_TO_FOLLOW:
            if followersCount > MIN_FOLLOWER_TO_FOLLOW:
                tweet.user.follow()
                logging.info("followed user: " + tweet.user.name)

                sleepForRnd(MIN_WAIT_BETWEEN_ACTION, MAX_WAIT_BETWEEN_ACTION)
        
    
    except StopIteration:
        logging.info("amt new favs: "+ctrFavored)
        logging.info("Twitter bot stopped")
        break
    
    except tweepy.TweepyException as e:
        errCode = e.api_codes[0]
        
        # ERR_CODE 139 = Tweet is already favored
        if(errCode == ERROR_ALREADY_FAVED):
            logging.info("Error: post already faved")
            sleepForRnd(MIN_WAIT_ON_ALREADY_FAVED, MAX_WAIT_ON_ALREADY_FAVED)
                
        elif(errCode == ERROR_FOLLOW_TO_MANY_PEOPLE):
            logging.info(e)
            sleepForRnd(MIN_WAIT_ON_ALREADY_FAVED, MAX_WAIT_ON_ALREADY_FAVED)
        
        else:
            logging.warning("unhandeld Error "+e.reason)
            sleepForRnd(MIN_WAIT_ON_ERR, MAX_WAIT_ON_ERR)


