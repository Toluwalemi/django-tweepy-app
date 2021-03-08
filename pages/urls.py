from django.urls import path, include

from .views import Home, show_doc_info  # new

app_name = 'pages'

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('', Home.as_view(), name="home"),
    path('dashboard/', show_doc_info, name="some_home"),
]
