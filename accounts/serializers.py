from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

user = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = user
        fields = ['id','email','name','password']

