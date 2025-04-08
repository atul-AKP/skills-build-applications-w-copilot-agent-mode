"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from fitness_app.views import UserView, TeamView, ActivityView, LeaderboardView, WorkoutView
from rest_framework.decorators import api_view
from rest_framework.response import Response

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/users/', UserView.as_view(), name='user-list'),
    path('api/teams/', TeamView.as_view(), name='team-list'),
    path('api/activities/', ActivityView.as_view(), name='activity-list'),
    path('api/leaderboard/', LeaderboardView.as_view(), name='leaderboard-list'),
    path('api/workouts/', WorkoutView.as_view(), name='workout-list'),
]

# Add api_root for the base API endpoint
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/',
    })

urlpatterns.append(path('', api_root, name='api-root'))
