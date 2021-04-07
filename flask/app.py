from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
import numpy as np
from tensorflow import keras
model = keras.models.load_model('model')
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    team_means = pd.read_csv('out.csv')
    team_players = pd.read_csv('static/teams_info.csv')

    del team_means['Unnamed: 0']
    del team_players['Unnamed: 0']
    main_teams_list = ['Astralis', 'Natus Vincere','Vitality', 'BIG', 'Liquid', 'Virtus.pro', 'Heroic', 'G2', 'OG', 'Gambit', 'mousesports', 'fnatic', 'Complexity',  'Spirit', 'Evil Geniuses']
    main_teams = team_players[team_players['team'].isin(main_teams_list)]

    means_teams = team_means[team_means['team'].isin(main_teams_list)]
    means = means_teams.copy()
    means = means.round(decimals=2)
    t = main_teams.copy()
    print(t.head)
    print(means)
    means.reset_index().values.tolist()
    logos = ["https://img-cdn.hltv.org/teamlogo/9bgXHp-oh1oaXr7F0mTGmd.svg?ixlib=java-2.1.0&s=f567161ab183001be33948b98c4b2067", 
    "https://img-cdn.hltv.org/teamlogo/yQB6cm3KZ_BcyrgppBQMjc.svg?ixlib=java-2.1.0&s=06825290bfb61c9f8467f5c323f51974",
    "https://img-cdn.hltv.org/teamlogo/0-i_bEjrf3v4eYqaG0Bix7.svg?ixlib=java-2.1.0&s=4eecbec277f018772a9b92c22da1a459",
    "https://img-cdn.hltv.org/teamlogo/p6OXTVsTFEhOcbTJ8gmuP6.png?invert=true&ixlib=java-2.1.0&sat=-100&w=100&s=2e51eb9aef71e50ef46e5fc812876d18",
    "https://img-cdn.hltv.org/teamlogo/dLtWEdSV58lIX1amAFggy0.svg?ixlib=java-2.1.0&s=f24d0a7b3ef24ed57184a51d35202b4e",
    "https://img-cdn.hltv.org/teamlogo/zFLwAELOD15BjJSDMMNBWQ.png?ixlib=java-2.1.0&w=100&s=88aeba1564bc27de69fb2302e47e1a7c",
    "https://img-cdn.hltv.org/teamlogo/pNV-lVdpvYZIkDwHdEXXg-.svg?ixlib=java-2.1.0&s=8b557b5b4d283208976340ef1bc44c76",
    "https://img-cdn.hltv.org/teamlogo/ffSPDr5mbWSKI4yruyfVtx.svg?ixlib=java-2.1.0&s=2b0a91cf4a31e6eec7a5928b10465f32",
    "https://img-cdn.hltv.org/teamlogo/JMeLLbWKCIEJrmfPaqOz4O.svg?ixlib=java-2.1.0&s=c02caf90234d3a3ebac074c84ba1ea62",
    "https://img-cdn.hltv.org/teamlogo/0-i_bEjrf3v4eYqaG0Bix7.svg?ixlib=java-2.1.0&s=4eecbec277f018772a9b92c22da1a459",
    "https://img-cdn.hltv.org/teamlogo/kixzGZIb9IYAAv-1vGrGev.svg?ixlib=java-2.1.0&s=8f9986a391fcb1adfbfff021b824a937",
    "https://img-cdn.hltv.org/teamlogo/7b6DouMNGWcqENDx1vw_Ot.png?ixlib=java-2.1.0&w=100&s=da19b361a2d10da3214e534c010961b2",
    "https://img-cdn.hltv.org/teamlogo/l7kuxrEAcHnKebe1lagTwv.svg?ixlib=java-2.1.0&s=8bca7011fe85275b16e811b872df6111",
    "https://img-cdn.hltv.org/teamlogo/yZ6Bpuui1rW3jocXQ68XgZ.svg?ixlib=java-2.1.0&s=f39be1d3e7baf30a4e7f0b1216720875",
    "https://img-cdn.hltv.org/teamlogo/GAlByJtDTnkgbb9p_71SUL.png?ixlib=java-2.1.0&w=100&s=ddc5952ae492cbefb10fbe64471486b5"]
    t['logos'] = logos
    #main_teams = main_teams.sort_values(by="mean.kast", ascending=False)
    print(request.method)
    if "predict" in request.form:
        print("Prediction works", request.form['team1input'], request.form['team2input'])
        team1= str(request.form['team1input']).strip()
        team1_stats = team_players[team_players['team'] == team1]
        print(team1_stats)
        team2= str(request.form['team2input']).strip()
        team2_stats = team_players[team_players['team'] == team2]
        print(team2_stats)
        del team1_stats['team']
        del team2_stats['team']
        team2_stats.columns = [str("col"+ str(x)) for x in range(0,20)]
        print(team2_stats)
        x = pd.concat([team1_stats.reset_index(drop=True), team2_stats.reset_index(drop=True)], axis=1)
        print(x)
        model.predict(x)
        prediction = model.predict(x)
        rounded = int(np.rint(prediction).tolist()[0][0])
        print(rounded)
        if rounded >= 0:
            score1 = 16
            score2 = score1 - rounded
        else:
            score2 = 16
            score1 = score2 - rounded

        return render_template("index.php", score1=score1, score2=score2, data=t, team1 = team1, team2=team2, prediction = rounded, selected="true")
    else:
        return render_template("index.php", data=t)


if __name__ == '__main__':
    app.debug = True
    app.run(host  = '0.0.0.0', port = 7676)
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
