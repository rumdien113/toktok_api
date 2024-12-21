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