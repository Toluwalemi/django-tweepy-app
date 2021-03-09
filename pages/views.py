import logging

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F, Sum
from django.shortcuts import render
from django.views.generic import TemplateView

# Get an instance of a logger
from pages.models import Tip, Link

logger = logging.getLogger(__name__)


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Tip.objects.all(). \
        annotate(popularity=Sum(F('likes') + F('retweets'))).order_by('popularity')
    links = Link.objects.all()
    tip_contains_query = request.GET.get('tip_contains')
    exact_posted_by = request.GET.get('exact_posted_by')

    if is_valid_queryparam(tip_contains_query):
        qs = qs.filter(python_tip__icontains=tip_contains_query)

    if is_valid_queryparam(exact_posted_by):
        qs = qs.filter(posted_by=exact_posted_by)

    return qs


def show_tips(request):
    if request.method == "GET":
        qs = filter(request)
        # tips_render = Tip.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(qs, 10)
        try:
            tips_render = paginator.page(page)
        except PageNotAnInteger:
            tips_render = paginator.page(1)
        except EmptyPage:
            tips_render = paginator.page(paginator.num_pages)
        context = {
            'tips_render': tips_render,
            # 'link_render': Link.objecs.all(),
        }

        return render(request, "pages/dashboard.html", context)


# Create your views here.
class Home(TemplateView):
    template_name = "pages/home.html"
