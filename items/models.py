from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

class Item(models.Model):
  item_name = models.CharField(max_length=64 , blank=True, default="")
  image = models.CharField(max_length=10000)
  CATEGORY_CHOICES = [
    ("Vehicles", 'Vehicles'),
    ("Coins & Bullion", 'Coins & Bullion'),
    ("Art", 'Art'),
    ("Furniture",'Furniture'),
    ("Electronics",'Electronics'),
    ("Jewelry",'Jewelry'),
    ]
  category = models.CharField(
    choices=CATEGORY_CHOICES,
    max_length=100,
    default=CATEGORY_CHOICES[0][0]
    )
  
  description = models.TextField()
  init_price = models.IntegerField(blank=True, null=True)
  highest_bidding = models.IntegerField(default=0)

  bid_increment = models.IntegerField(default=0)
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE ,blank=True, null=True)
  bidder = models.ForeignKey(get_user_model(),related_name="bidder", blank=True, null=True,on_delete=models.DO_NOTHING)

  start_date = models.DateTimeField(('start_date'), default=timezone.now)
  end_date = models.DateTimeField(('end_date'), default=timezone.now)
  bidder_counter = models.IntegerField(default=0)
  favorite_counter=models.IntegerField(default=0)
  is_sold = models.BooleanField(default=False)
  is_expirated = models.BooleanField(default=False)

  
