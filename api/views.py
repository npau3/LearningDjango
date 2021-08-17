from django.shortcuts import render
from main.models import Task
from rest_framework import viewsets, permissions
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



#Create your views here.
