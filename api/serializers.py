from rest_framework import serializers

from pages.models import Tip, Contribution


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ('id', 'python_tip', 'posted_by', 'likes', 'retweets', 'tweet_link', 'timestamp')


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ('id', 'contributor', 'daily_tip', 'name_or_id', 'email')
