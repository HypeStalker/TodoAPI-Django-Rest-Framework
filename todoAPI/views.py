from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User

from .models import Task
from .serializers import TaskSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class ListTasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class DetailTasks(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUsers(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer