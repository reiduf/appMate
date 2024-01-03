from django.urls import path
from . import views

urlpatterns = [
  path('', views.signup, name='home'),
  path('accounts/signup/', views.signup, name="signup"),
  path('jobs/', views.jobs_index, name='index'),
  path('jobs/<int:job_id>/', views.jobs_detail, name='deatail'),
  

]