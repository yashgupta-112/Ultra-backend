from rest_framework import serializers
from .models import plans,info,tickets,service,addon
from django.contrib.auth.models import User

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = plans
        fields ='__all__'

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = info
        fields ='__all__'

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets
        fields ='__all__'
        
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username', 'email', 'password']
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = service
        fields ='__all__'

class AddonSerializer(serializers.ModelSerializer):
    class Meta:
        model = addon
        fields ='__all__'
        