from .models import Car, Truck, Boat
from .serializers import CarSerializer, TruckSerializer, BoatSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# cars
@api_view(['GET', 'POST'])
def car_list(request, format=None):

    permission_classes = (IsAuthenticated,)
    if request.method == 'GET':
        try:
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)
        except:
            Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        try:
            serializer = CarSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        except:
            Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, id, format=None):
    permission_classes = (IsAuthenticated,)

    try:
        car = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# trucks
@api_view(['GET', 'POST'])
def truck_list(request, format=None):

    permission_classes = (IsAuthenticated,)
    if request.method == 'GET':
        try:
            trucks = Truck.objects.all()
            serializer = TruckSerializer(trucks, many=True)
            return Response(serializer.data)
        except:
            Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        try:
            serializer = TruckSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        except:
            Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def truck_detail(request, id, format=None):
    permission_classes = (IsAuthenticated,)

    try:
        truck = Truck.objects.get(pk=id)
    except truck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TruckSerializer(truck)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TruckSerializer(truck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# boat
@api_view(['GET', 'POST'])
def boat_list(request, format=None):

    permission_classes = (IsAuthenticated,)
    if request.method == 'GET':
        try:
            boats = Boat.objects.all()
            serializer = BoatSerializer(boats, many=True)
            return Response(serializer.data)
        except:
            Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        try:
            serializer = BoatSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        except:
            Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def boat_detail(request, id, format=None):
    permission_classes = (IsAuthenticated,)

    try:
        boat = Boat.objects.get(pk=id)
    except boat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BoatSerializer(boat)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BoatSerializer(boat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        boat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)