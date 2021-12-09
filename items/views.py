from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Item
from .serializers import ItemSerializer

class ItemsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemgDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer