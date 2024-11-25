from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    salutation = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    organisation = models.CharField(max_length=200, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)
    year_of_chevening_award = models.IntegerField(blank=True, null=True)
    university = models.CharField(max_length=200, blank=True, null=True)
    course = models.CharField(max_length=200, blank=True, null=True)
    other_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.first_name} {self.surname}"

    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
class Gallery(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
         return self.caption if self.caption else "Untitled Image"
       
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image', 'gallery')
    
admin.site.register(GalleryImage, GalleryImageAdmin)       

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)  # Optional image field

    def __str__(self):
        return self.title
    
class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='newsletters/', help_text='Upload the PDF file of the newsletter.')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    