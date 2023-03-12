from django.urls import path
from .import views

urlpatterns = [
    path('',views.home_view,name = 'home'),
    path('todo/new/',views.addTask,name = 'todo_new'),
    path('todo/<int:pk>/edit/',views.editTask,name = 'edit_todo'),
    path('todo/<pk>/remove/',views.todo_remove,name = 'todo_remove'),
    path("register",views.register,name="register"),
    path('users',views.get_allUsers,name = 'users'),
    path('todo/task_assign/',views.assign_task,name = 'assign'),
]