from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def add_task(request):
   if request.method== "POST":
      taskform=forms.taskform(request.POST)
      if taskform.is_valid():
         taskform.save()
         return redirect('home')
   else:
      taskform=forms.taskform()
   return render(request,'add_task.html',{'form':taskform})

def edit_post(request,id):
    post=forms.TaskModel.objects.get(pk=id)
    taskform=forms.taskform(instance=post)
    if request.method== "POST":
      taskform=forms.taskform(request.POST,instance=post)
      if taskform.is_valid():
         taskform.save()
         return redirect('home')
    return render(request,'add_task.html',{'form':taskform})
def delete_post(request,id):
    post = models.TaskModel.objects.get(pk=id) 
    post.delete()
    return redirect('home')