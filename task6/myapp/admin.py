from django.contrib import admin
from .models import UserTable, Category, Post, PostImages
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(UserTable)
class user_table(admin.ModelAdmin):
    list_display = ('name', 'profile_pic_tag', 'email', 'phone', 'bio', 'joined_at', 'active')
    
    def profile_pic_tag(self, obj):
        if obj.profile_pic:
            return mark_safe(f'<img src="{obj.profile_pic.url}" width="100px" />')
        return "No Image"
    profile_pic_tag.short_description = 'Image'
    

@admin.register(Category)
class category(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')

@admin.register(Post)
class post(admin.ModelAdmin):
    list_display = ('title', 'content', 'categories', 'created_at', 'updated_at', 'published', 'views')

@admin.register(PostImages)
class post_images(admin.ModelAdmin):
    list_display = ('post', 'image_tag')
    
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px" />')
        return "No Image"
    image_tag.short_description = 'Image'