from rest_framework import serializers

from .models.donut import Donut
from .models.baker import Baker

class DonutSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = Donut

class DonutReadSerialzier(serializers.ModelSerializer):
	baker = serializers.StringRelatedField()
	class Meta:
		fields = '__all__'
		model = Donut 

class BakerSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = Baker