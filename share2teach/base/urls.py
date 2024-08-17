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
