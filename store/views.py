from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 

from .models import Store
from .serializers import StoreSerializer
# Create your views here.


class StoresView(APIView):
	"""View class for stores/ for viewing and creating"""
	def get(self, request):
		stores = Store.objects.all()
		serializer = StoreSerializer(stores, many = True)
		return Response({'stores': serializer.data})

	def post(self, request):
		serializer = StoreSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetailView(APIView):
	"""	View class for stores/:pk for viewing a single Store, updating a single Store, or removing a single Store"""
	def get(self, request, pk):
		store = get_object_or_404(Store, pk=pk)
		serializer = StoreSerializer(store)
		return Response({'Store': serializer.data})
	
	def patch(self, request, pk):
		store = get_object_or_404(Store, pk=pk)
		serializer = StoreSerializer(store, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		store = get_object_or_404(Store, pk=pk)
		store.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
