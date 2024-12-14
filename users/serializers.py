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

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     user = User(**validated_data)
    #     if password:
    #         user.set_password(password)
    #     user.save()
    #     return user 
