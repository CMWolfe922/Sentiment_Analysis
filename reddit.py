# commonly used words
import collections
import pandas as pd
# import matplotlib.pyplot as plt
# %matplotlib inline

# -------------------------------------------------------------------------- #

# reddit scraper imports
import praw
from praw.models import MoreComments
import pandas as pd
# my "secret" file. Holds my usernames and passwords

from secrets import reddit_client_secret, reddit_client_id, reddit_user_agent
# -------------------------------------------------------------------------- #

# now that I have imported everything, CREATE A REDDIT INSTANCE:
reddit = praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent=reddit_user_agent)

# create list of subreddits I want to extract post and comment data from each day:
subreddits = ["wallstreetbets", "StocksAndTrading", "Daytrading", "StockMarket", "CryptoCurrency",
              "stocks", "Trading", "CryptoMarkets", "Forex", "ethtrader", "DayTradingPro", "options",
              "RobinHoodPennyStocks", "thinkorswim", "Webull", "WallStreetbetsELITE", "trading212",
              "futurestrading", "interactivebrokers",  "wallstreetbetsnew", "UltimateTraders",
              "daytradingoptions", "DayTradingCrypro", "FluentInFinance"]


def return_subreddit_df(subreddit="all", limit=25):
    """
    :param subreddit: Which subreddit to get top posts.

    :param limit: number of desired posts. Default 25
    (This is for setting the limit after.hot(limit=25)
    and eventually determined from user input.)

    :returns: top posts in subreddit or default (top posts on reddit).
    data is returned in pandas df with the following columns:
    >>> title, score, id, subreddit, url, comments, selftext, created <<<
    """
    # empty list to insert data to:
    posts = []
    # variable for data
    top_posts = reddit.subreddit(subreddit).hot(limit=limit) # limit and subreddit params

    # FOR loop to append data to posts
    for post in top_posts:
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

    # Create df
    df = pd.DataFrame(posts, columns=["title","score", "id", "subreddit", "url", "comments","selftext", "created"])
    return df


def return_comments_for(ID_list):
    # empty list to append comments to
    _comments = []
    """
    :param ID_list: list of post IDs
    :returns: list of comments for each post ID
    in ID_list
    """
    # for loop to extract each ID one by one
    for ID in ID_list:
        # Create submission instance
        submission = reddit.submission(id=ID)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            _comments.append(comment.body)
    return _comments

# CREATE PRAW INSTANCE
reddit = praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent=reddit_user_agent)

# CALL FUNC TO FOR SUBREDDIT DATA
df = return_subreddit_df("FluentInFinance", limit=10)

# PASS DF INTO FUNC TO RETRIEVE POST COMMENTS
comments = return_comments_for(df["id"])

comments.sort()
