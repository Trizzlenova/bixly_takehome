from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list, name='car_list'),
    path('cars/<int:id>', views.car_detail, name='car_detail'),
    path('trucks/', views.truck_list, name='truck_list'),
    path('trucks/<int:id>', views.truck_detail, name='truck_detail'),
    path('boats/', views.boat_list, name='boat_list'),
    path('boats/<int:id>', views.boat_detail, name='boat_detail'),
]
