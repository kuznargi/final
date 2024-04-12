
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'Image', 'password1', 'password2','gender','phone','status']
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-box'}),
            'email': forms.EmailInput(attrs={'class': 'input-box'}),
            'first_name': forms.TextInput(attrs={'class': 'input-box'}),
            'last_name': forms.TextInput(attrs={'class': 'input-box'}),
            'Image': forms.FileInput(attrs={'class': 'img-input'}),
            'gender':forms.Select(attrs={'class': 'input-box'}),
            'phone': forms.NumberInput(attrs={'class': 'input-box'}),
            'status': forms.Select(attrs={'class': 'input-box'}),
            # 'college': forms.Select(attrs={'class': 'input-box'}),
            'password1': forms.PasswordInput(attrs={'class': 'input-box'}),
            'password2': forms.PasswordInput(attrs={'class': 'input-box'}),
        }

# class UserEditForm(models.Model):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'first_name', 'last_name', 'Image', 'gender','phone','status']
        
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'input-box'}),
#             'email': forms.EmailInput(attrs={'class': 'input-box'}),
#             'first_name': forms.TextInput(attrs={'class': 'input-box'}),
#             'last_name': forms.TextInput(attrs={'class': 'input-box'}),
#             'Image': forms.FileInput(attrs={'class': 'img-input'}),
#             'gender':forms.Select(attrs={'class': 'input-box'}),
#             'phone': forms.NumberInput(attrs={'class': 'input-box'}),
#             'status': forms.Select(attrs={'class': 'input-box'}),
#             # 'college': forms.Select(attrs={'class': 'input-box'}),
            # 'password1': forms.PasswordInput(attrs={'class': 'input-box'}),
            # 'password2': forms.PasswordInput(attrs={'class': 'input-box'}),
        # }


    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Image', 'title', 'description', 'author']
        widgets={
            'Image': forms.FileInput(attrs={'class': 'img-input'}),
            'title': forms.TextInput(attrs={'class': 'input-box'}),
            'description': forms.TextInput(attrs={'class': 'input-box'}),
            'author': forms.TextInput(attrs={'class': 'input-box'}),
        }

class HomeWorkFormTeacher(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = ['Image', 'Title','Description','Mark']
        widgets={
            'Image': forms.FileInput(attrs={'class': 'img-input'}),
            'title': forms.TextInput(attrs={'class': 'input-box'}),
            'description': forms.TextInput(attrs={'class': 'input-box'}),
            'Mark': forms.NumberInput(attrs={'class': 'input-box'}),
        }
class HomeWorkStudent(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = ['homework','StudentComment']
        widgets={
            #  'homework' : forms.FileField(widget=forms.FileInput(attrs={'class': 'img-input'})),
              'homework' : forms.FileInput(attrs={'class': 'img-input'}),
            'StudentComment': forms.TextInput(attrs={'class': 'input-box'}),
        }
        