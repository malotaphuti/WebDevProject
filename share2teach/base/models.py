from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    
    title = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)  # Store the file path manually
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_documents')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
