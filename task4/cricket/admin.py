from django.contrib import admin
from .models import PlayerCategory, PlayerTeam, Player

# Register your models here.

@admin.register(PlayerCategory)
class PlayerCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_desc')
    
@admin.register(PlayerTeam)
class PlayerTeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team_desc')
    
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'player_category_id', 'player_team_id', 'player_runs', 'player_wickets', 'player_hundreds', 'player_fifties', 'player_jersey_no')