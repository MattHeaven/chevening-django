from django.contrib import admin
from .models import CustomUser, Profile
from .models import GalleryImage, Gallery
from .models import Event
from .models import Newsletter

admin.site.register(Event)
# Define the inline for GalleryImage
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

# Register the GalleryAdmin model with inline GalleryImages
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ('title',)

# Correctly register GalleryImage model (no need for inlines)
# admin.site.register(GalleryImage)

# CustomUser and Profile admin registrations
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('salutation', 'first_name', 'surname', 'email', 'phone_number', 'organisation', 'job_title', 'sector', 'year_of_chevening_award', 'university', 'course')
    search_fields = ('first_name', 'surname', 'email')      

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_uploaded', 'pdf_file')

admin.site.register(Newsletter, NewsletterAdmin)
