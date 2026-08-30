import one_match_simulation

def matchups_to_teams_list(matchups):
    teams_list = []
    for matchup in matchups:
        teams_list.append(matchup[0])
        teams_list.append(matchup[1])
    return teams_list

def simulate_knockouts(teams_list):
    if len(teams_list) == 1:
        return teams_list[0]['team']
    winners = []
    
    for i in range(0, len(teams_list), 2):
        team1 = teams_list[i]
        team2 = teams_list[i+1]
        winner = one_match_simulation.find_winner(team1, team2)
        if winner == "team1 wins":
            winners.append(team1)

        else:
            winners.append(team2)

    return simulate_knockouts(winners)
