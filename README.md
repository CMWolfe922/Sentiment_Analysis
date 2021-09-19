# SENTIMENT ANALYSIS
### Reddit Post and Comment Scraper
- as of now this returns all of the top 25 post's data for any subreddit that you want. There is a list where you can pass in any subreddit's that you want the post data from.

- There are still a lot of features that can be added as far as what data can be pulled from Reddit. I just haven't added a lot of them because I haven't needed them. Feel free to add whatever you think would make this more benefitial.

- The python module I am using to interact with Reddit is praw

#### Reddit "TO-DOs"

- [x] Build a list of subreddits that I want searched daily
- [x] Give that list a variable name
- [x] pass the list into the get_top_25_post() function
- [x] create empty list to append top_25_post data to
- [x] append data to list and then shape into pandas df
- [x] Retrieve Post ID from Panda Dataframe
- [x] assign ID to submission value of Reddit instance
- [x] use submission.comment.list() to retrieve all of the comment data
- [ ] append comment data to a list
- [ ] create another pandas dataframe for just the comments
- [ ] Create function to find commonly used words
- [ ] Create CSV files from the commonly used words
- [ ] Find some type of package or API to help with the Sentiment Analysis

### MAIN GOALS FOR REPOSITORY:

1. __Create a stock market / crypto currency sentiment analysis program__ that will eventually take in Reddit, Twitter, Facebook, Yahoo Finance, Google Finance, Stock Twits and any other social media/news outlets out there that I can scrape text data from, and create a points based system from 3 (being very positive) to -3 (being very negative). 
  - Also, each data source will be weighted based off statistical analysis of which sources have a better "prediction" percentage. So, if one sources positive material has more of a correlation with the stock price/crypto price going up, then that source will be weighted accordingly. 
  - I have decided on an exact method yet of how I want to determine the weight. I was thinking maybe something based off of difference in range and take in to account the number of sources and where each source ranks in data quality.
2. Before I can even choose on a method of weighting the sources or ranking them __I have to first complete the finlearn repository__. That is the repository that I am creating to get all the stock market prices and crypto prices. 
  - Once that is complete, then I can focus more on this. Once I complete that repository I want to merge it with this repository. Then it will be one program that can run every day at a specific time to scrape that day's data (I was thinking 12:01AM). This way in the morning it can send an email with the results of the prediction for that days stock price. 
  - By that point I hope to have the program gathering text and time series data, as well as have a ML model built to train itself on predicting price movement. 
3. With the ML model, I want to base it on 1 minute data only. Based on the theory that using daily prices from years ago will never work because the markets today are too different than they were years ago. Things change on a minute by minute basis now, plus crypto currency is involved now. So considering all these factors, I want to monitor price movement on a minute by minute basis and scan the web for articles, reddit posts, tweets, facebook posts, stock twit posts, and any other large forum, to see how price react to:
  - number of positive/negative posts, the nature of the posts (categorize them), where the posts or article came from, the author, etc.. 
  - Second, check the correlation of stock price movements vs. crypto movements. See if any have large correlations (as well as commodities)


__Obviously this will take A LOT of data and won't be possible to track the entire stock market on regular computers__ but, I was thinking of using a method to monitor the top 100 stocks and top 100 crypto currencies that are talked about or tweeted about. As I am building the sentiment analysis program, I will have it count the number of mentions for every symbol (stock and crypto) and once I am ready to combine the two programs and let it start learning, use the top 100 for each. Maybe even watch to see if a new currency or stock begins to be talked about more then we can drop the last place for either category and put the new target in the list. 

I am open to ideas on this though and I am looking for some people to help. I am not that great at writing code so any help would be appreciated. 
