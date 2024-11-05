from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Your email address", required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    message = forms.CharField(label="Type your message...", required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'5'}))