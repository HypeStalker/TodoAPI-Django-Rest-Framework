from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Task



class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    detail_url = serializers.HyperlinkedIdentityField(view_name="todo_detail", lookup_field="pk")
    author_url = serializers.HyperlinkedIdentityField(view_name="user_detail", lookup_field="pk")
    class Meta:
        model = Task
        fields = [
            "detail_url",
            "id",
            "author",
            "author_url",
            "body",
            "isCompleted",
            "created_at",
            "edited_at",
            ]

class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user_detail", lookup_field="pk")
    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "username",
        ]