from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views 

# app_name = "account"

urlpatterns = [
    # path('login/', views.user_login, name="login"),
    path('', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name= 'register'),
    path('edit/', views.edit, name="edit"),
]