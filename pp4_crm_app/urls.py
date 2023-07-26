from django.contrib import admin
from django.urls import path, include
from dashboard import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.index, name='index'),
    path('new-client/', views.CreateClient.as_view(), name='new-client'),
    path('call-log-form/', views.CallLog.as_view(), name='call-log-form'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('client-search/', views.client_search, name='client_search'),
    path('client-list/', views.display_clients, name='display-clients'),
    # path('client-list/', views.DiplayClients.as_view(), name='display-clients'),
    path('<int:id>/', views.clients_file, name='details'),
    path('edit-note/<int:id>/', views.display_note, name='edit-note'),
    path('edit-client/<int:id>/', views.update_client, name='edit-client'),
    path('task/', views.display_task, name='task'),
    path('display-call/', views.DisplayCallLog.as_view(), name='display-call'),
    path('task-list/', views.TaskList.as_view(), name='task-list'),
    path('<int:id>/note/', views.display_client_note, name='note'),
    path('note/<int:pk>/delete', views.DeleteNote.as_view(), name='delete-note'),
    path('task-update/<int:pk>', views.UpdateTask.as_view(), name='task-update'),
    path('delete-task/<int:pk>', views.DeleteTask.as_view(), name='delete-task'),
    path('delete-call/<int:pk>', views.DeleteCall.as_view(), name='delete-call'),
]
