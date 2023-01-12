from django.shortcuts import render
from projects import models, serializers
from rest_framework import viewsets

# Create your views here.


class ProjectInfo_ViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectInfo.objects.filter(show=True)
    serializer_class = serializers.ProjectInfo_Serializers
