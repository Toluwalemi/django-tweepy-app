import json
import logging
import time

import tweepy

from pages.helpers.tweepy_config import create_api

logger = logging.getLogger(__name__)


def get_user_timeline(api):
    logger.info("Retrieving and following followers")
    tweets_count = 200
    screen_name = "python_tip"
    all_tweets = []
    try:
        new_tweets = api.user_timeline(screen_name=screen_name,
                                       tweet_mode='extended', count=tweets_count,
                                       include_rts=False, exclude_replies=True, include_entities=True)
        all_tweets.extend(new_tweets)
        print("...%s tweets downloaded so far" % (len(all_tweets)))
        oldest = all_tweets[-1].id - 1  # saves id minus 1 to avoid duplication

        # keep getting tweets until none is left
        while len(new_tweets) > 0:
            print("getting tweets before %s" % oldest)
            new_tweets = api.user_timeline(screen_name=screen_name,
                                           tweet_mode='extended', count=tweets_count,
                                           include_rts=False, exclude_replies=True, include_entities=True,
                                           max_id=oldest)
            all_tweets.extend(new_tweets)
            oldest = all_tweets[-1].id - 1
            print("...%s tweets downloaded so far" % (len(all_tweets)))

        tips_tweets = []
        for tweet in all_tweets:
            if '#pythontip' in tweet._json['full_text']:
                print('true')
                tips_tweets.append(tweet._json)
        with open('./pages/tweepy_response.txt', 'w+') as json_file:
            json.dump(tips_tweets, json_file, indent=4)

    except tweepy.RateLimitError as e:
        print("You have exceed the rate limit. I'll just cool off for  15 minutes. Sorry!")
        time.sleep(60 * 15)
    except tweepy.TweepError:
        print("Looks like there's been some error. Let's cool for for a minute. Shall we?")
        time.sleep(60)

    return True


def execute_user_timeline():
    api = create_api()
    while True:
        get_user_timeline(api)
        logger.info("waiting")
        time.sleep(60 * 1440)


if __name__ == "__main__":
    execute_user_timeline()
