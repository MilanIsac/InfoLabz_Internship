from django.contrib import admin
from .models import newsArticle
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(newsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_type', 'news_date', 'news_desc', 'news_image_tag', 'news_tags')

    def news_image_tag(self, obj):
        if obj.news_image:
            return mark_safe(f'<img src="{obj.news_image.url}" width="100" height="100" />')
        return "No Image"
    
    news_image_tag.short_description = 'Image'