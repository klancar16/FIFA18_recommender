from flask import *
from data_preprocess import read_data, group_by_team
from data_logic import first_team, sort_first_eleven, first_eleven_stats, find_similar_to_team, \
    filtering_our_constraints, filtering_user_constraints

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True
)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
dat = read_data()
team_data = group_by_team(dat)


@app.route('/change_team', methods=['POST'])
def change_team():
    new_team = str(request.json['team'])
    session['team'] = new_team
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/change_formation', methods=['POST'])
def change_formation():
    new_formation = str(request.json['formation'])
    session['formation'] = new_formation
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/constraints', methods=['POST'])
def constraints():
    constraints_json = json.dumps(request.json)
    session['constraints'] = constraints_json
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/rem_constraints', methods=['POST'])
def rem_constraints():
    session['constraints'] = ''
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route("/")
def show_tables():
    if 'team' not in session:
        session['team'] = 'Paris Saint-Germain'
    if 'formation' not in session:
        session['formation'] = '433'
    if 'constraints' not in session:
        session['constraints'] = ''

    start_eleven = first_team(session['formation'], team_data.get_group(session['team']))
    sorted_start_eleven = sort_first_eleven(start_eleven)
    fr_el_stats = first_eleven_stats(start_eleven)
    worst_player = sorted_start_eleven.iloc[0]

    filtered_recommends = filtering_our_constraints(worst_player, worst_player['Position'], dat)
    if session['constraints'] != '':
        filtered_recommends = filtering_user_constraints(filtered_recommends, json.loads(session['constraints']))

    sorted_similar = find_similar_to_team(fr_el_stats, filtered_recommends)

    return render_template('index.html',
                           tables=[sorted_similar.head(5)[['Name', 'Age', 'Overall', 'Potential','Wage', 'Club']].
                                        to_html(classes="table table-striped", index=False),
                                   start_eleven[['Position', 'Name', 'Age', 'Overall', 'Potential', 'Wage']].
                                        to_html(classes="table table-striped first-eleven", index=False)
                                   ],
                           teams=['Arsenal', 'AS Monaco', 'Paris Saint-Germain'],
                           cur_team=session['team'],
                           formations=['433', '442', '352'],
                           cur_formation=session['formation'],
                           worst_player=worst_player['Name'])


if __name__ == "__main__":
    app.run(debug=True)