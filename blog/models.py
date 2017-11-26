from django.db import models


class DeliveryData(models.Model):
    company_name = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=8, decimal_places=1)
    total_length = models.IntegerField(default=0)
    del_time = models.DecimalField(max_digits=8, decimal_places=2)
    start_area = models.CharField(max_length=10)
    end_area = models.CharField(max_length=10)
    price = models.IntegerField(default=0)
    tel_num = models.CharField(max_length=16, blank=True)
