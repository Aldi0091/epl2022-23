from process.team import Home, Away
from process.game import Game


class Main:

    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.total_hg = Game().average_league_home_goals()
        self.total_ag = Game().average_league_away_goals()
        self.home = Home(self.home_team)
        self.away = Away(self.away_team)

    
    def projected_xg_home(self):
        projected_xg_home = self.home.attack_strength_home() * self.away.defense_strength_away() * self.total_hg
        return projected_xg_home
    
    def projected_xg_away(self):
        projected_xg_away = self.away.attack_strength_away() * self.home.defense_strength_home() * self.total_ag
        return projected_xg_away




