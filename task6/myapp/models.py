from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class UserTable(models.Model):
    name = models.CharField(max_length=100, null=False)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=False)
    phone = models.CharField(max_length=15, unique=True, null=False)
    bio = models.TextField(max_length=300)
    joined_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=300)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class PostImages(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_imgs/')
    
    def __str__(self):
        return self.post.title

