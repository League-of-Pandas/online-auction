import datetime
from typing import ItemsView
from django import test
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.shortcuts import get_object_or_404

from .models import Item

class ItemModelTests(TestCase):

    def test_blog_content(self):
        user = get_user_model().objects.create_user(username='tasneem',password='pass')
        user.save()
    
        test_item = Item.objects.create(
            owner = user,
            item_name = 'name',
            description = 'about the item',
            image = 'image.jpg',
            category = 'Art',
            init_price = 100,
            highest_bidder = 'unknown',
            min_bid = 5,
            bidder = user,
            start_date = '2021-12-14T14:09:00Z',
            end_date = '2021-12-28T14:09:00Z',
            bidder_counter = 4,
            favorite_counter=4,
            is_sold= False,
            is_expirated= False
        )
        
        test_item.save()
        item = Item.objects.filter(item_name='name')[0]
        self.assertEqual(str(item.owner), 'tasneem')
        self.assertEqual(item.item_name, 'name')
        self.assertEqual(item.description, 'about the item')
        self.assertEqual(item.image, 'image.jpg')

        self.assertEqual(item.category,'Art')
        self.assertEqual(item.init_price,100)
        self.assertEqual(item.highest_bidder,'unknown')
        self.assertEqual(item.min_bid, 5)
        self.assertEqual(str(item.bidder),'tasneem')
        self.assertEqual(item.favorite_counter,4)
        self.assertEqual(item.bidder_counter,4)
        self.assertEqual(item.is_sold, False)
        self.assertEqual(item.is_expirated,False)

class APITest(APITestCase):

    def test_list(self):
        response = self.client.get(reverse('item_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    

    def test_detail(self):

        user = get_user_model().objects.create_user(username='tasneem',password='pass')
        user.save()

        test_item = Item.objects.create(
            owner = user,
            item_name = 'name',
            description = 'about the item',
            image = 'image.jpg',
            category = 'Art',
            init_price = 100,
            highest_bidder = 'unknown',
            min_bid = 5,
            bidder = user,
            start_date = '2021-12-14T14:09:00Z',
            end_date = '2021-12-28T14:09:00Z',
            bidder_counter = 4,
            favorite_counter=4,
            is_sold= False,
            is_expirated= False
        )
        test_item.save()

        response = self.client.get(reverse('item_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,       
            "owner" : user.id,
            "item_name" :test_item.item_name,
            "description" : test_item.description,
            "image" : test_item.image,
            "category" : test_item.category,
            "init_price" : test_item.init_price,
            "highest_bidder" : test_item.highest_bidder,
            "start_date" : test_item.start_date,
            "end_date" : test_item.end_date,
            "bidder_counter" : test_item.bidder_counter,
            "favorite_counter":test_item.favorite_counter,
            "is_sold": test_item.is_sold,
            "is_expirated": test_item.is_expirated,
            "bidder" : user.id,
            "min_bid": test_item.min_bid,
    
        })
        

    def test_create(self):
        user = get_user_model().objects.create_user(username='tasneem',password='pass')
        user.save()
        
        url = reverse('item_list')
        data = {      
            "owner" : user.id,
            "item_name" :"name",
            "description" : "about the item",
            "image" : "image.jpg",
            "category" : "Art",
            "init_price" : 100,
            "highest_bidder" : "unknown",
            "start_date" :'2021-12-14T14:09:00Z' ,
            "end_date" : '2021-12-28T14:09:00Z',
            "bidder_counter" : 4,
            "favorite_counter":4,
            "is_sold": False,
            "is_expirated": False,
            "bidder" : user.id,
            "min_bid": 5,
        }
        


        response = self.client.post(url, json=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
            (response.status_code, response.content)
        ) 



        self.assertEqual(Item.objects.count(), 0)
        
    def test_update(self):
        user = get_user_model().objects.create_user(username='tasneem',password='pass')
        user.save()

        test_item = Item.objects.create(
            owner = user,
            item_name = 'name',
            description = 'about the item',
            image = 'image.jpg',
            category = 'Art',
            init_price = 100,
            highest_bidder = 'unknown',
            min_bid = 5,
            bidder = user,
            start_date = '2021-12-14T14:09:00Z',
            end_date = '2021-12-28T14:09:00Z',
            bidder_counter = 4,
            favorite_counter=4,
            is_sold= False,
            is_expirated= False
        )

        test_item.save()

        url = reverse('item_detail',args=[test_item.id])
        data = {
            "owner" : test_item.owner.id,
            "item_name" :"name",
            "description" : "about the item",
            "image" : "image.jpg",
            "category" : "Art",
            "init_price" : 100,
            "highest_bidder" : "unknown",
            "start_date" :'2021-12-14T14:09:00Z' ,
            "end_date" : '2021-12-28T14:09:00Z',
            "bidder_counter" : 4,
            "favorite_counter":4,
            "is_sold": False,
            "is_expirated": False,
            "bidder" : test_item.bidder.id,
            "min_bid": 5,
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
            (response.status_code, response.content)
        ) 
   


    