from data_preprocess import read_data, group_by_team
from data_logic import first_team, sort_first_eleven, first_eleven_stats, find_similar_to_team, \
    filtering_our_constraints

if __name__ == '__main__':
    dat = read_data()
    #print(dat['Preferred Positions'].unique())
    team_data = group_by_team(dat)
    #print(team_data.get_group('AS Monaco'))
    start_eleven = first_team('433', team_data.get_group('AS Monaco'))
    sorted_start_eleven = sort_first_eleven(start_eleven)
    fr_el_stats = first_eleven_stats(start_eleven)
    worst_player = sorted_start_eleven.iloc[0]

    filtered_recommends = filtering_our_constraints(worst_player, worst_player['Position'], dat)
    sorted_similar = find_similar_to_team(fr_el_stats, filtered_recommends)

    print(worst_player[['Name', 'Age', 'Overall', 'Potential', 'Wage', 'Position']])
    print(sorted_similar.head(10)[['Name', 'Age', 'Overall', 'Potential', 'Wage', 'Club']])
