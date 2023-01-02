from work import Work

team1, team2="Chelsea", "Bournemouth"
the_game = Work(team1, team2)

w1 = the_game.home_odds_to_win()
w2 = the_game.away_odds_to_win()
xx = the_game.draw_odds()
odd_1x = the_game.odds_1x()
odd_x2 = the_game.odds_x2()
total_more_1_5 = the_game.total(1.5, "greater")
team1_score = the_game.team_to_score("home")
team2_score = the_game.team_to_score("away")

print(f"the winning odds of {team1}: ", w1)
print(f"the winning odds of {team2}: ", w2)
print(f"the draw odds: ", xx)
print(f"the 1x odds of {team1}: ", odd_1x)
print(f"the x2 odds of {team2}: ", odd_x2)
print(f"total of 1.5 more: ", total_more_1_5)
print(f"{team1} to score odds: ", team1_score)
print(f"{team2} to score odds: ", team2_score)