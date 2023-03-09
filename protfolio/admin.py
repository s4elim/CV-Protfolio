from .models import Profile
from django.contrib import admin


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'mail', 'phone', 'created_at')
    
admin.site.register(Profile, ProfileAdmin)