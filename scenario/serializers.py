

from rest_framework import serializers

from .models import Scenario, Platform, MachineType, Configuration, Results

class ScenarioSerializer(serializers.ModelSerializer):
    platform_name = serializers.CharField(source='platform.description')
    machine_type_name = serializers.CharField(source='machine_type.description')
    configuration_name = serializers.CharField(source='configuration.description')
    
    results_ = serializers.SerializerMethodField()

    def get_results_(self, scenario_id):
        pesticide_qs = Results.objects.filter(scenario_id=scenario_id)
        return ResultsSerializer(pesticide_qs, many=True).data

    class Meta:
        model = Scenario
        fields = ["description","mandatory","platform_name","machine_type_name", "configuration_name", "results_"]


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ["id", "description"]

class MachineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineType
        fields = ["id", "description"]

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ["id", "description"]

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ["id", "scenario_id", "result"]