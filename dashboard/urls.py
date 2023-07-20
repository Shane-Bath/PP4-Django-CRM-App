from . import views
# from .views import CustomLoginView
from django.urls import path

urlpatterns = [
    path('new-client/', views.CreateClient.as_view(), name='new-client'),
    path('task-update/<int:pk>', views.UpdateTask.as_view(), name='task-update'),
    path('delete-task/<int:pk>', views.DeleteTask.as_view(), name='delete-task'),
    path('delete-call/<int:pk>', views.DeleteCall.as_view(), name='delete-call'),
]
