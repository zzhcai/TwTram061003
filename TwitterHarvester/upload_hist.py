import re
import json
import couchdb
from datetime import datetime
import geopandas as gpd
from methods import locate, score_sentence

filename = "/home/ubuntu/twitter-melb.json"

# get couchDB IP address
var_filename = "../ansible/vars/setup.yaml"
with open(var_filename, 'r') as f:
    first_line = f.readline().strip()
    db_ip = first_line.split()[1]

# settings for CouchDB
SERVER = "http://admin:admin@" + db_ip + ":5984"

# connecting CouchDB server
server = couchdb.Server(SERVER)

# connect to or create a database
try:
    db = server["historic_melb"]
except couchdb.http.ResourceNotFound:
    db = server.create("historic_melb")

# SA4 in Melbourne
sa4 = gpd.read_file("shapes/SA4_2021_AUST_GDA2020.shp").dropna()
sa4 = (
    sa4.loc[sa4["GCC_CODE21"] == "2GMEL", ["SA4_NAME21", "geometry"]]
    .reset_index()
    .drop("index", axis=1)
    .rename(columns={"SA4_NAME21": "name"})
)
with open("../sa4.json", "w") as f:
    f.write(sa4.to_json())

# SA3
sa3 = gpd.read_file("shapes/SA3_2021_AUST_GDA2020.shp").dropna()
sa3 = (
    sa3.loc[sa3["GCC_CODE21"] == "2GMEL", ["SA3_NAME21", "geometry"]]
    .reset_index()
    .drop("index", axis=1)
    .rename(columns={"SA3_NAME21": "name"})
)
with open("../sa3.json", "w") as f:
    f.write(sa3.to_json())

# SA2
sa2 = gpd.read_file("shapes/SA2_2021_AUST_GDA2020.shp").dropna()
sa2 = (
    sa2.loc[sa2["GCC_CODE21"] == "2GMEL", ["SA2_NAME21", "geometry"]]
    .reset_index()
    .drop("index", axis=1)
    .rename(columns={"SA2_NAME21": "name"})
)
with open("../sa2.json", "w") as f:
    f.write(sa2.to_json())

with open(filename, "r") as f:
    f.readline()
    for line in f:
        content = line.strip().strip(",")
        tweet = json.loads(content)
        datetime_object = datetime.strptime(
            tweet["doc"]["created_at"], "%a %b %d %X %z %Y"
        )
        geo = tweet["doc"]["geo"]
        sentiment = score_sentence(tweet["doc"]["text"])

        item = {
            "_id": tweet["id"],
            "text": tweet["doc"]["text"],
            "author": tweet["doc"]["user"]["id"],
            "created_at": datetime_object.isoformat(),
            "geo": geo,
            "sa4": locate(geo, sa4),
            "sa3": locate(geo, sa3),
            "sa2": locate(geo, sa2),
            "location": tweet["doc"]["location"],
            "polarity_score": sentiment["polarity_score"],
            "introspection_score": sentiment["introspection_score"],
            "temper_score": sentiment["temper_score"],
            "attitude_score": sentiment["attitude_score"],
            "sensitivity_score": sentiment["sensitivity_score"]
        }

        keywords = ["myki", "tram", "train", "bus", "metro"]
        print(item["sa4"])
        if item["sa4"] != None and any(re.search(k, item["text"], re.IGNORECASE) for k in keywords):
            try:
                db.save(item)
                # print("saved twitter", tweet["id"])
            except:
                print("failed save")
