input()
import snscrape.modules.twitter as sntwitter
import pandas as pd
from time import sleep
from tqdm import tqdm

tweet_data = []

username = input('enter your keyword: ')
number = int(input('how many tweets to scrape: '))
for i, tweets in enumerate(sntwitter.TwitterSearchScraper('{}'.format(usernmame)).get_items()):
    if i > number:
        break
    tweet_data.append([tweets.date, tweets.content, tweets.user.username, tweets.url])

df = pd.DataFrame(tweet_data, columns = ['Date', 'Tweets', 'Username', 'URL'])
df.to_csv(f'{username}.csv', index=False, encoding='utf-8')