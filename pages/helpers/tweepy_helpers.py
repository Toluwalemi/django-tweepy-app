import json
import logging
import time
from datetime import datetime, timezone

import tweepy

from pages.helpers.tweepy_config import create_api
from pages.models import Tip, Link

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

        # store each tweet object in a list and store in a file
        tips_tweets = []
        for tweet in all_tweets:
            def format_date_time(json_obj):
                return time.strftime('%Y-%m-%d %H:%M:%S',
                                     time.strptime(json_obj._json['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))

            tweet._json['created_at'] = format_date_time(tweet)
            if '#pythontip' in tweet._json['full_text']:
                tips_tweets.append(tweet._json)
        with open('./pages/tweepy_response.txt', 'w+') as json_file:
            json.dump(tips_tweets, json_file, indent=4)

        # store the keys needed in a list then populate the db
        responses = []
        with open('./pages/tweepy_response.txt') as txt_file:
            data = json.load(txt_file)
            for item in data:
                my_response = {"id": item.get('id'),
                               "python_tip": item.get('full_text'),
                               "timestamp": item.get('created_at'),
                               "likes": item.get('favorite_count'),
                               "retweets": item.get('retweet_count'),
                               "tweet_link": f"https://twitter.com/python_tip/status/{item['id']}",
                               }
                if len(item['entities']['user_mentions']) > 0:
                    z = item['entities']['user_mentions'][0]
                    my_response['posted_by'] = z['screen_name']
                if 'extended_entities' in item:
                    my_response['media_links'] = item['extended_entities']['media']
                responses.append(my_response)
        for response in responses:
            if not Tip.objects.filter(id=response['id']).exists():
                if 'media_links' in response:
                    media_links = response['media_links']
                    response.pop('media_links')
                tip_objects = Tip.objects.create(**response)
                if 'media_links' in response:
                    for j in media_links:
                        print(j['media_url_https'])
                        Link.objects.create(media_link=j['media_url_https'], tip=tip_objects)

    except tweepy.RateLimitError as e:
        print("You have exceed the rate limit. I'll just cool off for  15 minutes. Sorry!")
        time.sleep(60 * 15)
    except tweepy.TweepError:
        print("Looks like there's been some error. Let's cool for for a minute. Shall we?")
        time.sleep(60)

    return True


def main():
    api = create_api()
    while True:
        get_user_timeline(api)
        logger.info("waiting")
        time.sleep(60 * 1440)


if __name__ == "__main__":
    main()
