from rest_framework import serializers

from pages.models import Tip, Contributor


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ('id', 'python_tip', 'posted_by', 'likes', 'retweets', 'tweet_link', 'timestamp')


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('daily_tip', 'name_or_id', 'email')
