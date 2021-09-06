from django.contrib import admin
from django.urls import path

from .views import micro_service1, micro_service2

urlpatterns = [
    path('service1/', micro_service1, name='service1'),
    path('service2/', micro_service2, name='service2'),
]
