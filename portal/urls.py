from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('employer-dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('seeker-dashboard/', views.seeker_dashboard, name='seeker_dashboard'),
    path('post-job/', views.post_job, name='post_job'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
]






