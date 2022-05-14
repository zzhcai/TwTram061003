from dash import Dash, dcc, html, Input, Output
import couchdb
from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px

with open('../webapp/public/jsons/sa3.json') as f:
    suburb = json.load(f)


app = Dash(__name__)


app.layout = html.Div([
    dcc.Dropdown(["polarity", "temper", "attitude", "introspection", "sensitivity"], "polarity", id='senti'),
    'was scored by this many students:',
    dcc.Graph(id='output'),
])

@app.callback(Output('output', 'figure'), Input('senti', 'value'))
def update_output(value):
    global db
    # if value == 1:
    #     a = next(db.iterview("geo/polarity_max_id", 1))['value']['max']
    # elif value == 2:
    #     a = next(db.iterview("geo/polarity_sum_count", 1))['value']['sum']
    # else: 
    
    keys = []
    sums = []
    for i in db.view("{:s}/sa_sum_count".format(value), group=True, group_level=2):
        keys.append(i['key'][-1])
        sums.append(i['value']['sum']/i['value']['count'])
        # lis.append((i['key'][-1], i['value']['sum']))

    df = pd.DataFrame({'key': keys, 'sum': sums})

    fig = px.choropleth_mapbox(df, geojson=suburb, locations='key', color='sum',
                        color_continuous_scale="Viridis",
                        featureidkey="properties.name",
                        # range_color=(0, 12),
                        mapbox_style="carto-positron",
                        zoom=9, center = {"lat": -37.66, "lon": 145},
                        opacity=0.5,
                        labels={'sum':'sum polarity score'}, 
                        width=1500, height=800
                        )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

if __name__ == '__main__':
    SERVER = "http://admin:admin@172.26.130.6:5984"

    server = couchdb.Server(SERVER)

    try:
        db = server["historic_melb"]
    except couchdb.http.ResourceNotFound:
        print("No db")

    # for i in db.view("polarity/sa_sum_count", group=True, group_level=2):
    #     print(i)

    app.run_server(port=3000, host='0.0.0.0')