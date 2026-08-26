import group_simulation

def get_third_teams(groups):
    third_teams = []
    for group in groups.values():
        third_teams.append([group[2]])
    return third_teams

def select_qualifiers(third_teams, groups):
    for team_info in third_teams:
        team_info.append(team_info[0]['points'] - group_simulation.get_expected_group_score(team_info[0], groups[team_info[0]['group']]))
    third_teams.sort(key = lambda x : x[1], reverse = True)
    if third_teams[7][1] == third_teams[8][1]:
        third_teams = break_third_tie(third_teams)
    return third_teams[:8]

def break_third_tie(third_teams):
    cutoff_teams = []
    for i, team_info in enumerate(third_teams):
        if team_info[1] == third_teams[7][1]:
            cutoff_teams.append([i, team_info])
    cutoff_teams.sort(key = lambda x : x[1][0]['elo'], reverse = True)
    start_index = cutoff_teams[0][0]
    end_index = cutoff_teams[-1][0]
    third_teams[start_index: end_index + 1] = [team_info[1] for team_info in cutoff_teams]
    return third_teams