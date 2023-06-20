from django.db import models

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=3)
    logo = models.ImageField(null=True)
    win_count = models.IntegerField(default=0)
    loss_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.team_name
    
class Season(models.Model):
    season_number = models.IntegerField()
    teams = models.ForeignKey(Team)         # TODO: need to make this a many to many??
    current = models.BooleanField()

    def __str__(self):
        return 'Season ' + str(self.season_number)
    
class Player(models.Model):
    season = models.ForeignKey(Season)
    player_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.player_name

class Matchup(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    date = models.DateField()
    home_team = models.ForeignKey(Team)
    away_team = models.ForeignKey(Team)
    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.away_team) + ' vs ' + str(self.home_team) + ' on ' + str(self.date)
