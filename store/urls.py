from django.urls import path
from .views import StoresView, StoreDetailView

urlpatterns = [
	path('',StoresView.as_view(), name='donuts'),
	path('<int:pk>/',StoreDetailView.as_view(), name='donut')

]