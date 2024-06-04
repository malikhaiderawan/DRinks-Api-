from rest_framework import serializers
from .models import malik

class malikserializer(serializers.ModelSerializer):
    class Meta:
        model=malik
        fields= ['id','name','type','drink']

