from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login as auth_login
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Document
from .forms import ModerationForm

import os

# Existing views

def home(request):
    return render(request, 'home.html')

def register(request):
    # Your registration logic here
    return render(request, 'register.html')

def login(request):
    # Your login logic here
    return render(request, 'login.html')


# Document Moderation Views

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
