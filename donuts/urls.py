from django.urls import path
from .views.donut_views import DonutsView, DonutDetailView
from .views.baker_views import BakersView, BakerDetailView

urlpatterns = [
	path('donuts/',DonutsView.as_view(), name='donuts'),
	path('donuts/<int:pk>/',DonutDetailView.as_view(), name='donut'),
	path('bakers/',BakersView.as_view(), name='bakers'),
	path('bakers/<int:pk>/',BakerDetailView.as_view(), name='baker'),
	


]