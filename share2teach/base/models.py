from django.db import models
<<<<<<< HEAD
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
=======
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    ADMIN = 'admin'
    EDUCATOR = 'educator'
    MODERATOR = 'moderator'

    USER_TYPES = [
        (ADMIN, 'Admin'),
        (EDUCATOR, 'Educator'),
        (MODERATOR, 'Moderator'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPES, default=EDUCATOR)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

>>>>>>> fd96fa894f51faa6a89861552f97c3c68ac90a1d
