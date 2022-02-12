from rest_framework import serializers
from .models import Detail

class DetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__'