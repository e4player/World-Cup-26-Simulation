import one_match_simulation

def create_group(teams):
    groups = {}
    for team in teams:
        group = team["group"]
        groups.setdefault(group, []).append(team)
    return groups

def update_standings(result, team1_stats, team2_stats):
    if result == "team1 wins":
        team1_stats['points'] += 1
    elif result == "team2 wins":
        team2_stats['points'] += 1
    else:
        team1_stats['points'] += 0.5
        team2_stats['points'] += 0.5
    
def simulate_group(groups, group_name):
    group_info = groups[group_name]
    for i in range(3):
        for j in range(i+1,4):
            team1_stats = group_info[i]
            team2_stats = group_info[j]
            result = one_match_simulation.find_winner(team1_stats, team2_stats)
            update_standings(result, team1_stats, team2_stats)