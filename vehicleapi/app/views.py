from django.shortcuts import render
from rest_framework.views import APIView
from app.models import Vehicle
from app.serializers import VehicleSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.
class VehicleCreate(APIView):
    def post(self,request):
        data=request.data
        serializer_instance=VehicleSerializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
class VehicleList(APIView):
    def get(self,request):
        qs=Vehicle.objects.all()
        serializer_instance=VehicleSerializer(qs,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
class VehicleRetrieve(APIView):
    def get(self,request,pk):
        v=get_object_or_404(Vehicle,id=pk)
        serializer_instance=VehicleSerializer(v)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
class VehicleUpdate(APIView):
    def put(self,request,pk):
        data=request.data
        v=get_object_or_404(Vehicle,id=pk)
        serializer_instance=VehicleSerializer(instance=v,data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

class VehiclepartialUpdate(APIView):
    def patch(self,request,pk):
        data=request.data
        v=get_object_or_404(Vehicle, id=pk)
        serializer_instance=VehicleSerializer(instance=v,data=data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class VehicleDelete(APIView):
    def delete(self,request,pk):
        v=get_object_or_404(Vehicle,id=pk)
        v.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

