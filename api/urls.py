from django.urls import path
from .views import TipAPIView, DetailTip, PostTip

urlpatterns = [
    path('<int:pk>/', DetailTip.as_view()),
    path('', TipAPIView.as_view()),
    path('create/', PostTip.as_view()),
]
