from rest_framework import serializers

from .models import Donut

class DonutSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = Donut
		