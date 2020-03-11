""" flask_example.py
    Required packages:
    - flask
    - folium
    Usage:
    Start the flask server by running:
        $ python flask_example.py
    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed
"""

from flask import Flask, request, abort, jsonify

import folium
from flask.templating import render_template
import pandas as pd
import json

app = Flask(__name__)

state = pd.read_csv('CenPop2010_Mean_ST.txt')
st_list = list(state.T.to_dict().values())

@app.route('/', methods=['GET'])
def index():
    

    x = request.args.get("st")
    if x is None:
        start_coords = (37.7749, -122.4194)
    else:
        y = state[state["STATEFP"] == int(x)]
        lat = y.iloc[0]["LATITUDE"]
        lng = y.iloc[0]["LONGITUDE"]
        #print(isinstance(lat, float))
        #print(lat, lng)
        start_coords = (lat, lng)
        #start_coords = (33.008097, -86.756826)
        #start_coors = (lat, lng)

    folium_map = folium.Map(location=start_coords, zoom_start=8)
    folium_map.save('templates/map.html')
    return render_template('testj2.html', st_list=st_list)

@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(st_list)
    
if __name__ == '__main__':
    app.run(debug=True)
