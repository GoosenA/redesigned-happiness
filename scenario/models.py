from django.db import models

# Create your models here.

class Platform(models.Model):
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.description


class MachineType(models.Model):
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.description


class Configuration(models.Model):
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.description

class Scenario(models.Model):
    description = models.CharField(max_length = 200)
    mandatory = models.BooleanField(default=True)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE)
    configuration = models.ForeignKey(Configuration, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Results(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    result = models.CharField(max_length=20)

    def __str__(self):
        return self.result
