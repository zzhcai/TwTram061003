"""
@author Team 31, Melborune, 2022

Bingzhe Jin (1080774), Hongwei Chen (891632), Tian Hui (1054513),
Zhen Cai (1049487), Ziqi Zhang (1241157)

"""

import sys
import couchdb
import tweepy
import methods

MAX_RESULT = 10  # number of search tweets per page
PAGE_LIMIT = float("inf")  # number of pages


CONSUMER_KEY = "l1m1kwTc68Dguv9yKmFpaxTsR"
CONSUMER_SECRET = "WVgjbKyz9ICmMZRBbh2dxAHieOv1JWwoKdwMX77tUNvpibjaG1"
OAUTH_TOKEN = "1513822841426554881-XAos7hxcInZX2zuUtBWEHrNUgHVyfi"
OAUTH_TOKEN_SECRET = "IQRmIeodvV8wgmt9DtxUruUQJ95G32cSF4mDu2jL8kkVK"
bearer = "AAAAAAAAAAAAAAAAAAAAAP6kbQEAAAAAMonSjW3WVKpcrP6y%2BstoNcEFz3g%3DGPSE7WXwGTZSu0CrXRRVEuJaTeBlfPBAKOz6e8yVRMCaOErR6q"

client = tweepy.Client(
    bearer_token=bearer,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=OAUTH_TOKEN,
    access_token_secret=OAUTH_TOKEN_SECRET,
    wait_on_rate_limit=True,
)


def search(query):
    collection = tweepy.Paginator(
        client.search_recent_tweets,
        query=query,
        expansions=["author_id", "geo.place_id", "attachments.media_keys"],
        max_results=MAX_RESULT,
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
        limit=PAGE_LIMIT,
    )

    for i in collection:
        for tweet in i[0]:
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

    search(options.query)
