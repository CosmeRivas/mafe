from django.urls import path
from . import views

app_name = 'mafeapp'

urlpatterns = [
    path('', views.home, name='home'),
]
