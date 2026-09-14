from rest_framework import serializers
from cars.models import Gear


class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = ('name',)
