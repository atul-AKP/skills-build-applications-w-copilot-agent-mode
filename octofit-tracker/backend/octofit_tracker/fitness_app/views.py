from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserView(APIView):
    def get(self, request):
        return Response({"message": "User GET endpoint"}, status=status.HTTP_200_OK)

class TeamView(APIView):
    def get(self, request):
        return Response({"message": "Team GET endpoint"}, status=status.HTTP_200_OK)

class ActivityView(APIView):
    def get(self, request):
        return Response({"message": "Activity GET endpoint"}, status=status.HTTP_200_OK)

class LeaderboardView(APIView):
    def get(self, request):
        return Response({"message": "Leaderboard GET endpoint"}, status=status.HTTP_200_OK)

class WorkoutView(APIView):
    def get(self, request):
        return Response({"message": "Workout GET endpoint"}, status=status.HTTP_200_OK)
