from process.poisson import Poisson


class Work:

    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.stats = Poisson(self.home_team, self.away_team)
        self.stats.poisson()
        self.stats.distribute()
        self.home_wins = self.stats.home_wins
        self.away_wins = self.stats.away_wins
        self.draws = self.stats.draws
        self.homes = self.stats.home_games
        self.aways = self.stats.away_games

    def home_odds_to_win(self):
        home_odds_to_win = 0
        for val in self.home_wins.values():
            home_odds_to_win += val
        W1 = round(home_odds_to_win, 2)
        bookW1 = round(100 / W1, 2)
        return bookW1

    def away_odds_to_win(self):
        away_odds_to_win = 0
        for val in self.away_wins.values():
            away_odds_to_win += val
        W2 = round(away_odds_to_win, 2)
        bookW2 = round(100 / W2, 2)
        return bookW2

    def draw_odds(self):
        draw_odds = 0
        for val in self.draws.values():
            draw_odds += val
        X = round(draw_odds, 2)
        bookX = round(100 / X, 2)
        return bookX
    
    def odds_1x(self):
        odds_1x = 0
        for val in self.home_wins.values():
            odds_1x += val
        for val in self.draws.values():
            odds_1x += val
        _1x = round(odds_1x, 2)
        book1X = round(100 / _1x, 2)
        return book1X
    
    def odds_x2(self):
        odds_x2 = 0
        for val in self.away_wins.values():
            odds_x2 += val
        for val in self.draws.values():
            odds_x2 += val
        x2 = round(odds_x2, 2)
        bookX2 = round(100 / x2, 2)
        return bookX2
    
    def total(self, value, operator):
        """Value takes parameter 1.5, 2.5, 3.5 or 4.5
            Operator takes parameter "less" or "greater"
        """
        total_below = 0
        for a in range(6):
            for b in range(6):
                if a + b < value:
                    score = self.homes[a] * self.aways[b]
                    total_below += score
        if operator == "less":
            probability = round(total_below*100, 2)
            coef = round(100 / probability, 2)
            return coef
        elif operator == "greater":
            probability = round((1 - total_below)*100, 2)
            coef = round(100 / probability, 2)
            return coef

    def team_to_score(self, team):
        """Parameter team takes value either 'home' or 'away'."""
        team1_scores = 0
        team2_scores = 0
        for c in range(6):
            for d in range(6):
                if c > 0:
                    score = self.homes[c] * self.aways[d]
                    team1_scores += score
        for c in range(6):
            for d in range(6):
                if d > 0:
                    score = self.homes[c] * self.aways[d]
                    team2_scores += score
        if team == "home":
            t1_sc = round(team1_scores*100, 2)
            coef = round(100 / t1_sc, 2)
            return coef
        elif team == "away":
            t2_sc = round(team2_scores*100, 2)
            coef = round(100 / t2_sc, 2)
            return coef


