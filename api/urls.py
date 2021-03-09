from django.urls import path
from .views import TipAPIView, DetailTip, PostContribution

app_name = 'api'

urlpatterns = [
    path('<int:pk>/', DetailTip.as_view(), name="detail_view"),
    path('', TipAPIView.as_view(), name="list_view"),
    path('create/', PostContribution.as_view(), name="create_view"),
]
