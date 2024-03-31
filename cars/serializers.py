from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):

    photo = serializers.ImageField(required=False)

    class Meta:
        model = Car
        fields = '__all__'
