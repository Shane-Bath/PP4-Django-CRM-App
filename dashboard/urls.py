from . import views
from django.urls import path

urlpatterns = [

    path('task-update/<int:pk>',
         views.UpdateTask.as_view(),
         name='task-update'),
    path('delete-task/<int:pk>',
         views.DeleteTask.as_view(),
         name='delete-task'),
    path('delete-call/<int:pk>',
         views.DeleteCall.as_view(),
         name='delete-call'),
]
