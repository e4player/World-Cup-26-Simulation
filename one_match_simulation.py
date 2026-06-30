import random
import math

def expected_score(team1_rating, team2_rating):
   expected_score = 1/(1+10**((team2_rating-team1_rating)/400))
   return expected_score

def draw_probability(team1_rating, team2_rating):
    elo_diff = abs(team1_rating-team2_rating)
    draw_prob = 0.3*math.exp(-elo_diff/400)
    return draw_prob

def find_winner(team1, team2, teams):
     exp_score = expected_score(team1_rating = teams[team1], team2_rating=teams[team2])
     draw_prob = draw_probability(team1_rating=teams[team1], team2_rating=teams[team2])
     team1_win_prob = exp_score - draw_prob/2

     r = random.random()

     if r < team1_win_prob:
         result = f'{team1} wins'
     elif r < team1_win_prob + draw_prob:
         result = "Draw"
     else: 
        result = f'{team2} wins'
     return result