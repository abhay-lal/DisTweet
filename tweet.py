import tweepy

api_key = "6QKssjoogZgbYxqu4tq3oMZWf"
api_key_secret = "AeGaLp93QXZfN0S6WoE2emSdmBNM0ANlPlEFyitfzCxPHCLIvH"
access_token = "804686968177049601-EG5545NblupPzgrPObIQFVA97Jqlz1c"
access_token_secret = "HadgA2PUNQySdNVZiuubcKGJHivFBm20bZwtKiZNaADQy"

auth = tweepy.OAuthHandler("6QKssjoogZgbYxqu4tq3oMZWf", "AeGaLp93QXZfN0S6WoE2emSdmBNM0ANlPlEFyitfzCxPHCLIvH")
auth.set_access_token("804686968177049601-EG5545NblupPzgrPObIQFVA97Jqlz1c", "HadgA2PUNQySdNVZiuubcKGJHivFBm20bZwtKiZNaADQy")

api = tweepy.API(auth)


class Linstener(tweepy.Stream):
    def on_status(self, status):
        print(status.user.screen_name + " " + status.text)
        

stream_tweet = Linstener(api_key, api_key_secret, access_token, access_token_secret)

keywords = [-180, -90, 180, 90]

stream_tweet.filter(locations = keywords)

print("Tweets Started")