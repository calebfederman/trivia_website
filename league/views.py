from django.shortcuts import render
from django.views import View
from .models import Team, Player, Season, Matchup

# Create your views here.

# TODO: create html templates

class StandingsView(View):
    def get(self, request):
        teams = Team.objects.all().order_by('-win_count', 'team_name')
        return render(request, 'standings.html', {'teams': teams})

class ScheduleView(View):
    def get(self, request):
        matchups = Matchup.objects.all().order_by('date')
        return render(request, 'schedule.html', {'matchups': matchups})

class MatchupDetailView(View):
    def get(self, request, matchup_id):
        matchup = Matchup.objects.get(id=matchup_id)
        questions = matchup.question_set.all()
        return render(request, 'matchup_detail.html', {'matchup': matchup, 'questions': questions})

class TeamDetailView(View):
    def get(self, request, team_id):
        team = Team.objects.get(id=team_id)
        players = team.player_set.all()
        return render(request, 'team_detail.html', {'team': team, 'players': players})