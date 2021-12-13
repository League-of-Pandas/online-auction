from logging import currentframe
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser

class CustomUserModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_model = CustomUser.objects.create(
            is_superuser= True,
            username= "tahany",
            first_name= "tahany",
            last_name= "ali",
            email= "tahany@admin.com",
            is_staff= True,
            is_active= True,
            date_joined= "2021-12-12T12:04:50.450159Z",
            location= 'location',
            number= '1223447',
        )
        test_model.save()

    def test_user_content(self):
        model = CustomUser.objects.get(id=1)
        self.assertEqual(model.is_superuser, True)
        self.assertEqual(model.username, 'tahany')
        self.assertEqual(model.first_name, 'tahany')
        self.assertEqual(model.last_name, 'ali')
        self.assertEqual(model.email, 'tahany@admin.com')
        self.assertEqual(model.is_staff, True)
        self.assertEqual(model.is_active, True)
        self.assertEqual(model.location, 'location')
        self.assertEqual(model.number, '1223447')

class APIUserTest(APITestCase):
    def test_user_list(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test_item = CustomUser.objects.create(
            is_superuser= True,
            username= "tahany",
            first_name= "tahany",
            last_name= "ali",
            email= "tahany@admin.com",
            is_staff= True,
            is_active= True,
            date_joined= "2021-12-12T12:04:50.450159Z",
            location= 'location',
            number= '1223447',
        )
        test_item.save()

    def test_user_post(self):
        user = get_user_model().objects.create_user(username='tahany',password='0000')
        user.save()
        
        url = reverse('user_list')
        data = {
            "is_superuser" : True,
            "username" : "tahani",
            "first_name" : "tahani",
            "last_name": "ali",
            "password": "01234tahany",
            "email" : "tahani95@admin.com",
            "is_staff":True,
            "is_active": True,
            "date_joined": "2021-12-12T12:04:50.450159Z",
            "location":"location",
            "number":"1223447",  
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, user.id)

    # def test_user_update(self):
    #     user = get_user_model().objects.create_user(username='tahany',password='0000')
    #     user.save()

    #     test_item = CustomUser.objects.create(
    #         is_superuser= True,
    #         username= "tahani",
    #         first_name= "tahani",
    #         last_name= "ali",
    #         email= "tahani95@admin.com",
    #         is_staff= True,
    #         is_active= True,
    #         date_joined= "2021-12-12T12:04:50.450159Z",
    #         location= 'location',
    #         number= '1223447',
    #     )
    #     test_item.save()

    #     url = reverse('user_detail',args=[test_item.id])
    #     data = {
    #         "is_superuser" : True,
    #         "username" : "tahani",
    #         "first_name" : "tahani",
    #         "last_name": "ali",
    #         "password": "01234tahany",
    #         "email" : "tahani95@admin.com",
    #         "is_staff":True,
    #         "is_active": True,
    #         "date_joined": "2021-12-12T12:04:50.450159Z",
    #         "location":"location",
    #         "number":"1223447", 
    #     }
    #     response = self.client.put(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK, url)

    # def test_delete(self):
    #         """Test the user can delete a item."""

    #         user = get_user_model().objects.create_user(username='tahany',password='0000')
    #         user.save()

    #         test_user = CustomUser.objects.create(
    #             is_superuser= True,
    #             username= "tahany",
    #             first_name= "tahany",
    #             last_name= "ali",
    #             email= "tahany@admin.com",
    #             is_staff= True,
    #             is_active= True,
    #             date_joined= "2021-12-12T12:04:50.450159Z",
    #             location= 'location',
    #             number= '1223447',
    #         )
    #         test_user.save()
    #         item = CustomUser.objects.get()
    #         url = reverse('user_detail', kwargs={'pk': item.id})
    #         response = self.client.delete(url)
    #         print(response.data)
    #         self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)

