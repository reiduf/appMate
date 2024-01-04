from django.urls import path
from . import views

urlpatterns = [
  path('', views.signup, name='home'),
  path('accounts/signup/', views.signup, name="signup"),
  path('jobs/', views.jobs_index, name='index'),
  path('jobs/<int:job_id>/', views.jobs_detail, name='deatail'),
  path('jobs/create/', views.JobCreate.as_view(), name='jobs_create'),
  path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='jobs_update'),
  path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='jobs_delete'),
]