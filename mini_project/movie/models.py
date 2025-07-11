from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

gender_choices = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class State(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.state_name
    
class City(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city_name
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='actor_pics/')
    bio = models.TextField()
    nationality = models.CharField(max_length=50)
    awards = models.TextField()
    gender = models.CharField(max_length=100, choices=gender_choices)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name
    
    
    def actor_image(self):
        if self.profile_pic:
            return mark_safe('<img src={} width="50" height="50" />'.format(self.profile_pic.url))

        return "No Image"
    
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='user_pics/')
    phone = models.CharField(max_length=15)
    status = models.BooleanField(default=True)
    date_joined = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=100, choices=gender_choices)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def user_image(self):
        if self.profile_pic:
            return mark_safe('<img src={} width="50" height="50" />'.format(self.profile_pic.url))

        return "No Image"
    
    
class Director(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='director_pics/')
    bio = models.TextField()
    nationality = models.CharField(max_length=50)
    awards = models.TextField()
    gender = models.CharField(max_length=100, choices=gender_choices)
    
    def __str__(self):
        return self.name
    
    def director_image(self):
        if self.profile_pic:
            return mark_safe('<img src={} width="50" height="50" />'.format(self.profile_pic.url))

        return "No Image"
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_year = models.IntegerField()
    trailer_link = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ForeignKey(Actor, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    
class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateField(auto_now_add=True)