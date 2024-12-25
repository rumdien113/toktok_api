import uuid
from rest_framework import serializers

from users.models import User
from users.serializers import UserSerializer
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    id_user = UserSerializer(read_only=True)
    total_likes = serializers.IntegerField(read_only=True)
    total_comments = serializers.IntegerField(read_only=True)   
    
    class Meta:
        model = Post
        fields = ['id', 'id_user', 'media', 'title', 'share', 'created_at', 'total_likes', 'total_comments']

    def create(self, validated_data):
        user_id = validated_data.pop('id_user')

        try:
            uuid.UUID(str(user_id))
        except ValueError:
            raise serializers.ValidationError({'id_user': 'Invalid UUID format'})

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({'id_user': 'User not found'})

        validated_data['id_user'] = user
        return Post.objects.create(**validated_data)