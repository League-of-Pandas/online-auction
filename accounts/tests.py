# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse

# from rest_framework import status
# from rest_framework.test import APITestCase

# from .models import CustomUser

# class CustomUserModelTests(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         test_user = get_user_model().objects.create_user(username='tasneem',password='pass')
#         test_user.save()

#         test_model = CustomUser.objects.create(
#             last_login= "2021-12-12T12:55:04.964996Z",
#             is_superuser= True,
#             username= "tasneem",
#             first_name= "tasneem",
#             last_name= "alabsi",
#             email= "tasneem@admin.com",
#             is_staff= True,
#             is_active= True,
#             date_joined= "2021-12-12T12:04:50.450159Z",
#             location= 'location',
#             number= '1223447',
#             groups= [],
#             user_permissions= []
#         )
#         test_model.save()

#     def test_user_content(self):
#         model = CustomUser.objects.get(id=1)

#         self.assertEqual(model.is_superuser, True)
#         self.assertEqual(model.username, 'tasneem')
#         self.assertEqual(model.first_name, 'tasneem')
#         self.assertEqual(model.last_name, 'alabsi')
#         self.assertEqual(model.email, 'tasneem@admin.com')
#         self.assertEqual(model.is_staff, True)
#         self.assertEqual(model.is_active, True)
#         self.assertEqual(model.location, 'location')
#         self.assertEqual(model.number, '1223447')
#         self.assertEqual(model.groups, [])
#         self.assertEqual(model.user_permissions, [])