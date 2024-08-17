from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"), 
    path("register/", views.register, name="register" ),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]

