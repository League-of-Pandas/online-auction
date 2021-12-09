from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField
# Create your models here.

class Item(models.Model):
  item_name = models.CharField(max_length=64)
  image = models.CharField(max_length=10000)
  description = models.TextField()
  init_price = models.IntegerField()
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  highest_bidder = models.CharField(max_length=64, blank=True)
