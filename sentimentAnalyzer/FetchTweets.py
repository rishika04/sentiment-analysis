import tweepy

consumer_key = "PqlDzi3JYtVaTL4TnaPCwschi"
consumer_secret = "VSG0JijxjWToWa4w8e52RFSxh0O8WZiESXXOCXC6374tGFVeK2"

access_token = "2468944789-NHtxFjhG24Nwkc7zu59Sp5grKZHBcDVD8etBwic"
access_token_secret = "d0FU6s9d9Qn0kJVN9TMoV14s6wNkPND6ew3W7EpkI1Yrm"


class FetchData():

    def getTwitterData(self, tag):
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)

            api = tweepy.API(auth)

            public_tweets = api.search( q = tag, count=50000,language = 'en' )

            return public_tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))


