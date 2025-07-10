from django.contrib import admin
from .models import User, Author, Category, News, Comments, Likes
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'timestamp', 'profile_pic_tag')
    
    def profile_pic_tag(self, obj):
        if obj.profile_pic:
            return mark_safe(f'<img src="{obj.profile_pic.url}" width="100px" />')
        return "No Image"
    profile_pic_tag.short_description = 'Image'
    
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'bio', 'timestamp', 'total_news', 'phone', 'profile_pic_tag')
    
    def profile_pic_tag(self, obj):
        if obj.profile_pic:
            return mark_safe(f'<img src="{obj.profile_pic.url}" width="100px" />')
        return "No Image"
    profile_pic_tag.short_description = 'Image'
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'timestamp', 'image_tag')
    
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px" />')
        return "No Image"
    image_tag.short_description = 'Image'
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'category', 'timestamp', 'is_published', 'updated_at', 'image_tag')
    
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px" />')
        return "No Image"
    image_tag.short_description = 'Image'
    
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('news', 'subject', 'user', 'timestamp', 'description')
    

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('news', 'user', 'timestamp')