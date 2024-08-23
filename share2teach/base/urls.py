from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views




urlpatterns = [
    path("",views.home, name="home"), 
    path("register/",views.register, name="register"),
    path("login/",views.login, name="login"),
    path("logout/",views.logout, name="logout"),
    path("pending_documents/",views.pending_documents, name="pending_documents"),
    path('review_document/<int:id>/', views.review_document, name='review_document'), 
    path("manual_documents/",views.upload_folder_documents, name="manual_documents"),
    #path('moderate/', moderate_documents, name='moderate_documents'),
    #path('upload/', upload_document, name='upload_document'),
    # urls.py



    # ... other URL patterns
    path('upload/', views.upload_document, name='upload_document'),
    
 
]
