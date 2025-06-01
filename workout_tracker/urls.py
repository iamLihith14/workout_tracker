"""workout_tracker URL Configuration

Points our project to our workout application.
"""
from django.urls import re_path, include

urlpatterns = [
    re_path(r'^', include("apps.workout.urls")),
]
