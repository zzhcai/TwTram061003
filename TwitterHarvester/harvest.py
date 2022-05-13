"""
@author Team 31, Melborune, 2022

Bingzhe Jin (1080774), Hongwei Chen (891632), Tian Hui (1054513),
Zhen Cai (1049487), Ziqi Zhang (1241157)

"""

import sys
import couchdb
import tweepy
import methods


CONSUMER_KEY = "l1m1kwTc68Dguv9yKmFpaxTsR"
CONSUMER_SECRET = "WVgjbKyz9ICmMZRBbh2dxAHieOv1JWwoKdwMX77tUNvpibjaG1"
OAUTH_TOKEN = "1513822841426554881-XAos7hxcInZX2zuUtBWEHrNUgHVyfi"
OAUTH_TOKEN_SECRET = "IQRmIeodvV8wgmt9DtxUruUQJ95G32cSF4mDu2jL8kkVK"
bearer = "AAAAAAAAAAAAAAAAAAAAAP6kbQEAAAAAMonSjW3WVKpcrP6y%2BstoNcEFz3g%3DGPSE7WXwGTZSu0CrXRRVEuJaTeBlfPBAKOz6e8yVRMCaOErR6q"


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


    harvester = TwitterStreaming(bearer)
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
