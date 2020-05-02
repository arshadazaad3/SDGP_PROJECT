from GoogleNews import GoogleNews
from gnewsclient import gnewsclient
import pandas as pd
from random import randint
user_topic='health'
client = gnewsclient.NewsClient(language='english', location='', topic=user_topic, max_results=5)
df = pd.DataFrame(client.get_news())
newsList = df['title'].tolist()

column_names = ['ArticleId', 'Text', 'Category']

df = pd.DataFrame(columns = column_names)
for item in newsList:
    value = randint(5000, 5200)
    df = df.append({'ArticleId': value, 'Text': item, 'Category': 'health'}, ignore_index=True)

with open('newNewsHealth.csv', 'a', newline='') as f:
    df.to_csv(f, header=f.tell()==0)
