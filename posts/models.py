from django.db import models
import uuid

from users.models import User

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True, max_length=155)
    share = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def total_likes(self):
        from likes.models import Like
        return Like.objects.filter(target_id=self.id, target_type='post').count()
    
    @property
    def total_comments(self):
        from comments.models import Comment
        return Comment.objects.filter(post=self).count()