import json
import couchdb
from datetime import datetime
from methods import score_sentence

filename = "./twitter-melb.json"

# settings for CouchDB
SERVER = 'http://admin:admin@localhost:5984'

# connecting CouchDB server
server = couchdb.Server(SERVER)

# connect to or create a database
try:
    db = server["historic_melb"]
except couchdb.http.ResourceNotFound:
    db = server.create("historic_melb")

with open(filename, 'r') as f:
    f.readline()
    for i in range(2500000):
        content = f.readline().strip().strip(",")
        tweet = json.loads(content)
        datetime_object = datetime.strptime(tweet["doc"]["created_at"], '%a %b %d %X %z %Y')
        sentiment = score_sentence(tweet["doc"]["text"])

        item = {
                '_id': tweet["id"],
                'text': tweet["doc"]["text"],
                'author': tweet["doc"]["user"]["id"],
                'created_at': datetime_object.isoformat(), 
                'geo': tweet["doc"]["geo"],
                'location': tweet["doc"]["location"],
                'polarity_score': sentiment['polarity_score'],
                'introspection_score': sentiment['introspection_score'],
                'temper_score': sentiment['temper_score'],
                'attitude_score': sentiment['attitude_score'],
                'sensitivity_score': sentiment['sensitivity_score']
                }
        try:
            db.save(item)
            # print("saved twitter", tweet["id"])
        except:
            print("failed save")