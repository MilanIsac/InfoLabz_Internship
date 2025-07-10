from django.contrib import admin
from .models import Country, State, City, Actor, User, Director, Category, Movie, Review, WatchList

# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state_name', 'country_id')
    
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'state_id')
    
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'state', 'city', 'actor_image', 'bio', 'nationality', 'awards', 'gender', 'birth_date')
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'user_image', 'phone', 'status', 'date_joined', 'gender', 'state', 'city', 'country')
    
@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'state', 'city', 'director_image', 'bio', 'nationality', 'awards', 'gender')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'director', 'release_year', 'description', 'trailer_link', 'actors', 'created_at')
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie', 'rating', 'comment', 'created_at')
    
@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie', 'added_at')