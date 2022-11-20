from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 

from ..models.donut import Donut
from ..serializers import DonutSerializer, DonutReadSerialzier
# Create your views here.


class DonutsView(APIView):
	"""View class for donuts/ for viewing and creating"""
	serializer_class = DonutSerializer
	def get(self, request):
		donuts = Donut.objects.all()
		serializer = DonutReadSerialzier(donuts, many = True)
		return Response({'donuts': serializer.data})

	def post(self, request):
		serializer = DonutSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DonutDetailView(APIView):
	"""	View class for donuts/:pk for viewing a single donut, updating a single donut, or removing a single donut"""
	serializer_class = DonutSerializer
	def get(self, request, pk):
		donut = get_object_or_404(Donut, pk=pk)
		serializer = DonutSerializer(donut)
		return Response({'donut': serializer.data})
	
	def patch(self, request, pk):
		donut = get_object_or_404(Donut, pk=pk)
		serializer = DonutReadSerialzier(donut, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		donut = get_object_or_404(Donut, pk=pk)
		donut.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
