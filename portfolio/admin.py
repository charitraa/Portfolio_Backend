from django.contrib import admin
from django.utils.html import format_html
from .models import PortfolioItem

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'type', 'created_at', 'updated_at', 'image_tag')
    
    # Add search box for these fields
    search_fields = ('title', 'type', 'description')
    
    # Add filters on the right sidebar
    list_filter = ('type', 'created_at', 'updated_at')
    
    # Fields that are clickable in the list view
    list_display_links = ('title',)
    
    # Default ordering
    ordering = ('-created_at',)
    
    # Read-only fields
    readonly_fields = ('id', 'created_at', 'updated_at', 'image_tag')
    
    # Show image preview in admin
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image Preview'
