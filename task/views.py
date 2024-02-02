from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Task
# Create your views here.

user = User.objects.get(username='user1')  # Припустимо, що такий користувач існує
task = Task.objects.create(title='Завдання 1', description='Опис завдання 1', assigned_to=user)


task = Task.objects.get(title='Завдання 1')
task.status = 'виконано'
task.save()


new_user = User.objects.get(username='user2')  # Припустимо, що такий користувач існує
task = Task.objects.get(title='Завдання 1')
task.assigned_to = new_user
task.save()