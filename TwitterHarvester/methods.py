# http://sentic.net/api/#intensity
# EMOTION RECOGNITION

from senticnet.senticnet import SenticNet
from cleantext import clean
from optparse import OptionParser


def clean_text(text):
    return clean(
        text,
        fix_unicode=True,
        to_ascii=True,
        lower=True,
        no_line_breaks=True,
        no_urls=True,
        no_emails=True,
        no_phone_numbers=True,
        no_numbers=True,
        no_digits=True,
        no_currency_symbols=True,
        no_punct=True,
        replace_with_punct="",
        replace_with_url="",
        replace_with_email="",
        replace_with_phone_number="",
        replace_with_number="",
        replace_with_digit="",
        replace_with_currency_symbol="",
        lang="en",
    ).split(" ")


def sn_sentence(sentence):
    sn = SenticNet()
    polarity_score = 0
    introspection_score = 0
    temper_score = 0
    attitude_score = 0
    sensitivity_score = 0
    valid_word_num = 0

    for word in sentence:
        try:
            concept_info = sn.concept(word)
            polarity_score += float(concept_info["polarity_value"])
            introspection_score += float(concept_info["sentics"]["introspection"])
            temper_score += float(concept_info["sentics"]["temper"])
            attitude_score += float(concept_info["sentics"]["attitude"])
            sensitivity_score += float(concept_info["sentics"]["sensitivity"])
            valid_word_num += 1
        except:
            continue

    return {
        "word_num": valid_word_num,
        "polarity_score": polarity_score,
        "introspection_score": introspection_score,
        "temper_score": temper_score,
        "attitude_score": attitude_score,
        "sensitivity_score": sensitivity_score,
    }


# average score per word
def aggregated_scores(lis):
    polarity_score = 0
    introspection_score = 0
    temper_score = 0
    attitude_score = 0
    sensitivity_score = 0
    word_num = 0

    for sentence in lis:
        score = sn_sentence(sentence)
        polarity_score += score["polarity_score"]
        introspection_score += score["introspection_score"]
        temper_score += score["temper_score"]
        attitude_score += score["attitude_score"]
        sensitivity_score += score["sensitivity_score"]
        word_num += score["word_num"]
    if word_num == 0:
        word_num += 1
    return {
        "polarity_score": polarity_score / word_num,
        "introspection_score": introspection_score / word_num,
        "temper_score": temper_score / word_num,
        "attitude_score": attitude_score / word_num,
        "sensitivity_score": sensitivity_score / word_num,
    }


def score_sentence(sentence):
    return aggregated_scores([clean_text(sentence)])


def readCommand(argv):
    parser = OptionParser()

    parser.add_option("-q", "--query", dest="query", help="enter query", default="")

    parser.add_option(
        "-d", "--database", dest="database", help="database name", default=""
    )

    # parser.add_option('-t', '--timeline', dest='timeline', help='home timeline', default='')

    parser.add_option("-u", "--userdb", dest="userdb", help="user database", default="")

    options, otherjunk = parser.parse_args(argv)

    return options


def save_tweet(db, tweet):
    sentiment = score_sentence(tweet.text)

    item = {
        "_id": str(tweet.id),
        "text": tweet.text,
        "author": tweet.author_id,
        "created_at": tweet.created_at.isoformat(),
        "geo": tweet.geo,
        "polarity_score": sentiment["polarity_score"],
        "introspection_score": sentiment["introspection_score"],
        "temper_score": sentiment["temper_score"],
        "attitude_score": sentiment["attitude_score"],
        "sensitivity_score": sentiment["sensitivity_score"],
    }
    try:
        db.save(item)
        # print("saved twitter", tweet.id)
    except:
        pass


def save_user(user_db, user):

    item = {
        "_id": str(user.id),
        "name": user.name,
        "username": user.username,
        "location": user.location,
    }
    try:
        user_db.save(item)
        # print("saved user", user.id)
    except:
        pass
