from rest_framework import serializers

from pages.models import Tip


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ('id', 'python_tip', 'posted_by', 'likes', 'retweets', 'tweet_link', 'timestamp')
