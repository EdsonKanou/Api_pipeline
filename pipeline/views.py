from mon_api.models import Sensor
from .serializers import SensorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def liste(request):
    if request.method == 'GET':
        sensors = Sensor.objects.all()  # Utilisation du modèle Sensor
        serializer = SensorSerializer(sensors, many=True)  # Serializer mis à jour
        return JsonResponse({'Sensor': serializer.data})

    if request.method == 'POST':
        serializer = SensorSerializer(data=request.data)  # Serializer mis à jour
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'DELETE', 'OPTIONS'])
def uni(request, id):
    try:
        sensor_instance = Sensor.objects.get(id=id)  # Utilisation du modèle Sensor
    except Sensor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT' or request.method == 'OPTIONS':
        serializer = SensorSerializer(sensor_instance, data=request.data)  # Serializer mis à jour
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = SensorSerializer(sensor_instance)  # Serializer mis à jour
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'DELETE':
        sensor_instance.delete()
        return Response("Sensor deleted", status=status.HTTP_204_NO_CONTENT)
