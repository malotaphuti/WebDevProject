from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login as auth_login
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Document
from .forms import ModerationForm

import os

# Existing views
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from .models import CustomUser
from .forms import LoginForm
from .utils import send_verification_code  
from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer

# VIEWS START HERE
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to a dashboard or home page
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            #send_verification_code(user)
            return redirect('verify_account')
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def pending_documents(request):
    """List all pending documents for the moderator to review"""
    documents = Document.objects.filter(status='Pending')
    return render(request, 'pending_documents.html', {'documents': documents})

@login_required
def review_document(request, document_id):
    """Allow moderator to review, approve, or reject a document"""
    document = get_object_or_404(Document, id=document_id)
    
    if request.method == 'POST':
        form = ModerationForm(request.POST)
        if form.is_valid():
            document.status = form.cleaned_data['status']
            document.feedback = form.cleaned_data['feedback']
            document.save()
            return redirect('pending_documents')  # Redirect back to the pending documents list
    else:
        form = ModerationForm()

    return render(request, 'review_document.html', {'document': document, 'form': form})

@login_required
def upload_folder_documents(request):
    """List files from a manually uploaded folder"""
    folder_path = os.path.join(settings.BASE_DIR, 'documents')  # Adjust folder path if needed
    files = os.listdir(folder_path)  # List all files in the manual folder

    documents = [{'title': file, 'path': os.path.join(folder_path, file)} for file in files]

    return render(request, 'manual_documents.html', {'documents': documents})

@login_required
@user_passes_test(is_moderator)
def moderate_documents(request):
    """Allow moderators to view and moderate documents"""
    documents = Document.objects.filter(status='Pending')
    #comment
    if request.method == 'POST':
        doc_id = request.POST.get('doc_id')
        action = request.POST.get('action')
        document = get_object_or_404(Document, id=doc_id)
        document.moderated_by = request.user
        if action == 'publish':
            document.status = 'Published'
        elif action == 'reject':
            document.status = 'Rejected'
        document.save()
        return redirect('moderate_documents')

    return render(request, 'moderate_documents.html', {'documents': documents})


@login_required
def upload_document(request):
    """Handle the document upload"""
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.uploaded_by = request.user
            document.save()
            return redirect('pending_documents')  # Redirect to the pending documents list or another page
    else:
        form = DocumentUploadForm()

    return render(request, 'upload_document.html', {'form': form})

def verify_account(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            user = CustomUser.objects.get(verification_code=code)
            user.is_active = True
            user.save()
            return redirect('login')
        except CustomUser.DoesNotExist:
            # Handle error (e.g., render with an error message)
            pass
    return render(request, 'auth/verify.html')
