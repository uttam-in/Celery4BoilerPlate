from django.contrib import admin
from django.urls import path,include
from scheduler.views import CeleryTasks

urlpatterns = [
    path("schedule/", CeleryTasks.as_view(), name='schedule')
]