from django.test import TestCase

# Create your tests here.

from .models import Team, Season, Player, Matchup

class TeamModelTest(TestCase):
    def test_Team_model_str_representation(self):
        team = Team(team_name='Team A', short_name='A')
        self.assertEqual(str(team), 'Team A')

class SeasonModelTest(TestCase):
    def test_Season_model_str_representation(self):
        season = Season(season_number=1, current=True)
        self.assertEqual(str(season), 'Season 1')

class PlayerModelTest(TestCase):
    def test_Player_model_str_representation(self):
        player = Player(player_name='John Doe')
        self.assertEqual(str(player), 'John Doe')

class MatchupModelTest(TestCase):
    def test_Matchup_model_str_representation(self):
        team1 = Team(team_name='Team A', short_name='A', logo='team_a.png')
        team2 = Team(team_name='Team B', short_name='B', logo='team_b.png')
        matchup = Matchup(date='2023-06-19', home_team=team1, away_team=team2)
        expected_str = 'Team B vs Team A on 2023-06-19'
        self.assertEqual(str(matchup), expected_str)
