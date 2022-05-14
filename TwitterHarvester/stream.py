"""
@author Team 31, Melborune, 2022

Bingzhe Jin (1080774), Hongwei Chen (891632), Tian Hui (1054513),
Zhen Cai (1049487), Ziqi Zhang (1241157)

"""

import sys
import couchdb
import tweepy
import methods


class TwitterStreaming(tweepy.StreamingClient):
    def on_connect(self):
        print("Connected to Twitter, start streaming...")

    def on_connection_error(self):
        print("Stream has connection errors or times out")

    def on_disconnect(self):
        print("Disconnected from Twitter")

    def on_tweet(self, tweet):
        methods.save_tweet(db, tweet)


if __name__ == "__main__":
    options = methods.readCommand(sys.argv[1:])

    # settings for CouchDB
    SERVER = "http://admin:admin@localhost:5984"

    # connecting CouchDB server
    server = couchdb.Server(SERVER)

    # connect to or create a database
    try:
        db = server[options.database]
    except couchdb.http.ResourceNotFound:
        db = server.create(options.database)


    harvester = TwitterStreaming(options.bearer)
    
    # clear rules
    for r in harvester.get_rules()[0]:
        harvester.delete_rules(r.id)
    
    rule = tweepy.StreamRule(value=options.query)
    harvester.add_rules(rule)

    harvester.filter(
        expansions=["author_id", "geo.place_id", "attachments.media_keys"],
        tweet_fields=[
            "author_id",
            "context_annotations",
            "conversation_id",
            "created_at",
            "entities",
            "geo",
            "in_reply_to_user_id",
            "lang",
            "public_metrics",
            "possibly_sensitive",
            "referenced_tweets",
            "reply_settings",
            "source",
            "text",
            "withheld",
        ],
        user_fields=[
            "created_at",
            "description",
            "entities",
            "id",
            "location",
            "name",
            "public_metrics",
            "username",
            "verified",
            "withheld",
        ],
        media_fields=[
            "duration_ms",
            "height",
            "media_key",
            "preview_image_url",
            "type",
            "url",
            "width",
            "public_metrics",
            "alt_text",
        ],
        place_fields=[
            "contained_within",
            "country",
            "country_code",
            "full_name",
            "geo",
            "id",
            "name",
            "place_type",
        ],
    )
