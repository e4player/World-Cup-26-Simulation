import simulate_world_cup

def simulate_n_tournaments(n):
    win_probabilities = {}

    for i in range(n):
        winner = simulate_world_cup.simulate_world_cup()
        win_probabilities[winner] = win_probabilities.get(winner, 0) + 1
    
    for teams in win_probabilities:
        win_probabilities[teams] /= n
    
    return win_probabilities