from django.contrib import admin

# Register your models here.

from .models import Team, Season, Player, Matchup

class PlayerInline(admin.StackedInline):
    model = Player
    extra = 0

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'win_count', 'loss_count')
    search_fields = ('team_name',)
    inlines = [PlayerInline]

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('season_number', 'current')
    list_filter = ('current',)

@admin.register(Matchup)
class MatchupAdmin(admin.ModelAdmin):
    list_display = ('date', 'home_team', 'away_team', 'home_team_score', 'away_team_score')
    list_filter = ('season',)
    search_fields = ('home_team__team_name', 'away_team__team_name')

