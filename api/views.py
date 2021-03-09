# Create your views here.
from books.models import Book
from rest_framework import generics

from pages.models import Tip
from .serializers import BookSerializer


class TipAPIView(generics.ListAPIView):
    queryset = Tip.objects.all()
    serializer_class = BookSerializer
