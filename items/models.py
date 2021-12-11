from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

class Item(models.Model):
  item_name = models.CharField(max_length=64)
  # category = models.TextField(choices=)
  image = models.CharField(max_length=10000)
  # image = models.ImageField(upload_to='item_img/')
  # image = models.ImageField()
  CATEGORY_CHOICES = [
    ("Vehicles", 'Vehicles'),
    ("Coins & Bullion", 'Coins & Bullion'),
    ("Art", 'Art'),
    ]
  category = models.CharField(
    choices=CATEGORY_CHOICES,
    max_length=100,
    default=CATEGORY_CHOICES[0][0]
    )
  description = models.TextField()
  init_price = models.IntegerField()
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  highest_bidder = models.CharField(max_length=64, blank=True, null=True)

  start_data = models.DateTimeField(('start_data'), default=timezone.now)
  end_data = models.DateTimeField(('end_data'), default=timezone.now)
  bidder_counter = models.IntegerField(default=0)

# class Bodding(models.Model):
#   start_data = models.DateTimeField(('start_data'), default=timezone.now)
#   end_data = models.DateTimeField(('end_data'), default=timezone.now)
#   bidder_counter = models.IntegerField()
  
