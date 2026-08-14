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

def create_leaderboard(group):
    leaderboard = sorted(group, key = lambda x : x['points'], reverse = True)
    return leaderboard

def play_off(leaderboard, team1, team2):
    result = one_match_simulation.find_winner(team1[0], team2[0])
    if result == "team2 wins":
            temp = leaderboard[team1[1]]
            leaderboard[team1[1]] = leaderboard[team2[1]]
            leaderboard[team2[1]] = temp
    return leaderboard

def get_expected_group_score(given_team , group):
    group_expected_score = 0
    for team in group:
        if team == given_team:
            continue
        group_expected_score += one_match_simulation.expected_score(given_team['elo'], team['elo'])
    return group_expected_score
    

def break_tie(leaderboard):
    tied_teams = []
    comparison_index = 0
    while comparison_index < 3:
        if leaderboard[comparison_index + 1]['points'] != leaderboard[comparison_index]['points']:
            comparison_index += 1
        else:
            tied_teams.append([leaderboard[comparison_index], comparison_index])
            for i in range(comparison_index + 1, 4):
                if leaderboard[i]['points'] == leaderboard[comparison_index]['points']:
                    tied_teams.append([leaderboard[i],i])
            if len(tied_teams) == 2:
                leaderboard = play_off(leaderboard, tied_teams[0], tied_teams[1])
                tied_teams = []
                comparison_index +=1
            if len(tied_teams) > 2:
                for team_info in tied_teams:
                    team_info.append(team_info[0]['points'] - get_expected_group_score(team_info[0], leaderboard))
                tied_teams.sort(key = lambda x : x[2], reverse=True)
                for j, tied_team in enumerate(tied_teams):
                    tied_team[1] = j
                if len(tied_teams) == 4:
                    leaderboard = []
                    for team in tied_teams:
                        leaderboard.append(team[0])
                    return leaderboard
                elif comparison_index == 1:
                    new_leaderboard = [leaderboard[0]]
                    for team in tied_teams:
                        new_leaderboard.append(team[0])
                    leaderboard = new_leaderboard
                    return leaderboard
                else:
                    new_leaderboard = []
                    for team in tied_teams:
                        new_leaderboard.append(team[0])
                    new_leaderboard.append(leaderboard[3])
                    leaderboard = new_leaderboard
                    return leaderboard
    return leaderboard
        
def simulate_group(groups, group_name):
    group_info = groups[group_name]
    for i in range(3):
        for j in range(i+1,4):
            team1_stats = group_info[i]
            team2_stats = group_info[j]
            result = one_match_simulation.get_result(team1_stats, team2_stats)
            update_standings(result, team1_stats, team2_stats)
    return create_leaderboard(group_info)