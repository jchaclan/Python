import tweepy
import time

API_key = 'bXr3IlsKkpRygs4hmL54qHZA'
API_key_secret = '0qYMqx4d6YrTHtkCoVoHfkIFCCKvldTeILyfySdQSsMZSVLqC'
Access_token = '1265354860238704641-WkkkcVhPDkiULfDus62tEKJ9B4p9d'
Access_token_secret = 'TSlV4zqumG9AJNRlWq3Eqcfd8gARD3ksynbDSwJhUFf9'

auth = tweepy.OAuthHandler(API_key, API_key_secret)
auth.set_access_token(Access_token,Access_token_secret)
api = tweepy.API(auth)

user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)
    follower.follow()




#print(user.followers_count)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
