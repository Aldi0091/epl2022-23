from process.form import Data


class Game:

    def __init__(self):
        self.games = Data.all_games()
        self.total_games = len(self.games)

    def home_team_goals_season(self):
        home_team_goals_season = 0
        for game in self.games:
            home_team_goals_season += int(game[2])
        return home_team_goals_season
    
    def away_team_goals_season(self):
        away_team_goals_season = 0
        for game in self.games:
            away_team_goals_season += int(game[3])
        return away_team_goals_season
    
    def average_league_home_goals(self):
        average_league_home_goals = self.home_team_goals_season()/self.total_games
        return average_league_home_goals
    
    def average_league_away_goals(self):
        average_league_away_goals = self.away_team_goals_season()/self.total_games
        return average_league_away_goals