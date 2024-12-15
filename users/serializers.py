from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'firstname', 'lastname', 'birthdate', 'phone', 'gender', 'avatar', 'bio']    
        extra_kwargs = {'password': {'write_only': True}}
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()