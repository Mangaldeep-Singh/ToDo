from django.http import HttpResponse
from django.shortcuts import render
from ToDo.models import Task
def home(request):
    task = Task.objects.filter(is_completed=False).order_by('-modified_at')
    completed = Task.objects.filter(is_completed=True).order_by('-modified_at')
    context = {
        'tasks': task,
        'completed': completed,
    }
    return render(request,'home.html',context)