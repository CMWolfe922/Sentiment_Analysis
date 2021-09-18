# SENTIMENT ANALYSIS
### Reddit Post and Comment Scraper
- as of now this returns all of the top 25 post's data for any subreddit that you want. There is a list where you can pass in any subreddit's that you want the post data from.

- There are still a lot of features that can be added as far as what data can be pulled from Reddit. I just haven't added a lot of them because I haven't needed them. Feel free to add whatever you think would make this more benefitial.

- The python module I am using to interact with Reddit is praw

#### Reddit "TO-DOs"

[x] Build a list of subreddits that I want searched daily
[x] Give that list a variable name
[x] pass the list into the get_top_25_post() function
[x] create empty list to append top_25_post data to
[x] append data to list and then shape into pandas df
[x] Retrieve Post ID from Panda Dataframe
[x] assign ID to submission value of Reddit instance
[x] use submission.comment.list() to retrieve all of the comment data
[] append comment data to a list
[] create another pandas dataframe for just the comments
[] Create function to find commonly used words
[] Create CSV files from the commonly used words
[] Find some type of package or API to help with the Sentiment Analysis
