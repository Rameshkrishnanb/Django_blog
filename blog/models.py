from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk":self.pk})

"""
from blog.models import Post
from django.contrib.auth.models import User

User.objects.all()
User.objects.first()
User.objects.first()
user = User.objects.filter(username="blah").first()
user.id
user.pk
user = User.objects.get(id=1)
Post.objects.all()
post_1 = Post(title="Blog 10", content="First Post Content", author=user)
Post.objects.all()



user.post_set
user.post_set.all()
user.post_set.create(title="blog 2",content="second post content")
Post.objects.all()
"""
