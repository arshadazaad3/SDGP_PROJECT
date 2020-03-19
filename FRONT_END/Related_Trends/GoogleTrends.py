from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import pandas as pd

import datetime
from datetime import date
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

keywordToSearch = "coronavirus"

user_cat = 0  # Category of focus: all
user_timeframe = 'today 5-y'  # Timeframe of analysis: last 5 years
user_geo = ''  # Country of focus: worldwide

user_keyword_list = [keywordToSearch]
print (user_keyword_list)

answer = input('Do you want to pick from speciific category? (e.g. Art & Entertainment) (Yes/No): ')

if answer.upper() == "YES":
    category_list = 'Here is the list of categories: \n Arts & Entertainment: 3 \n Autos & Vehicles: 47 \n Beauty & Fitness: 44 \n Books & Literature: 22 \n Business & Industrial: 12 \n Computers & Electronics: 5 \n Finance: 7 \n Food & Drink: 71 \n Games: 8 \n Health: 45 \n Hobbies & Leisure: 65 \n Internet & Telecom: 13 \n Home & Garden: 11 \n Law & Government: 19 \n Jobs & Education: 958 \n News: 16 \n Online Communities: 299 \n People & Society: 14 \n Pets & Animals: 66 \n Real Estate: 29 \n Reference: 533 \n Science: 174 \n Shopping: 18 \n Sports: 20 \n Travel: 67'
    print (category_list)
    user_category = int(input('Please indicate the code of the category to focus on: '))

list_of_cat = [3, 47, 44, 22, 12, 5, 7, 71, 8, 45, 65, 11, 13, 958, 19, 16, 299, 14, 66, 29, 533, 174, 18, 20, 67]
if answer.upper() == "YES":
    if user_category in list_of_cat:
        print ('Category is now set')
    else:
        user_category = int(input('Category code not valid, please indicate the right code: '))
        if user_category in list_of_cat:
            print ('Category is now set')
        else:
            user_cat = int(input('Category code not valid, please indicate the right code: '))
            if user_category in list_of_cat:
                print ('Category is now set')
            else:
                user_category = int(input('Category code not valid, please indicate the right code: '))

numdays = 7
numweeks = 52
numyears = 1
total_time_range = numdays * numweeks * numyears

end_date = date.today()
today_date = date.today()
end_date = today_date
begin_date = end_date - datetime.timedelta(days=total_time_range - 7)
user_timeframe = begin_date.strftime('%Y-%m-%d') + ' ' + end_date.strftime('%Y-%m-%d')
print(user_timeframe)

pytrend = TrendReq()

pytrend.build_payload(kw_list=user_keyword_list, cat=user_cat, timeframe=user_timeframe, geo=user_geo)

interest_over_time = pytrend.interest_over_time()
print(interest_over_time)

interest_by_region_df = pytrend.interest_by_region(inc_low_vol=False)
# print(interest_by_region_df.head())
#
print('\n RANKED COUNTRIES THAT SEARCHED FOR THE  KEYWORD "', keywordToSearch, '"')
print("")
print(interest_by_region_df.sort_values(by=keywordToSearch, ascending=False)[keywordToSearch])

related_queries_dict = pytrend.related_queries()

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print("\n RELATED QUERIES\n")
print(related_queries_dict)

# trending searches
print (" \n TRENDING SEARCHES \n ")
trending_searches_df = pytrend.trending_searches()
print(trending_searches_df.head())

# Get Google Top Charts for Component 3
print (" \n GOOGLE SEARCH TOP CHARTS \n ")
top_charts_df = pytrend.top_charts(2019, hl='en-US', tz=300, geo='GLOBAL')
print(top_charts_df.head())

# What is Searched Today

print (" \n WHAT IS SEARCHED TODAY \n ")

today_searches_df = pytrend.today_searches()
print(today_searches_df.head())

print(pytrend.suggestions(keyword=keywordToSearch))
