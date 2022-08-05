import tweepy

auth = tweepy.OAuthHandler(api_key, api_secrete)
auth.set_access_token(access_token ,access_token_secrete)

api = tweepy.API(auth)


class Linstener(tweepy.Stream):
    def on_status(self, status):
        print(status.user.screen_name + " " + status.text)
        

stream_tweet = Linstener(api_key, api_key_secret, access_token, access_token_secret)

keywords = [-180, -90, 180, 90]

stream_tweet.filter(locations = keywords)

print("Tweets Started")
