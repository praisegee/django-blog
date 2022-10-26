from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    @property
    def img_url(self):
        try:
            url = self.image.url
        except ValueError:
            url = "/media/d2.jpg"
        return url


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content[:30]



        



