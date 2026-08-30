import json
import group_simulation
import third_place_tie
import bracket_setup
import knockouts

def simulate_world_cup():
    with open("team_ratings.json", "r") as file:
        teams = json.load(file)

    groups = group_simulation.create_group(teams)

    for group_name in groups:
        leaderboard = group_simulation.simulate_group(groups, group_name)
        leaderboard = group_simulation.break_tie(leaderboard)
        groups[group_name] = leaderboard

    third_teams = third_place_tie.get_third_teams(groups)

    third_qualifiers = third_place_tie.select_qualifiers(third_teams, groups)

    third_teams_order = bracket_setup.add_third_place_teams(bracket_setup.get_third_place_groups(third_qualifiers),1,[])

    bracket = bracket_setup.create_bracket(groups, third_teams_order, third_qualifiers)

    teams_list = knockouts.matchups_to_teams_list(bracket)

    winner = knockouts.simulate_knockouts(teams_list)

    return winner