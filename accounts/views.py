from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    
)
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer
# from .permissions import AllowAnyCustom

class UserList(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer