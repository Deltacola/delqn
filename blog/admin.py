from django.contrib import admin
from .models import DeliveryData
from .models import RecommendData

admin.site.register(DeliveryData)
admin.site.register(RecommendData)