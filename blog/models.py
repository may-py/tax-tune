from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #(auto_now=True) or (auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, editable=False ,related_name='comment', on_delete=models.CASCADE)
    name = models.ForeignKey(User ,on_delete=models.CASCADE)
    #name = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment %s -by %s' %(self.post.title, self.name)