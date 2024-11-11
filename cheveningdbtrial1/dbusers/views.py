from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .forms import ProfileForm, UserRegisterForm, ContactForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile
from .models import GalleryImage
from .models import Gallery
from .models import Event
from .models import Newsletter
def home(request):
    return render(request, 'dbusers/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Hi {email}, your account was created successfully!')
            return redirect('dbusers:profile')
        else:
            messages.error(request, 'Error creating your account. Please try again.')
    else:
        form = UserRegisterForm() 
    return render(request, 'dbusers/register.html', {'form': form})

def login(request):
    return render(request, 'dbusers/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
    return redirect('dbusers:home')  # Adjust this according to your URL configuration

def profile(request):
    return render(request, 'dbusers/profile.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            message = form.cleaned_data.get('message')
            email_inquiry(name=name, email=email, message=message, subject="Lab Tutorials")
            messages.success(request, "Email was sent successfully!")
            return redirect('dbusers:contact')
        else:
            messages.error(request, "Error processing email, please try again.")
    else:
        form = ContactForm()
    
    return render(request, 'emailapp/contact.html', {'form': form})

def email_inquiry(name, email, message, subject):
    msg_plain = render_to_string('emailapp/email_inquiry.txt', {
        'contactName': name, 
        'contactEmail': email, 
        'contactMessage': message,
    })
    msg_html = render_to_string('emailapp/email_inquiry.html', {
        'contactName': name, 
        'contactEmail': email, 
        'contactMessage': message,
    })
    send_mail(
        subject=subject,
        message=msg_plain,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        html_message=msg_html
    )

def create_profile(request):    
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            Profile.objects.create(**form.cleaned_data)
            messages.success(request, "Profile created successfully!")
            return redirect('dbusers:profile')
        else:
            messages.error(request, "Error creating profile. Please check your inputs.")
    else:
        form = ProfileForm()
    
    return render(request, 'dbusers/create_profile.html', {'form': form})

def profile_success(request):       
    return render(request, 'dbusers/profile_success.html')

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'dbusers/gallery.html', {'images': images})

def gallery_view(request):
    galleries = Gallery.objects.prefetch_related('images').all()
    return render(request, 'dbusers/gallery.html', {'galleries': galleries})

def event_list(request):
    events = Event.objects.all()  # Get all events
    return render(request, 'dbusers/events.html', {'events': events})

def event_detail(request, id):
    event = Event.objects.get(id=id)  # Get the event by ID
    return render(request, 'dbusers/event_detail.html', {'event': event})

def newsletter_list(request):
    newsletters = Newsletter.objects.all()
    return render(request, 'dbusers/newsletters/newsletter_list.html', {'newsletters': newsletters})
