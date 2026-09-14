from rest_framework import serializers

from cars.models import CarImage, Car
from cars.serializers import CarImageSerializer


class CarSerializer(serializers.ModelSerializer):
    fuel = serializers.CharField(source = 'fuel.name')
    gear = serializers.CharField(source = 'gear.name')
    color = serializers.CharField(source = 'color.name')
    status = serializers.CharField(source = 'status.name')
    brand = serializers.CharField(source = 'brand.name')
    vin = serializers.CharField(max_length = 20, required = False, allow_blank = True)
    images = serializers.SerializerMethodField()
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(allow_empty_file = False, use_url = False),
        required = False
    )

    class Meta:
        model = Car
        fields = (
            'id', 'model', 'brand', 'year', 'mileage', 'power', 'displacement', 'vin', 'fuel', 'gear', 'color',
            'price', 'status', 'images', 'uploaded_images', 'created_at', 'updated_at'
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
        )
        write_only_fields = ('uploaded_images',)

    def create(self, validated_data: dict) -> Car:
        uploaded_images = validated_data.pop('uploaded_images', [])
        car = Car.objects.create(**validated_data)

        for image, index in enumerate(uploaded_images):
            CarImage.objects.create(car = car, image = image, index = index)

        return car

    def get_images(self, obj: Car) -> dict:
        qs = obj.images.all()
        return CarImageSerializer(qs, many = True).data
