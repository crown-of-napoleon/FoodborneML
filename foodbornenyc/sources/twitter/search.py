"""
Simple Twitter Search based on keywords once every 5 seconds & save to database
"""
from time import time, sleep

from twython import Twython
from twython.exceptions import TwythonError
from sqlalchemy.exc import OperationalError

from foodbornenyc.models.documents import Tweet
from foodbornenyc.models.models import get_db_session
from foodbornenyc.db_settings import twitter_config
from foodbornenyc.sources.twitter.util \
    import tweet_to_Tweet, user_to_TwitterUser, place_to_Location,\
           reset_location_cache

from foodbornenyc.util.util import sec_to_hms, get_logger, xuni
logger = get_logger(__name__, level="INFO")

twitter = Twython(twitter_config['consumer_key'],
    twitter_config['consumer_secret'],
    twitter_config['access_token'],
    twitter_config['access_token_secret'])

search_terms = [
    '#foodpoisoning',
    '#stomachache',
    '"food poison"',
    '"food poisoning"',
    'stomach',
    'vomit',
    'puke',
    'diarrhea',
    '"the runs"'
]

def make_query(keywords):
    """ Take keywords and Twython object and return back the statuses"""
    try:
        query = ' OR '.join(keywords)
        results = twitter.search(q=query)
        tweets = results['statuses']
    except TwythonError:
        logger.warning("Twython Error. Skipping this request")
        tweets = []
    return tweets

def query_twitter(how_long=0, interval=5):
    """ Interface function """
    db = get_db_session()
    reset_location_cache()
    # can send 180 requests per 15 min = 5 sec
    start = time()

    # make sure we don't create duplicates.
    # keeping track of this ourselves saves many db hits
    # if we don't specify go indefinitely
    while time() - start < how_long:
        tweets = make_query(search_terms)
        if not tweets: # if we dont get anything back, sleep and try again
            sleep(interval)
            continue
        # if a retrieved tweet has a loc/user with a matching ID already in the
        # db, that loc/user is updated instead of a new one added, bc of merge
        try:
            db.add_all([db.merge(tweet_to_Tweet(t)) for t in tweets])
            db.commit()
        except OperationalError:
            pass
        sleep(interval)

