
from django.urls import path
from . import views
from home.dash_apps.finished_apps import liveArduino


urlpatterns = [
    path('', views.home, name='home')
]
 


