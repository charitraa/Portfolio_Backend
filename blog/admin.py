from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'created_at', 'updated_at')
    
    # Add search box for these fields
    search_fields = ('title', 'content')
    
    # Add filters on the right sidebar
    list_filter = ('created_at', 'updated_at')
    
    # Fields that are clickable in the list view
    list_display_links = ('title',)
    
    # Default ordering
    ordering = ('-created_at',)

    # Optional: make slug field or id read-only
    readonly_fields = ('id', 'created_at', 'updated_at')

