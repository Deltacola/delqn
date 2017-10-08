from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Delivery(models.Model):
    start_area = models.CharField(max_length=5)
    end_area = models.CharField(max_length=5)
    method = models.CharField(max_length=5)
    price = models.IntegerField(default=0)