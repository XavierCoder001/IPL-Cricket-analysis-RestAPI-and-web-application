from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()['teams']
    return render_template('index.html', teams=sorted(teams))

@app.route('/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = requests.get('http://127.0.0.1:5000/api/teamvteam?team1={}&team2={}'.format(team1, team2))
    response = response.json()

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json()['teams']

    return render_template('index.html',result=response, teams=sorted(teams))


@app.route('/batsman-record')
def batsman_record():
    batsman_name = request.args.get('batsman_name')

    response = requests.get(
        f'http://127.0.0.1:5000/api/batsman-record?batsman_name={batsman_name}'
    )

    data = response.json()

    # Example:
    # {
    #   "RG Sharma": {
    #       "all": {...},
    #       "against": {...}
    #   }
    # }

    player_name = list(data.keys())[0]
    player_record = data[player_name]

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json()['teams']

    return render_template(
        'index.html',
        teams=sorted(teams),
        batsman_name=player_name,
        batsman_result=player_record
    )

@app.route('/bowler-record')
def bowler_record():
    bowler_name = request.args.get('bowler_name')

    response = requests.get(
        f'http://127.0.0.1:5000/api/bowling-record?bowler_name={bowler_name}'
    )

    data = response.json()

    player_name = list(data.keys())[0]
    player_record = data[player_name]

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json()['teams']

    return render_template(
        'index.html',
        teams=sorted(teams),
        bowler_name=player_name,
        bowler_result=player_record
    )

app.run(debug=True, port=8080)