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


# index_subs = [enumerate(subreddits) for i in subreddits]

# print(index_subs)


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


# TODO: WRITE POSTS TO CSV
post_path = f"data/{subreddit}_posts.csv"
