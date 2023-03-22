import datetime

import pandas as pd
import seaborn as sns
import snscrape.modules.twitter as sntwitter
import base64
sns.set_theme(style="whitegrid")

initialQuery = input('Enter query text to be matched (or leave it blank by pressing enter)')
twitterUser = input('Enter specific username(s) from a twitter account (or leave it blank by pressing enter): ')
startDate = input('Enter startdate in this format yyyy-mm-dd (or leave it blank by pressing enter): ')
endDate = input('Enter enddate in this format yyyy-mm-dd (or leave it blank by pressing enter): ')
excludeRetweets = input('Exclude Retweets? (y/n): ')
excludeReplies = input('Exclude Replies? (y/n): ')


def search(text, username, since, until, retweet, replies):
    q = text
    if username != '':
        q += f" from:{username}"
    if until == '':
        until = datetime.datetime.strftime(datetime.date.today(), '%Y-%m-%d')
    q += f" until:{until}"
    if since == '':
        since = datetime.datetime.strftime(datetime.datetime.strptime(until, '%Y-%m-%d') -
                                           datetime.timedelta(days=7), '%Y-%m-%d')
    q += f" since:{since}"
    if retweet == 'y':
        q += f" exclude:retweets"
    if replies == 'y':
        q += f" exclude:replies"
    return q


def get_tweets_as_file(text, username, since, until, retweet, replies):
    q = search(text, username, since, until, retweet, replies)
    # Creating list to append tweet data
    tweets_list1 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(q).get_items()):
        tweets_list1.append([tweet.date, tweet.id, base64_encode(tweet.rawContent), tweet.user.twitterUser, tweet.lang,
                             tweet.hashtags, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount,
                             tweet.media])

    tweets_df1 = pd.DataFrame(tweets_list1, columns=['DateTime', 'TweetId', 'Text', 'Username', 'Language',
                                                     'Hashtags', 'ReplyCount', 'RetweetCount', 'LikeCount',
                                                     'QuoteCount', 'Media'])
    tweets_df1.to_csv(f"{twitterUser}", index=False)


def base64_encode(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def base64_decode(message):
    base64_bytes = message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

# print(base64_encode('Python'))
# print(base64_decode(base64_encode('Python')))
get_tweets_as_file(initialQuery, twitterUser, startDate, endDate, excludeRetweets, excludeReplies)
