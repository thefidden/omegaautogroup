from rest_framework import serializers

from cars.filters import CarImageFilter
from cars.models import Car
from cars.serializers import CarImageSerializer


class ClientCarSerializer(serializers.ModelSerializer):
    fuel = serializers.CharField(source = 'fuel.name')
    gear = serializers.CharField(source = 'gear.name')
    color = serializers.CharField(source = 'color.name')
    status = serializers.CharField(source = 'status.name')
    brand = serializers.CharField(source = 'brand.name')
    images = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = (
            'id', 'model', 'brand', 'year', 'mileage', 'power', 'displacement', 'fuel', 'gear', 'color',
            'price', 'status', 'images'
        )
        read_only_fields = (
            'id', 'model', 'brand', 'year', 'mileage', 'power', 'displacement', 'fuel', 'gear', 'color',
            'price', 'status', 'images'
        )

    def get_images(self, obj: Car) -> dict:
        qs = CarImageFilter(data = { 'only_public': True }, queryset = obj.images.all()).qs
        return CarImageSerializer(qs, many = True).data
