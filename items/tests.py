import datetime
from typing import ItemsView
from django import test
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from django.shortcuts import get_object_or_404

from .models import Item

class ItemModelTests(TestCase):

    # @classmethod
    # def setUpTestData(cls):
        # user = get_user_model().objects.create_user(username='tasneem',password='pass')
        # user.save()
    
        # test_item = Item.objects.create(
        #     owner = user,
        #     item_name = 'name',
        #     description = 'about the item',
        #     image = 'image.jpg',
        #     category = 'Art',
        #     init_price = 100,
        #     highest_bidder = 'unknown',
        #     start_date = '2021-12-14T14:09:00Z',
        #     end_date = '2021-12-28T14:09:00Z',
        #     bidder_counter = 4
        # )
        
        # test_item.save()
        # print('hello',user)
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
            start_date = '2021-12-14T14:09:00Z',
            end_date = '2021-12-28T14:09:00Z',
            bidder_counter = 4
        )
        
        test_item.save()
        item = Item.objects.filter(item_name='name')[0]
        print('hi fofo',item)
        # try:
        #     item = Item.objects.get(pk=1)
        # except Item.DoesNotExist:
        #     item = None
        print('hello',Item.objects)
        self.assertEqual(str(item.owner), 'tasneem')
        self.assertEqual(item.item_name, 'name')
        self.assertEqual(item.description, 'about the item')
        self.assertEqual(item.image, 'image.jpg')

        self.assertEqual(item.category,'Art')
        self.assertEqual(item.init_price,100)
        self.assertEqual(item.highest_bidder,'unknown')
        # self.assertEqual(item.start_date, datetime.datetime(2021, 12, 14, 14, 9, tzinfo=))
        # self.assertEqual(item.end_date,'2021-12-28T14:09:00Z')
        self.assertEqual(item.bidder_counter,4)

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('item_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        user = get_user_model().objects.create_user(username='tasneem2',password='pass')
        user.save()

        test_item = Item.objects.create(
            owner = user,
            item_name = 'name1',
            description = 'about the item',
            image = 'image.jpg',
            category = 'Art',
            init_price = 100,
            highest_bidder = 'unknown',
            start_date = '2021-12-14T14:09:00Z',
            end_date = '2021-12-28T14:09:00Z',
            bidder_counter = 4
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
            "bidder_counter" : test_item.bidder_counter
    
        })
        

    def test_create(self):
        test_user = get_user_model().objects.create_user(username='tasneem',password='pass')
        test_user.save()

        url = reverse('item_list')
        data = {
            "id": 1,
            "owner" : test_user.id,
            "item_name" :'name',
            "description" : 'about the item',
            "image" : 'image.jpg',
            "category" : 'Art',
            "init_price" : 100,
            "highest_bidder" : 'unknown',
            "start_date" : '2021-12-14T14:09:00Z',
            "end_date" : '2021-12-28T14:09:00Z',
            "bidder_counter" : 4
        }

        # response = self.client.post(url, data, format='json')
        # print('res2',response)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        # self.assertEqual(Item.objects.count(), 1)
        # self.assertEqual(Item.objects.get().name, data["item_name"])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='tasneem',password='pass')
        test_user.save()

        test_item = Item.objects.create(
            owner = test_user,
            item_name = 'name1',
            description = 'about the item',
            image = 'image.jpg',
            category = 'Art',
            init_price = 100,
            highest_bidder = 'unknown',
            start_date = '2021-12-14T14:09:00Z',
            end_date = '2021-12-28T14:09:00Z',
            bidder_counter = 4
        )

        test_item.save()

        url = reverse('item_detail',args=[test_item.id])
        data = {
            "owner" : test_user.id,
            "item_name" :test_item.item_name,
            "description" : test_item.description,
            "image" : test_item.image,
            "category" : test_item.category,
            "init_price" : test_item.init_price,
            "highest_bidder" : test_item.highest_bidder,
            "start_date" : test_item.start_date,
            "end_date" : test_item.end_date,
            "bidder_counter" : test_item.bidder_counter
        }

        response = self.client.put(url, data, format='json')

        # self.assertEqual(response.status_code, status.HTTP_200_OK, url)

#         self.assertEqual(Character.objects.count(), test_character.id)
#         self.assertEqual(Character.objects.get().name, data['name'])


#     def test_delete(self):
#         """Test the api can delete a character."""

#         test_user = get_user_model().objects.create_user(username='tasneem',password='pass')
#         test_user.save()

#         test_character = Character.objects.create(
#             writer = test_user,
#             name = 'any',
#             description = '...',
#             death_year = '2000',
#         )

#         test_character.save()

#         character = Character.objects.get()

#         url = reverse('characters_detail', kwargs={'pk': character.id})


#         response = self.client.delete(url)

#         self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)

