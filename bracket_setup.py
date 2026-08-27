def create_bracket(groups, third_teams_order, third_place_qualifiers):
    round_of_32 = [
    [get_second_place_team(groups, 'A'), get_second_place_team(groups, 'B')],
    [get_group_winner(groups, 'E'),"third team"],
    [get_group_winner(groups, 'F'), get_second_place_team(groups, 'C')],
    [get_group_winner(groups, 'C'), get_second_place_team(groups, 'F')],
    [get_group_winner(groups, 'I'),"third team"],
    [get_second_place_team(groups, 'E'), get_second_place_team(groups, 'I')],
    [get_group_winner(groups, 'A'),"third team"],
    [get_group_winner(groups, 'L'),"third team"],
    [get_group_winner(groups, 'D'),"third team"],
    [get_group_winner(groups, 'G'),"third team"],
    [get_second_place_team(groups, 'K'), get_second_place_team(groups, 'L')],
    [get_group_winner(groups, 'H'), get_second_place_team(groups, 'J')],
    [get_group_winner(groups, 'B'),"third team"],
    [get_group_winner(groups, 'J'), get_second_place_team(groups, 'H')],
    [get_group_winner(groups, 'K'),"third team"],
    [get_second_place_team(groups, 'D'), get_second_place_team(groups, 'G')]
    ]

    for matchup in round_of_32:
        if matchup[1] == "third team":
            matchup[1] = group_to_team_info(third_teams_order[0], third_place_qualifiers)
            third_teams_order = third_teams_order[1:]

    return round_of_32


def get_third_place_groups(third_place_qualifiers):
    third_place_group_list = []
    for team in third_place_qualifiers:
        third_place_group_list.append(team[0]['group'])
    return third_place_group_list

def get_group_winner(groups, group_name):
    group = groups[group_name]
    return group[0]

def get_second_place_team(groups, group_name):
    group = groups[group_name]
    return group[1]

def valid_matchup(match_number, group_letter):
    third_place_possibilities = {
        1: ["A", "B", "C", "D", "F"],  # Match 74: winner E
        2: ["C", "D", "F", "G", "H"],  # Match 77: winner I
        3: ["C", "E", "F", "H", "I"],  # Match 79: winner A
        4: ["E", "H", "I", "J", "K"],  # Match 80: winner L
        5: ["B", "E", "F", "I", "J"],  # Match 81: winner D
        6: ["A", "E", "H", "I", "J"],  # Match 82: winner G
        7: ["E", "F", "G", "I", "J"],  # Match 85: winner B
        8: ["D", "E", "I", "J", "L"],  # Match 87: winner K
    }
    if group_letter in third_place_possibilities[match_number]:
        return True
    else:
        return False

def add_third_place_teams(third_place_group_list, match_number, third_teams_order):
    if match_number == 9:
        return third_teams_order
    for group in third_place_group_list:
        if group not in third_teams_order and valid_matchup(match_number, group):
            third_teams_order.append(group)
            result = add_third_place_teams(
                third_place_group_list,
                match_number + 1,
                third_teams_order
            )
            if result is not None:
                return result
            third_teams_order.pop()
    return None

def group_to_team_info(group_name, third_place_qualifiers):
    for team in third_place_qualifiers:
        if team[0]['group'] == group_name:
            return team[0]