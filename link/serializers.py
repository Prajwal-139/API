from rest_framework import serializers
from .models import BookMyShow

class BookMyShowSer(serializers.ModelSerializer):
    class Meta:
        model = BookMyShow
        fields = '__all__'