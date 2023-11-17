# commonly used words
import collections
import pandas as pd
import time
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
    title, score, id, subreddit, url, comments, selftext, created <<<
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

main_comment_list = []
comments = []
posts = []
for post in sub_df["title"]:
    posts.append(post)
    
for id in sub_ids:
    sub_comments = return_comments_for(id)
    time.sleep(.25)
    comments.append(sub_comments)
    
for id in sub_ids:
    # this grabs each posts id to use to get that posts comments
    for comment in comments:
        # this loops through each posts comments and appends to main list
        main_comment_list.append(comment)

# Zip the posts and main_comment_list together into a list of tuples
main = list(zip(posts, main_comment_list))

# extract each post title and comments for that post and save them to a dataframe
print(main)

"""I need to fix the comments that are being written to a CSV file for
because some reason they're saving the wrong comments to the CSV file.
It may be because I am using trying to save the wrong data."""
