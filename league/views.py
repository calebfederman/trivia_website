from django.shortcuts import render
from django.views import View
from .models import Team, Player, Season, Matchup
from django.db.models import Q

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, 'league/index.html')

class StandingsView(View):
    def get(self, request):
        teams = Team.objects.all().order_by('-win_count', 'team_name')
        return render(request, 'league/standings.html', {'teams': teams})

class ScheduleView(View):
    def get(self, request):
        matchups = Matchup.objects.all().order_by('week')
        return render(request, 'league/schedule.html', {'matchups': matchups})

class MatchupDetailView(View):
    def get(self, request, matchup_id):
        matchup = Matchup.objects.get(id=matchup_id)
        return render(request, 'league/matchup_detail.html', {'matchup': matchup})

class TeamDetailView(View):
    def get(self, request, team_id):
        team = Team.objects.get(id=team_id)
        players = team.player_set.all()
        matchups = Matchup.objects.filter(Q(home_team=team) | Q(away_team=team)).order_by('date')
        return render(request, 'league/team_detail.html', {'team': team, 'players': players, 'matchups':matchups})