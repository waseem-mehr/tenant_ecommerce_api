from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','mobile_number','is_mobile_veriefied','business_name']


class UserBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['business_name']