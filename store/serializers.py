from rest_framework import serializers

from .models import Store

class StoreSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = Store
		