from django.urls import path
from . import views

urlpatterns = [
  path('', views.signup, name='home'),
  path('dash/', views.home, name='dash'),
  path('accounts/signup/', views.signup, name="signup"),
  path('jobs/', views.jobs_index, name='index'),
  path('jobs/<int:job_id>/', views.jobs_detail, name='detail'),
  path('jobs/create/', views.JobCreate.as_view(), name='jobs_create'),
  path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='jobs_update'),
  path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='jobs_delete'),
  path('jobs/<int:job_id>/add_todo/', views.add_todo, name='add_todo'),
  path('jobs/<int:job_id>/update_todo/<int:todo_id>/', views.update_todo, name='update_todo'),
  path('jobs/<int:job_id>/delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
  path('jobs/<int:job_id>/add_status/', views.add_status, name='add_status'),
  path('jobs/<int:job_id>/delete_status/<int:status_id>/', views.delete_status, name='delete_status'),
  path('connections/', views.connections_index, name='connections_index'),
  path('connections/<int:connection_id>', views.connections_detail, name='connections_detail'),
  path('connections/create/', views.ConnectionCreate.as_view(), name='connections_create'),
  path('connections/<int:pk>/update/', views.ConnectionUpdate.as_view(), name='connections_update'),
  path('connections/<int:pk>/delete/', views.ConnectionDelete.as_view(), name='connections_delete'),
]