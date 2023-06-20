from django.contrib import admin

# Register your models here.

from .models import Team, Season, Player, Matchup

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'win_count', 'loss_count')
    search_fields = ('team_name',)

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('season_number', 'current')
    list_filter = ('current',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'team', 'season')
    list_filter = ('team', 'season')

@admin.register(Matchup)
class MatchupAdmin(admin.ModelAdmin):
    list_display = ('date', 'home_team', 'away_team', 'home_team_score', 'away_team_score')
    list_filter = ('season',)
    search_fields = ('home_team__team_name', 'away_team__team_name')

