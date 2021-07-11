import tweepy
import json
import csv

# Credentials in json file

creds = json.load(open("credentials.json"))

consumer_key = creds["consumer_key"]
consumer_secret = creds["consumer_secret"]
access_token = creds["access_token"]
access_token_secret = creds["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Query: Football

# Open/Create a file to append data
csvFile = open("ua.csv", "a")
# Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(
    api.search, q="#football", count=100, lang="en", since="2021-07-10"
).items():
    print(tweet.created_at, tweet.text)
    # tweet.author can be appended
    csvWriter.writerow([tweet.created_at, tweet.text.encode("utf-8")])
