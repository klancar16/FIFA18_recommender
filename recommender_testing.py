from data_preprocess import read_data, group_by_team, formations
from data_logic import first_team, sort_first_eleven, first_eleven_stats, find_similar_to_team, \
    filtering_our_constraints
from pprint import pprint
from timeit import default_timer as timer
from pyperclip import copy

similarities = ['pearson', 'cosine', 'minkowski']
time_elapsed = {
    'pearson': 0,
    'cosine': 0,
    'minkowski': 0
}
if __name__ == '__main__':
    dat = read_data()
    team_data = group_by_team(dat)
    teams = team_data.groups.keys()
    teams = ['FC Barcelona', 'Manchester United', 'Chelsea', 'Liverpool', 'Arsenal']
    teams = ['Paris Saint-Germain']
    no_of_teams = len(teams)
    forms = formations().keys()

    i = 0
    j = 0
    st = ''
    for team in teams:
        i = i + 1
        if team_data.get_group(team).shape[0] < 11:
            continue

        st = st + '=' + team + '================================================' + '\n'
        for formation in forms:
            start_eleven = first_team(formation, team_data.get_group(team))
            st = st + start_eleven[['Position', 'Name', 'Age', 'Overall']].to_string() + '\n'
            sorted_start_eleven = sort_first_eleven(start_eleven)
            fr_el_stats = first_eleven_stats(start_eleven)
            worst_player = sorted_start_eleven.iloc[0]
            filtered_recommends = filtering_our_constraints(worst_player, worst_player['Position'], dat)
            if filtered_recommends.size == 0:
                break
            st = st + worst_player[['Name', 'Age', 'Overall', 'Potential', 'Wage', 'Position']].to_string() + '\n'
            for sim in similarities:
                start = timer()
                sorted_similar = find_similar_to_team(fr_el_stats, filtered_recommends, sim)
                end = timer()
                time_elapsed[sim] = time_elapsed[sim] + (end - start)
                st = st + sorted_similar.head(3)[['Name', 'Age', 'Overall', 'Potential', 'Club']].to_string() + '\n'
        j = j + 1
        print('{0}/{1}'.format(i, no_of_teams))
    copy(st)
    print('Legit: {0}'.format(j))
    pprint(time_elapsed)