import os
import pandas as pd


def get_tweets_for_user(twitter_username):
    since_date = "2023-01-01"
    until_date = "2023-03-29"

    filename = f"twitter_{twitter_username}"
    # Using OS library to call CLI commands in Python
    os.system('snscrape --jsonl --since {} twitter-search "from:{} until:{}"> {}.json'
              .format(since_date, twitter_username, until_date, filename))

    # Reads the json generated from the CLI command above and creates a pandas dataframe
    tweets_df2 = pd.read_json(f"{filename}.json", lines=True)

    # Displays first 5 entries from dataframe
    # tweets_df2.head()

    # Export dataframe into a CSV
    tweets_df2.to_csv(f"{filename}.csv", sep=',', index=False)


users = ['NikkyHaley', 'realDonaldTrump', 'VivekGRamaswamy', 'Stapleton_MT', 'marwilliamson']

for user in users:
    print(f"Started getting tweets for user {user}")
    get_tweets_for_user(user)
    print(f"Finished getting tweets for user {user}")
