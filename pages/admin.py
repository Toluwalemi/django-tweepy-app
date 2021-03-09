from django.contrib import admin

# Register your models here.
from pages.models import Link, Tip, Contribution


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ['id', 'daily_tip', 'name_or_id', 'email']


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'python_tip', 'posted_by', 'tweet_link', 'is_published', 'likes', 'retweets']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['tip_id', 'media_link']


admin.site.register(Link, LinkAdmin)
