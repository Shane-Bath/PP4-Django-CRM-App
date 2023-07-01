from . import views
from django.urls import path

urlpatterns = [
    path('new-client/', views.CreateClient.as_view(), name='new-client'),
    path('call-log-form/', views.CallLog.as_view(), name='call-log-form'),
]