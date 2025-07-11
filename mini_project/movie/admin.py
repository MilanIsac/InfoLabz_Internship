from django.contrib import admin
from .models import Country, State, City, Actor, User, Director, Category, Movie, Review, WatchList

# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state_name', 'country_id')
    search_fields = ('state_name',)
    
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'state_id')
    search_fields = ('city_name',)
    
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'state', 'city', 'actor_image', 'bio', 'nationality', 'awards', 'gender', 'birth_date')
    list_per_page = 10
    search_fields = ('name',)
    list_filter = ['country',]
    list_editable = ('name',)
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'user_image', 'phone', 'status', 'date_joined', 'gender', 'state', 'city', 'country')
    search_fields = ('name',)
    list_filter = ['country',]
    
@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'state', 'city', 'director_image', 'bio', 'nationality', 'awards', 'gender')
    search_fields = ('name',)
    list_filter = ['country',]
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ['name',]
    list_editable = ('name',)
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'director', 'release_year', 'description', 'trailer_link', 'actors', 'created_at')
    search_fields = ('title',)
    list_filter = ['category', 'director']
    list_editable = ('title', 'category', 'director', 'release_year', 'description', 'trailer_link')
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie', 'rating', 'comment', 'created_at')
    list_filter = ['user', 'movie']
    search_fields = ('user__name', 'movie__title', 'comment')
    list_editable = ('rating',)
    
@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie', 'added_at')
    list_filter = ['user',]
    search_fields = ('user__name', 'movie__title')
    list_editable = ('movie',)