from . import views
from django.urls import path

urlpatterns = [
    path('new-client/', views.CreateClient.as_view(), name='new-client'),
    path('call-log-form/', views.CallLog.as_view(), name='call-log-form'),
    path('task-list/', views.TaskList.as_view(), name='task-list'),
    path('task-update/<int:pk>', views.UpdateTask.as_view(), name='task-update'),
]
