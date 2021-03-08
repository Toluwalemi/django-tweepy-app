from django.urls import path

from .views import Home, show_tips

app_name = 'pages'

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('', Home.as_view(), name="home"),
    path('dashboard/', show_tips, name="dashboard"),
]
