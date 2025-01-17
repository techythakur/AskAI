
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('suggest/', views.suggest,name='suggest'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('register/', views.register_user,name='register'),
    path('history/', views.history,name='history'),
    path('delete-history/', views.delete_history,name='delete-history'),
]
