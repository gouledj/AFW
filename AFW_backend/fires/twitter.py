# fires/twitter.py

import tweepy
from django.conf import settings
from .models import TwitterReport

def fetch_twitter_data():
    auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET_KEY)
    auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Adjust the query to fit your needs
    tweets = api.search_tweets(q="Alberta wildfire", count=100)

    for tweet in tweets:
        TwitterReport.objects.create(
            tweet_id=tweet.id_str,
            user=tweet.user.screen_name,
            content=tweet.text,
            location=tweet.place.full_name if tweet.place else '',
            timestamp=tweet.created_at
        )
