from django.db import models


class DeliveryData(models.Model):
    company_name = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    total_length = models.CharField(max_length=10)
    del_time = models.CharField(max_length=10)
    start_area = models.CharField(max_length=10)
    end_area = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
