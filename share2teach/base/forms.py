from django import forms
from .models import Document, CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class ModerationForm(forms.Form):
    STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    feedback = forms.CharField(widget=forms.Textarea, required=False)


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    affiliation = forms.CharField(max_length=255, required=False)
    phone = forms.CharField(max_length=255, required=True)
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPES, required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2', 'affiliation', 'user_type')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if email and password:
            if self.user_cache is None:
                raise forms.ValidationError("Invalid email or password")
        return self.cleaned_data


class DocumentUploadForm(forms.ModelForm):
    """Form for uploading documents"""
    class Meta:
        model = Document
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file:
            raise forms.ValidationError("No file selected!")
        return file
