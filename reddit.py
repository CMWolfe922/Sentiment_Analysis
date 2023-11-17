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
# my "config" file. Holds my usernames and passwords

from config import REDDIT_CLIENT_SECRET, REDDIT_CLIENT_ID, REDDIT_USER_AGENT
# -------------------------------------------------------------------------- #

# now that I have imported everything, CREATE A REDDIT INSTANCE:
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)

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


def return_comments_for(ID):
    # empty list to append comments to
    _comments = []
    """
    :param ID: individual ID 
    :returns: list of comments for post ID
    in ID
    """
    # Create submission instance
    submission = reddit.submission(id=ID)
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        _comments.append(comment.body)
    return _comments


# TODO: CREATE A WAY TO ASK USER FOR WHICH SUBREDDIT THEY WANT
def choose_subreddit(subreddit_list):
    choices = []
    indx = 0
    for i in subreddit_list:
        indx += 1
        choices.append((indx, i))
    # display the choices
    for i in choices:
        print(i)

    # get user input for index value
    get_choice = int(input(
        "Please enter the index value for which subreddit you would like to use: "))
    # take the index value and subtract 1 and then return
    # the value at that index in subreddit list
    idx = get_choice - 1
    subreddit = subreddit_list[idx]
    return subreddit

# CREATE PRAW INSTANCE
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)

# HAVE USER CHOOSE THE SUBREDDIT TO GET COMMENT DATA FOR
subreddit = choose_subreddit(subreddits)

# CALL FUNC TO GET SUBREDDIT POSTS DF
sub_df = return_subreddit_df(subreddit, limit=25)
sub_ids = [id for id in sub_df["id"]]
print(sub_ids)
# WRITE DF TO CSV FILE
post_path = f"data/{subreddit}_posts.csv"
comment_path = f"data/{subreddit}_comments.csv"
sub_df.to_csv(post_path, sep='|')

sub_comments = [id for sub_ids in return_comments_for(id)]
comments_df = pd.DataFrame(sub_comments, columns=['Comments'])
comments_df.to_csv(comment_path, sep='|')

"""I need to fix the comments that are being written to a CSV file for
because some reason they're saving the wrong comments to the CSV file.
It may be because I am using trying to save the wrong data. """
