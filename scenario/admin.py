from django.contrib import admin

# Register your models here.
from .models import Scenario, Platform, MachineType, Configuration, Results

admin.site.register(Scenario)
admin.site.register(Platform)
admin.site.register(MachineType)
admin.site.register(Configuration)
admin.site.register(Results)
