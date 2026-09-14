from rest_framework import serializers

from cars.models import CarStatus


class CarStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarStatus
        fields = ('name',)