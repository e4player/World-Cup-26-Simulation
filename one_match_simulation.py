import random
import math

def expected_score(team1_rating, team2_rating):
   expected_score = 1/(1+10**((team2_rating-team1_rating)/400))
   return expected_score

def draw_probability(team1_rating, team2_rating):
    elo_diff = abs(team1_rating-team2_rating)
    draw_prob = 0.3*math.exp(-elo_diff/400)
    return draw_prob

def get_result(team1_stats, team2_stats):
     exp_score = expected_score(team1_stats['elo'], team2_stats['elo'])
     draw_prob = draw_probability(team1_stats['elo'], team2_stats['elo'])
     team1_win_prob = exp_score - draw_prob/2

     r = random.random()

     if r < team1_win_prob:
         result = "team1 wins"
     elif r < team1_win_prob + draw_prob:
         result = "Draw"
     else: 
        result = "team2 wins"
     return result

def find_winner(team1_stats, team2_stats):
    exp_score = expected_score(team1_stats['elo'], team2_stats['elo'])

    r = random.random()

    if r < exp_score:
        result = "team1 wins"
    else:
        result = "team2 wins"
    return result