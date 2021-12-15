import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.shortcuts import get_object_or_404

from .models import Item,Bidders


class ItemModelTests(TestCase):
    def test_blog_content(self):
        user = get_user_model().objects.create_user(username="tester", password="pass")
        user.save()

        test_item = Item.objects.create(
            owner=user,
            item_name="name",
            description="about the item",
            image="image.jpg",
            category="Art",
            init_price=100,
            highest_bidding=110,
            bid_increment=5,
            # bidder = None,
            start_date="2021-12-14T14:09:00Z",
            end_date="2021-12-28T14:09:00Z",
            bidder_counter=2,
            favorite_counter=4,
            is_sold=False,
        )

        test_item.save()
        item = Item.objects.filter(item_name="name")[0]
        self.assertEqual(str(item.owner), "tester")
        self.assertEqual(item.item_name, "name")
        self.assertEqual(item.description, "about the item")
        self.assertEqual(item.image, "image.jpg")

        self.assertEqual(item.category, "Art")
        self.assertEqual(item.init_price, 100)
        self.assertEqual(item.highest_bidding, 110)
        self.assertEqual(item.bid_increment, 5)
        self.assertEqual(item.favorite_counter, 4)
        self.assertEqual(item.bidder_counter, 2)
        self.assertEqual(item.is_sold, False)


class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse("item_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        user = get_user_model().objects.create_user(username="tester", password="pass")
        user.save()

        test_item = Item.objects.create(
            owner=user,
            item_name="name",
            description="about the item",
            image="image.jpg",
            category="Art",
            init_price=100,
            highest_bidding=150,
            bid_increment=5,
            start_date="2021-12-14T14:09:00Z",
            end_date="2021-12-28T14:09:00Z",
            bidder_counter=4,
            favorite_counter=4,
            is_sold=False,
        )
        test_item.save()
        test_item.bidder.add(user)
        response = self.client.get(reverse("item_detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": 1,
                "owner": user.id,
                "item_name": test_item.item_name,
                "description": test_item.description,
                "image": test_item.image,
                "category": test_item.category,
                "init_price": test_item.init_price,
                "highest_bidding": test_item.highest_bidding,
                "bid_increment": test_item.bid_increment,
                "start_date": test_item.start_date,
                "end_date": test_item.end_date,
                "bidder_counter": test_item.bidder_counter,
                "favorite_counter": test_item.favorite_counter,
                "is_sold": test_item.is_sold,
                "bidder": [1],
            },
        )


class APITestCRUD(APITestCase):

    def test_create(self):
        user = get_user_model().objects.create_user(username='tester',password='pass')
        user.save()

        url = reverse('item_list')
        data = {
            "owner" : user.id,
            "bidder": user.id,
            "item_name" :"name",
            "image" : "image.jpg",
            "category" : "Art",
            "description" : "about the item",
            "init_price" : 1000,
            "highest_bidding" : 2500,
            "bid_increment": 100,
            "start_date" :'2021-12-14T14:09:00Z' ,
            "end_date" : '2021-12-28T14:09:00Z',
            "bidder_counter" : 40,
            "favorite_counter":50,
            "is_sold": True,
        }


        response = self.client.post(url, json=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
            (response.status_code, response.content)
        )
        response = self.client.post(url, data, format='json')

        self.assertEqual(Item.objects.count(), 0)


        self.client.login(username='tester',password='pass')
        response2 = self.client.post(url, data, format='json')

        self.assertEqual(response2.status_code, status.HTTP_201_CREATED, user.id)

    def test_update(self):
        user = get_user_model().objects.create_user(username='tester',password='pass')
        user.save()

        test_item = Item.objects.create(
            owner = user,
            item_name = 'name',
            description = 'about the item',
            image = 'image.jpg',
            category = 'Art',
            init_price = 100,
            highest_bidding = 150,
            bid_increment = 5,
            start_date = '2021-12-14T14:09:00Z',
            end_date = '2021-12-28T14:09:00Z',
            bidder_counter = 4,
            favorite_counter=4,
            is_sold= True,
        )
        test_item.save()
        test_item.bidder.add(user)

        url = reverse('item_detail',args=[test_item.id])
        data = {
            "owner" : test_item.owner.id,
            "item_name" :"name",
            "description" : "about the item",
            "image" : "image.jpg",
            "category" : "Art",
            "init_price" : 100,
            "highest_bidding" : 5,
            "start_date" :'2021-12-14T14:09:00Z' ,
            "end_date" : '2021-12-28T14:09:00Z',
            "bidder_counter" : 4,
            "favorite_counter":4,
            "is_sold": True,
            "bidder" : user.id,
            "bid_increment": 5,
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
            (response.status_code, response.content)
        )
        self.client.login(username='tester',password='pass')

        response2 = self.client.put(url, data, format='json')

        self.assertEqual(response2.status_code, status.HTTP_200_OK, url)

    def test_delete(self):
            """Test the api can delete a item."""

            user = get_user_model().objects.create_user(username='tasneem',password='123')
            user.save()

            test_item = Item.objects.create(
                owner = user,
                item_name = 'name',
                description = 'about the item',
                image = 'image.jpg',
                category = 'Art',
                init_price = 100,
                highest_bidding = 120,
                bid_increment = 5,
                start_date = '2021-12-13T14:09:00Z',
                end_date = '2021-12-15T14:09:00Z',
                bidder_counter = 4,
                favorite_counter=4,
                is_sold= True,
            )

            test_item.save()
            test_item.bidder.add(user)
            item = Item.objects.get()

            url = reverse('item_detail', kwargs={'pk': item.id})

            response = self.client.delete(url)
            self.assertEqual(
                response.status_code,
                status.HTTP_401_UNAUTHORIZED,
                (response.status_code, response.content)
            )

            self.client.login(username='tester',password='pass')
            response = self.client.delete(url)
            # self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)

class APITestBidderCRUD(APITestCase):
    """
    Test for Bidder 
    """
    def test_create(self):
        userOwner = get_user_model().objects.create_user(username='tester',password='pass')
        userOwner.save()

        userBidder = get_user_model().objects.create_user(username='bidder',password='pass')
        userBidder.save()

        urlBidders = reverse('bidders-list')
        dateBidder = {
            "user" : userOwner.id,
            "Product": userBidder.id,
        }
        response = self.client.post(urlBidders, json=dateBidder)
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
            (response.status_code, response.content)
        )
        response = self.client.post(urlBidders, dateBidder, format='json')

        self.assertEqual(Item.objects.count(), 0)


        self.client.login(username='tester',password='pass')
        response = self.client.post(urlBidders, dateBidder, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, userBidder.id)

    
