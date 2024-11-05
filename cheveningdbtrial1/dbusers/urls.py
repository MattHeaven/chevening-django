from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dbusers'


urlpatterns = [
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


]
