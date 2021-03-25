from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView

from team.models import Team
from team.team_serializer import TeamSerializer


class TeamAPIView(ListCreateAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Team.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = TeamSerializer
