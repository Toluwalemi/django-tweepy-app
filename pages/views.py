import os

import tweepy
from django.views.generic import TemplateView

consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_SECRET_KEY']
oauth_access_token = os.environ['TWITTER_ACCESS_TOKEN']
oauth_access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


def verify_twitter_credentials(auth):
    auth = tweepy.OAuthHandler(str(consumer_key), str(consumer_secret))
    auth.set_access_token(str(oauth_access_token), str(oauth_access_token_secret))
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        return "Authentication OK"
    except Exception:
        return "Error during authentication"


# Create your views here.
class Home(TemplateView):
    template_name = "pages/home.html"
