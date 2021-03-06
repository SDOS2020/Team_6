import uuid
from django.db import models
from users.models import User
# Create your models here.

class Class(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor', null=True, blank=True)
    mentees = models.TextField(default="{}")
    posts = models.TextField(default="{}")
    projects = models.TextField(default="{}")
    title = models.CharField(max_length=1024, default="")
    description = models.CharField(max_length=1024, default="")
    tags = models.CharField(max_length=1024, default="")


class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    post_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_by', null=True, blank=True)
    in_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='in_class', null=True, blank=True)
    post_text = models.TextField()
    comments = models.TextField()

class Comment(models.Model):
    parent = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='parent', null=True, blank=True)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_by', null=True, blank=True)
    comment_text = models.TextField(default="")
