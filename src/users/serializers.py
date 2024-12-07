from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'birthdate', 'password', 'email', 'firstname', 'lastname', 'username', 'phone', 'gender']    
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        # user = User(
        #     username = validated_data['username'],
        #     email = validated_data['email'],
        #     firstname= validated_data['firstname'],
        #     lastname = validated_data['lastname'],
        #     birthdate = validated_data['birthdate'],
        #     gender = validated_data['gender'],
        #     phone = validated_data['phone']
        # )
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user 
