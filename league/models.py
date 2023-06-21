from django.db import models

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=3)
    #logo = models.ImageField(null=True)
    win_count = models.IntegerField(default=0)
    loss_count = models.IntegerField(default=0)
    ot_loss_count = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    
    def __str__(self):
        return self.team_name
    
class Season(models.Model):
    season_number = models.IntegerField()
    teams = models.ManyToManyField(Team, related_name='seasons')
    current = models.BooleanField(default=False)

    def __str__(self):
        return 'Season ' + str(self.season_number)
    
class Player(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='players')
    player_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.player_name

class Matchup(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='matchups')
    week = models.IntegerField(default=0)
    date = models.DateField(default='12-31-2050')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matchups')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matchups')
    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)
    ot_loss = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # if the home team won
        if self.home_team_score > self.away_team_score:
            # adjust home team points and win count
            self.home_team.win_count += 1
            self.home_team.points += 2
            # adjust away team points and loss count
            # add one point if ot_loss
            if self.ot_loss:
                self.away_team.points += 1
                self.away_team.ot_loss_count += 1
            else:
                self.away_team.loss_count += 1
        # if the away team won
        elif self.home_team_score < self.away_team_score:
            # adjust away team points and win count
            self.away_team.win_count += 1
            self.away_team.points += 2
            # adjust away team points and loss count
            # add one point if ot_loss
            if self.ot_loss:
                self.home_team.points += 1
                self.home_team.ot_loss_count += 1
            else:
                self.home_team.loss_count += 1
        self.home_team.save()
        self.away_team.save()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # if the home team won
        if self.home_team_score > self.away_team_score:
            # adjust home team points and win count
            self.home_team.win_count -= 1
            self.home_team.points -= 2
            # adjust away team points and loss count
            # add one point if ot_loss
            if self.ot_loss:
                self.away_team.points -= 1
                self.away_team.ot_loss_count -= 1
            else:
                self.away_team.loss_count -= 1
        # if the away team won
        elif self.home_team_score < self.away_team_score:
            # adjust away team points and win count
            self.away_team.win_count -= 1
            self.away_team.points -= 2
            # adjust away team points and loss count
            # add one point if ot_loss
            if self.ot_loss:
                self.home_team.points -= 1
                self.home_team.ot_loss_count -= 1
            else:
                self.home_team.loss_count -= 1
        self.home_team.save()
        self.away_team.save()

    def __str__(self):
        return str(self.away_team) + ' vs ' + str(self.home_team) + ' on ' + str(self.date)
