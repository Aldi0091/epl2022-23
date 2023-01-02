from process.main import Main
from math import e, factorial


class Poisson:

    home_games = []
    away_games = []
    home_wins = {}
    away_wins = {}
    draws = {}

    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.main = Main(self.home_team, self.away_team)
        self.xg_home = self.main.projected_xg_home()
        self.xg_away = self.main.projected_xg_away()
    
    def poisson(self):
        for x in range(0, 6):
            probability_home = ((self.xg_home ** x) * (e ** (-self.xg_home))) / factorial(x)
            probability_away = ((self.xg_away ** x) * (e ** (-self.xg_away))) / factorial(x)
            self.home_games.append(probability_home)
            self.away_games.append(probability_away)
    
    def distribute(self):
        for jax in range(len(self.home_games)):
            for uax in range(len(self.away_games)):
                score = self.home_games[jax]*self.away_games[uax]
                if jax > uax:
                    self.home_wins[f'{str(jax)}:{str(uax)}'] = round(score*100, 2)
                elif jax < uax:
                    self.away_wins[f'{str(jax)}:{str(uax)}'] = round(score * 100, 2)
                elif jax == uax:
                    self.draws[f'{str(jax)}:{str(uax)}'] = round(score * 100, 2)