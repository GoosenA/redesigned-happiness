from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Scenario, Platform, Configuration, MachineType, Results
from .serializers import ScenarioSerializer, PlatformSerializer, ConfigurationSerializer, MachineTypeSerializer, ResultsSerializer
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

class ScenarioApiView(APIView):
    

    def get(self, request, *args, **kwargs):
        '''
        List scenario
        '''

        scenarios = Scenario.objects.filter()
        serializer = ScenarioSerializer(scenarios, many=True)

        # for s in serializer.data:
        #     print(s)

        # context = {"data": serializer.data}
        # return render(request, "index.html", context)

        return Response(serializer.data, status=status.HTTP_200_OK)

class PlatformApiView(APIView):
    def get(self, request, *args, **kwargs):
        platforms = Platform.objects.filter()
        serializer = PlatformSerializer(platforms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class ConfigurationApiView(APIView):
    def get(self, request, *args, **kwargs):
        configs = Configuration.objects.filter()
        serializer = ConfigurationSerializer(configs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MachineTypeApiView(APIView):
    def get(self, request, *args, **kwargs):
        machine_type = MachineType.objects.filter()
        serializer = MachineTypeSerializer(machine_type, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ResultsApiView(APIView):
    def get(self, request, *args, **kwargs):
        machine_type = Results.objects.filter()
        serializer = ResultsSerializer(machine_type, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)