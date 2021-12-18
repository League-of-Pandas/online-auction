from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
)
from rest_framework.permissions import IsAuthenticated
from .models import Item, Bidders
from .serializers import ItemSerializer, BiddersSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ItemsList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class BiddersList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Bidders.objects.all()
    serializer_class = BiddersSerializer

class BiddersDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Bidders.objects.all()
    serializer_class = BiddersSerializer