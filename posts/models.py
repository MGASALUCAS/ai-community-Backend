from django.db import models
from django.conf import settings

class Post(models.Model):
    POST_TYPES = [
        ('blog', 'Blog'),
        ('newsletter', 'Newsletter'),
        ('talks_podcast', 'Talks & Podcast'),
        ('other', 'Other'),
    ]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    post_type = models.CharField(max_length=20, choices=POST_TYPES)
    tags = models.CharField(max_length=255)
    caption = models.TextField()
    link = models.URLField()
    media = models.ImageField(upload_to='post_media/')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
