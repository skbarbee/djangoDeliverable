from django.urls import path
from .views import DonutsView, DonutDetailView

urlpatterns = [
	path('',DonutsView.as_view(), name='donuts'),
	path('<int:pk>/',DonutDetailView.as_view(), name='donut')

]