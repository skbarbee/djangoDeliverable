from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 

from ..models.baker import Baker
from ..serializers import BakerSerializer
# Create your views here.


class BakersView(APIView):
	"""View class for bakers/ for viewing and creating"""
	serializer_class = BakerSerializer
	def get(self, request):
		bakers = Baker.objects.all()
		serializer = BakerSerializer(bakers, many = True)
		return Response({'bakers': serializer.data})

	def post(self, request):
		serializer = BakerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BakerDetailView(APIView):
	"""	View class for bakers/:pk for viewing a single baker, updating a single baker, or removing a single baker"""
	serializer_class = BakerSerializer
	def get(self, request, pk):
		baker = get_object_or_404(Baker, pk=pk)
		serializer = BakerSerializer(baker)
		return Response({'baker': serializer.data})
	
	def patch(self, request, pk):
		baker = get_object_or_404(Baker, pk=pk)
		serializer = BakerSerializer(baker, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		baker = get_object_or_404(Baker, pk=pk)
		baker.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
