# Test write data to CSV file for now. Save in Data folder
subreddit = "TestSubreddit"
comment_data = "Hello World"
path = f"data/{subreddit}_comments.csv"
file = open(path, 'a')
file.write(comment_data)
file.close()


subreddits = ["wallstreetbets", "StocksAndTrading", "Daytrading", "StockMarket", "CryptoCurrency",
              "stocks", "Trading", "CryptoMarkets", "Forex", "ethtrader", "DayTradingPro", "options",
              "RobinHoodPennyStocks", "thinkorswim", "Webull", "WallStreetbetsELITE", "trading212",
              "futurestrading", "interactivebrokers",  "wallstreetbetsnew", "UltimateTraders",
              "daytradingoptions", "DayTradingCrypro", "FluentInFinance"]

# FIGURE OUT WAY TO PASS EACH SUBREDDIT TO RETURN DF FUNC
# MAYBE CREATING A GENERATOR FUNC TO YIELD EACH OPTION IN THE
# LIST WILL WORK.
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
    top_posts = reddit.subreddit(subreddit).hot(
        limit=limit)  # limit and subreddit params

    # FOR loop to append data to posts
    for post in top_posts:
        posts.append([post.title, post.score, post.id, post.subreddit,
                     post.url, post.num_comments, post.selftext, post.created])

    # Create df
    df = pd.DataFrame(posts, columns=[
                      "title", "score", "id", "subreddit", "url", "comments", "selftext", "created"])
    return df


# TODO: CREATE A WAY TO ASK USER FOR WHICH SUBREDDIT THEY WANT
def choose_subreddit(subreddit_list):
    choices = []
    indx = 0
    for i in subreddit_list:
        indx += 1
        choices.append((indx, i))
    # display the choices
    for i in choices: print(i)

    # get user input for index value
    get_choice = int(input("Please enter the index value for which subreddit you would like to use: "))
    # take the index value and subtract 1 and then return
    # the value at that index in subreddit list
    idx = get_choice - 1
    subreddit = subreddit_list[idx]
    return subreddit

choose_subreddit(subreddits)



"""
NEXT TASK TO COMPLETE. CREATE A FUNC TO WRITE THE POST
AND COMMENT DATA TO A CSV. MORE IMPORTANTLY, I NEED TO
CONVERT THE COMMENT DATA INTO A PANDAS DF AND THEN SAVE
THE PANDAS DF T0 CSV FILES TO BE MONITORED FOR SENTIMENT
ANALYSIS.
"""
# TODO: WRITE POSTS TO CSV
post_path = f"data/{subreddit}_posts.csv"

"""Create a function for the common words script that works with the
reddit data. """
import collections
def get_words(path, encoding="utf8"):

    path = path
    file = open(path, encoding=encoding)
    a = file.read()
    # now the stop words
    stopwords = set(line.strip() for line in open(path))
    stopwords = stopwords.union(set(['mr', 'one', 'two', 'said']))

    # now create a dict and add to it for every word in the file
    # that doesn't exist but if it does increase the count by 1
    wordcount = {}
    # now I need to split by punctuation and use case delimiters to prevent duplicates
    for word in a.lower().split():
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace(":", "")
        word = word.replace("\"", "")
        word = word.replace("!", "")
        word = word.replace("â€œ", "")
        word = word.replace("â€", "")
        word = word.replace("*", "")

        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

    # I can have user input choose how many of the top most common words to use.
    n_print = int(input("How many most common words to print: "))
    print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        print(word, ": ", count)
    #close the file
    file.close()

    # Create data frame of the most common wordss and draw a bar chart
    lst = word_counter.most_common(n_print)
    df = pd.DataFrame(lst, column=['Word', 'Count'])
    df.plot.bar(x='Word', y='Count')
