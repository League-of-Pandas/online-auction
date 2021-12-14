from rest_framework import serializers
from .models import CustomUser
from items.serializers import ItemSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    class Meta:
        model = CustomUser
        fields= '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

#  "id": 1,
#         "last_login": "2021-12-14T15:32:00.020473Z",
#         "is_superuser": true,
#         "username": "admin",
#         "first_name": "",
#         "last_name": "",
#         "email": "admin@admin.com",
#         "is_staff": true,
#         "is_active": true,
#         "date_joined": "2021-12-14T15:31:33.247318Z",
#         "location": null,
#         "number": null,
#         "groups": [],
#         "user_permissions": []