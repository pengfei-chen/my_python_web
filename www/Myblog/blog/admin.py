from django.contrib import admin

# Register your models here.

from .models import Blog
# admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=("title", "create_time", "count")
    
