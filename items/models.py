from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.aggregates import Max
from django.utils import timezone

# Create your models here.

class Item(models.Model):
  item_name = models.CharField(max_length=64)
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
  init_price = models.IntegerField()
  highest_bidder = models.CharField(max_length=64, blank=True, null=True)

  min_bid = models.IntegerField(default=0)
  # final_price = models.IntegerField(default={init_price})
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  bidder = models.ForeignKey(get_user_model(),related_name="bidder", blank=True, null=True,on_delete=models.DO_NOTHING)

  start_data = models.DateTimeField(('start_data'), default=timezone.now)
  end_data = models.DateTimeField(('end_data'), default=timezone.now)
  bidder_counter = models.IntegerField(default=0)
  favorite_counter=models.IntegerField(default=0)
  is_sold = models.BooleanField(default=False)
  is_expirated = models.BooleanField(default=False)

  
