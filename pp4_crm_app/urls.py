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
# from dashboard.views import CustomLoginView, SignupView, LogoutView, PasswordChangeView, PasswordResetView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.index, name='index'),
    path('new-client', include('dashboard.urls'), name='new-client'),
    path('dashboard/call-log-form/', views.CallLog.as_view(), name='call-log-form'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('client-search/', views.client_search, name='client_search'),
    path('client-list/', views.display_clients, name='client-list'),
    path('dash-client-list/', views.client_list, name='dash_client'),
    path('<int:id>/', views.clients_file, name='details'),
    path('edit-note/<int:id>/', views.display_note, name='edit-note'),
    path('edit-client/<int:id>/', views.update_client, name='edit-client'),
    path('task/', views.display_task, name='task'),
    path('task-update', include('dashboard.urls'), name='task-update'),
    path('delete-task', include('dashboard.urls'), name='delete-task'),
    path('delete-call', include('dashboard.urls'), name='delete-call'),
    path('display-call/', views.DisplayCallLog.as_view(), name='display-call'),
    path('task-list/', views.TaskList.as_view(), name='task-list'),
    path('<int:id>/note/', views.display_client_note, name='note'),
    path('note/<int:pk>/delete', views.DeleteNote.as_view(), name='delete-note'),
]
