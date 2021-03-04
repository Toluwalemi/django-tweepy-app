from django.contrib import admin

# Register your models here.
from pages.models import Link, Tip


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'python_tip', 'posted_by', 'is_published', 'likes', 'retweets']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['tip_id', 'tweet_link']

    # def view_tweets_link(self, obj):
    #     count = obj.links.count()
    #     url = (reverse("admin:pages_link_changelist")
    #            + "?")
    #     + urlencode({""})
    #     return formate_html('<a href="{}'>{} Links)


admin.site.register(Link, LinkAdmin)
