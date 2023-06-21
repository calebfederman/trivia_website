from django.urls import path
from .views import IndexView, StandingsView, ScheduleView, MatchupDetailView, TeamDetailView

app_name = 'league'

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('standings/', StandingsView.as_view(), name='standings'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('matchup/<int:matchup_id>/', MatchupDetailView.as_view(), name='matchup_detail'),
    path('team/<int:team_id>/', TeamDetailView.as_view(), name='team_detail'),
]
