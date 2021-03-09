from django.urls import path
from .views import TipAPIView

urlpatterns = [
    path('', TipAPIView.as_view()),
]
