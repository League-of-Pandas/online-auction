from django.db.models import fields
from rest_framework import serializers
from .models import Item,Bidders

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class BiddersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidders
        fields = '__all__'