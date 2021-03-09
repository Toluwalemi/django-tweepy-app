# Create your views here.
from rest_framework import generics

from pages.models import Tip, Contribution
from .serializers import TipSerializer, ContributionSerializer


class TipAPIView(generics.ListAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    paginate_by = 20


class PostTip(generics.CreateAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer


class DetailTip(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
