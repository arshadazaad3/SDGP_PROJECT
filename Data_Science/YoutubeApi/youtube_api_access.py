import string

from googleapiclient.discovery import build
import pandas as pd
api_key = 'AIzaSyCK2xg2jlA03mc4nU4rgKG9mYK9VCZyBjM'
youtube = build('youtube','v3',developerKey=api_key)
req = youtube.search().list(q='saveAustralia',part='snippet',type='video', maxResults=10)
res = req.execute()

# df = pd.DataFrame(res['items'])
# print(df.head())

for item in res['items']:
    print(item)

