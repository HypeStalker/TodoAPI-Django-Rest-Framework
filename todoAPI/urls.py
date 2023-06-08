from django.urls import path

from .views import ListTasks, DetailTasks, ListUsers, DetailUsers

urlpatterns = [
    path("", ListTasks.as_view(), name="todo_list"),
    path("<int:pk>/", DetailTasks.as_view(), name="todo_detail"),
    path("users/", ListUsers.as_view(), name="user_list"),
    path("users/<int:pk>/", DetailUsers.as_view(), name="user_detail"),
]
