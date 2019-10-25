from django import forms
from .models import Project, Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profile_picture'] 
        exclude=['user']  

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']