from process.form import Data
from process.game import Game

class Home:

    def __init__(self, team):
        self.team = team
        self.games = Data.all_games()
        self.total_hg = Game().average_league_home_goals()

    def average_home_goals(self):
        home_goals_total = 0
        total_home_games = 0
        for game in self.games:
            if game[0] == self.team:
                home_goals_total += int(game[2])
                total_home_games += 1
        average_home_goals = home_goals_total / total_home_games
        return average_home_goals

    def attack_strength_home(self):
        attack_strength_home = self.average_home_goals()/self.total_hg
        return attack_strength_home
    
    def average_home_conceded(self):
        home_conceded_total = 0
        total_home_games = 0
        for game in self.games:
            if game[0] == self.team:
                home_conceded_total += int(game[3])
                total_home_games += 1
        average_home_conceded = home_conceded_total / total_home_games
        return average_home_conceded

    def defense_strength_home(self):
        defense_strength_home = self.average_home_conceded()/self.total_hg
        return defense_strength_home



class Away:

    def __init__(self, team):
        self.team = team
        self.games = Data.all_games()
        self.total_ag = Game().average_league_away_goals()

    def average_conceded(self):
        conceded_total = 0
        total_away_games = 0
        for game in self.games:
            if game[1] == self.team:
                conceded_total += int(game[2])
                total_away_games += 1
        average_conceded = conceded_total / total_away_games
        return average_conceded
    
    def defense_strength_away(self):
        defense_strength_away = self.average_conceded()/self.total_ag
        return defense_strength_away
    
    def average_goal_away(self):
        goals_for_total = 0
        total_away_games = 0
        for game in self.games:
            if game[1] == self.team:
                goals_for_total += int(game[3])
                total_away_games += 1
        average_goal_away = goals_for_total / total_away_games
        return average_goal_away
    
    def attack_strength_away(self):
        attack_strength_away = self.average_goal_away()/self.total_ag
        return attack_strength_away