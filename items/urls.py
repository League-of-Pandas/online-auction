from django.urls import path
from .views import ItemsList, ItemDetail, BiddersDetail, BiddersList

urlpatterns = [
    path("", ItemsList.as_view(), name="item_list"),
    path("<int:pk>/", ItemDetail.as_view(), name="item_detail"),
    path('bidders/',BiddersList.as_view(), name='bidders-list'),
    path("bidders/<int:pk>/", BiddersDetail.as_view(), name="bidders_detail"),

]

