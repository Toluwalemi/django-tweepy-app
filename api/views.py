# Create your views here.
from rest_framework import generics

from pages.models import Tip, Contributor
from .serializers import TipSerializer, ContributorSerializer


class TipAPIView(generics.ListAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    paginate_by = 20


class PostTip(generics.CreateAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class DetailTip(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
