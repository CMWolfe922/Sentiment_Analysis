# Test write data to CSV file for now. Save in Data folder
subreddit = "TestSubreddit"
comment_data = "Hello World"
path = f"data/{subreddit}_comments.csv"
file = open(path, 'a')
file.write(comment_data)
file.close()
