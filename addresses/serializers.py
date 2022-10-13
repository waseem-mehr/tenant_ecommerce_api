from rest_framework import serializers
from .models import Country,City,State

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','name']


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id','name']

