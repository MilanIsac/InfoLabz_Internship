from django.db import models

# Create your models here.

class PlayerCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_desc = models.TextField()
    
    def __str__(self):
        return self.category_name
    

class PlayerTeam(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    team_desc = models.TextField()
    
    def __str__(self):
        return self.team_name

class Player(models.Model):
    player_name = models.CharField(max_length=100, unique=True)
    player_category_id = models.ForeignKey(PlayerCategory, on_delete=models.CASCADE)
    player_team_id = models.ForeignKey(PlayerTeam, on_delete=models.CASCADE)
    player_runs = models.IntegerField(default=0)
    player_wickets = models.IntegerField(default=0)
    player_hundreds = models.IntegerField(default=0)
    player_fifties = models.IntegerField(default=0)
    player_jersey_no = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.player_name