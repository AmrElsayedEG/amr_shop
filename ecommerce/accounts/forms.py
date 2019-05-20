from django import forms
from django.contrib.auth.models import User

from . import models

class profileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['country','img','tel','about_me','city']

class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']