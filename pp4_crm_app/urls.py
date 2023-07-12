"""PP4_CRM_APP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.index, name='index'),
    path('', include('dashboard.urls'), name='new-client'),
    path('', include('dashboard.urls'), name='call-log-form'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('client-search/', views.client_search, name='client_search'),
    path('client-list/', views.display_clients, name='client-list'),
    path('dash-client-list/', views.client_list, name='dash_client'),
    path('<int:id>/', views.clients_file, name='details'),
    path('edit-note/<int:id>/', views.display_note, name='edit-note'),
    path('<int:id>/note/', views.display_client_note, name='client-note'),
    path('edit-client/<int:id>/', views.update_client, name='edit-client'),
    path('display-call/', views.display_call_log, name='display-call'),
    path('', include('dashboard.urls'), name='task-list'),
    path('task/', views.display_task, name='task'),
    path('', include('dashboard.urls'), name='task-update'),
    path('', include('dashboard.urls'), name='delete-task'),
    path('dashboard/', views.CallLog.as_view(), name='dashboard'),
]
