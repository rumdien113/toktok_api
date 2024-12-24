import random
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from .serializers import PostSerializer

class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serizalizer = PostSerializer(data=request.data)
        if serizalizer.is_valid():
            serizalizer.save()
            return Response(serizalizer.data, status=status.HTTP_201_CREATED)
        return Response({
            'error': serizalizer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        all_posts = list(Post.objects.all())
        if not all_posts:
            return Response({'error': "No posts available"}, status=status.HTTP_404_NOT_FOUND)
        
        if id:
            try:
                current_post = Post.objects.get(id=id)
            except Post.DoesNotExist:
                return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            current_post = random.choice(all_posts)
        
        selected_posts = random.sample(all_posts, min(3, len(all_posts)))

        serializer = PostSerializer(selected_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response({
                'error': 'Post not found'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response({
                'error': 'Post not found'
            }, status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response({
            'message': 'Post deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)