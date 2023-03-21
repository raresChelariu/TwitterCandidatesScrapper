import datetime

import seaborn as sns
import snscrape.modules.twitter as sntwitter
from tqdm.notebook import tqdm_notebook

sns.set_theme(style="whitegrid")

text = input('Enter query text to be matched (or leave it blank by pressing enter)')
username = input('Enter specific username(s) from a twitter account without @ (or leave it blank by pressing enter): ')
since = input('Enter startdate in this format yyyy-mm-dd (or leave it blank by pressing enter): ')
until = input('Enter enddate in this format yyyy-mm-dd (or leave it blank by pressing enter): ')
retweet = input('Exclude Retweets? (y/n): ')
replies = input('Exclude Replies? (y/n): ')


def search(text, username, since, until, retweet, replies):
    global filename
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
    if username != '' and text != '':
        filename = f"{since}_{until}_{username}_{text}.csv"
    elif username != "":
        filename = f"{since}_{until}_{username}.csv"
    else:
        filename = f"{since}_{until}_{text}.csv"
    print(filename)
    return q


q = search(text, username, since, until, retweet, replies)
# Creating list to append tweet data
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(q).get_items()):
    tweets_list1.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username, tweet.lang,
                         tweet.hashtags, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount,
                         tweet.media])

print(tweets_list1)

