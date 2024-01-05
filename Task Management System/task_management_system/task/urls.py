from django.urls import path,include
from . import views


urlpatterns = [
    path('addtask/', views.add_task,name="addtask"),
    path('edit/<int:id>/', views.edit_post, name='editpost'),
    path('delete/<int:id>', views.delete_post, name='deletepost'),
]