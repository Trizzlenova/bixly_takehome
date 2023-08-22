from django.test import TestCase
from django.test import Client
from .models import Car

# Create your tests here.
class CarModelTest(TestCase):
    def test_car_model_exists(self):
        cars = Car.objects.count()
        self.assertEqual(cars, 0)
    
    def test_str_representation(self):
        car = Car.objects.create(make='Subaru', model='Impreza', year=2016)
        self.assertEqual(str(car), car.make)
    
    def get_car_list(self):
        c = Client()
        response = c.get('/cars/')
        self.assertEqual(response, 200)
