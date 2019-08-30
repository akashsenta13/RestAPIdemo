from rest_framework import serializers
from .models import Tech

class TechSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tech
        fields = '__all__'