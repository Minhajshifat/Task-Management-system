from django.shortcuts import render
from task.models import TaskModel
def home(request):
    post=TaskModel.objects.all()
    return render(request,'home.html',{'post':post})