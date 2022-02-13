from django.contrib import admin

# Register your models heregit .
from .models import BlogModel, Profile

admin.site.register(BlogModel)
admin.site.register(Profile)