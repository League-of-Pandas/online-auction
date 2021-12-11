from django.urls import path
from .views import ItemsList, ItemgDetail

urlpatterns = [
    path("", ItemsList.as_view(), name="item_list"),
    path("<int:pk>/", ItemgDetail.as_view(), name="item_detail"),
]

