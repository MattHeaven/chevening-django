from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static
from .forms import ProfileForm
from django.shortcuts import render, redirect
from django.contrib import admin
from .forms import ProfileForm
from .models import Profile
# from cheveningdbtrial1.dbusers import models

app_name = 'dbusers'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='dbusers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dbusers/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', views.contact, name='contact'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='dbusers/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='dbusers/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='dbusers/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='dbusers/password_reset_complete.html'), name='password_reset_complete'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile-details/', views.profile_details, name='profile_details'),
    path('profile_success/', views.profile_success, name='profile_success'),
    # path('gallery/', views.gallery, name='gallery'),
    # path('gallery/<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('gallery/', views.gallery_view, name='gallery_view'),
    path('events/', views.event_list, name='event_list'),  # URL for listing events
    path('events/<int:id>/', views.event_detail, name='event_detail'),  # URL for event detail
    path('newsletters/', views.newsletter_list, name='newsletter_list'),
]   

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            salutation = form.cleaned_data['salutation']
            first_name = form.cleaned_data['first_name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            organisation = form.cleaned_data['organisation']
            job_title = form.cleaned_data['job_title']
            sector = form.cleaned_data['sector']
            year_of_chevening_award = form.cleaned_data['year_of_chevening_award']
            university = form.cleaned_data['university']
            course = form.cleaned_data['course']
            # image = models.ImageField(upload_to='profile_pics', default='default.jpg')
            profile = Profile(salutation=salutation, first_name=first_name, surname=surname, email=email, phone_number=phone_number, organisation=organisation, job_title=job_title, sector=sector, year_of_chevening_award=year_of_chevening_award, university=university, course=course)
            return redirect('dbusers:profile_success')
            # return HttpResponseRedirect("Profile Successfully Created!Thanks", 'profile/success')
    else:
        form = ProfileForm()
    return render(request, 'dbusers/profile.html', {'form': form, 'profile_created': False})

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)