import logging
import os

import tweepy
from django.views.generic import TemplateView

# Get an instance of a logger
logger = logging.getLogger(__name__)


def create_api():
    """
    Test twitter credentials using Tweepy package
    @return: "Authentication OK" if valid else return "Error during authentication"
    @rtype: str
    """
    # Twitter OAuth credentials
    consumer_key = os.environ['TWITTER_API_KEY']
    consumer_secret = os.environ['TWITTER_SECRET_KEY']
    oauth_access_token = os.environ['TWITTER_ACCESS_TOKEN']
    oauth_access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(str(consumer_key), str(consumer_secret))
    auth.set_access_token(str(oauth_access_token), str(oauth_access_token_secret))
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api


def get_daily_tips(api):
    pass


# Create your views here.
class Home(TemplateView):
    template_name = "pages/home.html"
