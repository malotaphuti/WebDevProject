<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
   # path('register/', views.register, name='register'),
   # path('login/', views.login, name='login'),
    path('pending_documents/', views.pending_documents, name='pending_documents'),
    path('review_document/<int:document_id>/', views.review_document, name='review_document'),
    path('manual_documents/', views.upload_folder_documents, name='manual_documents'),
]
=======
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path("", views.home, name="home"), 
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('', include(router.urls)),
]

>>>>>>> fd96fa894f51faa6a89861552f97c3c68ac90a1d
