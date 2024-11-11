from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Your email address", required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    message = forms.CharField(label="Type your message...", required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'5'}))

class ProfileForm(forms.Form):
    # salutation = forms.ChoiceField(choices=[('Mr', 'Mr'), ('Ms', 'Ms'), ('Dr', 'Dr')], required=True)
    first_name = forms.CharField(max_length=100, required=True)
    surname = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    organisation = forms.CharField(max_length=200, required=True)
    job_title = forms.CharField(max_length=100, required=True)
    sector = forms.CharField(max_length=100, required=True)
    year_of_chevening_award = forms.IntegerField(required=True)
    university = forms.CharField(max_length=200, required=True)
    course = forms.CharField(max_length=200, required=True)    
