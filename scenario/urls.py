from django.urls import path

from . import views

urlpatterns = [
    path("", views.ScenarioApiView.as_view()),
    path("platforms", views.PlatformApiView.as_view()),
    path("machine_type", views.MachineTypeApiView.as_view()),
    path("configurations", views.ConfigurationApiView.as_view()),
    path("results", views.ResultsApiView.as_view()),

]