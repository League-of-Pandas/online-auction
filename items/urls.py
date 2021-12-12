from django.urls import path
from .views import ItemsList, ItemDetail

urlpatterns = [
    path("", ItemsList.as_view(), name="item_list"),
    path("<int:pk>/", ItemDetail.as_view(), name="item_detail"),
]

