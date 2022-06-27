#your twitter auth keys (https://developer.twitter.com/en/apps)
api_key = ""
api_secret_key = ""

access_token = ""
access_token_secret = ""

#standard search query input
search_query = 'gameDev OR screeps OR machinelearning OR MLAgents OR #indiegame OR #madewithunity'

#amount of tweets to pull
AMT_TWEETS = 250

#min and max wait time in seconds on an unexpected error
MIN_WAIT_ON_ERR = 3600 # 1 hour
MAX_WAIT_ON_ERR = 14400 # 4 hours

#wait time (in seconds) on warning: post already faved
MIN_WAIT_ON_ALREADY_FAVED = 120
MAX_WAIT_ON_ALREADY_FAVED = 300

#min and max wait time in seconds between bot actions
MIN_WAIT_BETWEEN_ACTION = 30
MAX_WAIT_BETWEEN_ACTION = 90

#min number of followers needed to follow the User
#max number of followers user is allowed to have to follow
#set max_follower_to_follow to 'inf' to ignore max Amount
#set min_follower_to_follow to 'inf' to disable the following feature
MIN_FOLLOWER_TO_FOLLOW = 0
MAX_FOLLOWER_TO_FOLLOW = 125

#min number of followers needed to favorite the tweet
#max number of followers user is allowed to have to favorite the tweet
#set max_follower_to_follow to 'inf' to ignore max Amount
#set min_follower_to_follow to 'inf' to disable the favoriting feature
MIN_FOLLOWER_TO_FAVORITE = 0
MAX_FOLLOWER_TO_FAVORITE = 500

