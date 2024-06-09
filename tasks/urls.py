from django.urls import path
from  .import views

urlpatterns = [path('', views.home, name='home'),
               path('add', views.add_task, name='add'),
               path('delete/<str:task_id>', views.delete_task, name='delete'),
               path('detail/<str:task_id>', views.detail_task, name='detail'),
               path('completed', views.completed, name='completed'),
               path('remaining', views.remaining, name='remaining'),
               path('change_complete/<str:task_id>', views.change_complete, name="change_status"),
               path('remove/<str:task_id>', views.remove_task, name="remove")
               ]