from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('hello/', views.profiles, name="profiles"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
]
