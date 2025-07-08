from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

choices = [
    ('politics', 'Politics'),
    ('sports', 'Sports'),
    ('business', 'Business'),
]

class newsArticle(models.Model):
    news_title = models.CharField(max_length=100)
    news_type = models.CharField(max_length=100, choices=choices)
    news_desc = models.TextField()
    news_date = models.DateField()
    news_image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    news_tags = models.CharField(max_length=100, blank=True, null=True)