from django.urls import path, include

from .views import Home  # new

app_name = 'pages'

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('', Home.as_view(), name="home"),
]
