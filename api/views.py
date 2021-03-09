# Create your views here.
from rest_framework import generics

from pages.models import Tip
from .serializers import TipSerializer


class TipAPIView(generics.ListAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
