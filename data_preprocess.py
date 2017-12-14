import pandas as pd


def transform_value(x):
    transformed = ''
    for ch in x:
        if ch == '.' or ch.isdigit():
            transformed = transformed + ch

    value = float(transformed)
    value = value*1000 if x[-1] == 'K' else value*1000000
    return value


def transform_attribute(x):
    if isinstance(x, int):
        return x
    transformed = ''
    for ch in x:
        if ch == '+' or ch == '-':
            return int(transformed)
        else:
            transformed = transformed + ch
    return int(transformed)


def read_data():
    dat = pd.read_csv("data/CompleteDataset.csv", delimiter=',')
    dat = dat.drop_duplicates(['Name', 'Age', 'Club'])
    dat.fillna(value=0, axis=0, inplace=True)
    dat.drop(['Unnamed: 0', 'Photo', 'Flag', 'Club Logo', 'Special', 'ID'], axis=1, inplace=True)
    dat['Preferred Positions'] = dat['Preferred Positions'].apply(lambda x: x.split())
    dat['Value'] = dat['Value'].apply(lambda x: transform_value(x))
    dat['Wage'] = dat['Wage'].apply(lambda x: transform_value(x))
    dat['GK'] = dat['Overall'] * dat['Preferred Positions'].apply(lambda x: 1 if 'GK' in x else 0)
    dat[dat.columns[8:42]] = dat[dat.columns[8:42]].apply(lambda x: x.apply(lambda y: transform_attribute(y)))
    return dat


def formations():
    formation_dict = {
        '433': ['GK', 'LB', 'CB', 'CB', 'RB', 'CM', 'CM', 'CAM', 'LW', 'RW', 'ST'],
        '442': ['GK', 'LB', 'CB', 'CB', 'RB', 'CDM', 'RM', 'LM', 'CAM', 'ST', 'ST'],
        '352': ['GK', 'CB', 'CB', 'CB', 'CM', 'CM', 'RWB', 'LWB', 'CAM', 'CF', 'ST']
    }
    return formation_dict


def group_by_team(dat):
    grouped_data = dat.groupby('Club')
    return grouped_data
