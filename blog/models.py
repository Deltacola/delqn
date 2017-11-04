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


class DeliveryData(models.Model):
    company_name = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    total_length = models.CharField(max_length=10)
    del_time = models.CharField(max_length=10)
    start_area = models.CharField(max_length=10)
    end_area = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
