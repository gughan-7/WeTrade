from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
from wordcloud import wordcloud,STOPWORDS

cred = credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://vtrade-1333d-default-rtdb.asia-southeast1.firebasedatabase.app/'

})

ref = db.reference('/uid/currentuser')
userid = ref.get()

ll = db.reference('traders/'+userid+'/stockdetails')
stocks = ll.get()

portfolio = list(stocks.keys())

now = dt.date.today()
now = now.strftime('%m-%d-%Y')
yesterday = dt.date.today() - dt.timedelta(days = 1)
yesterday = yesterday.strftime('%m-%d-%Y')

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 10
# save the company name in a variable
company_name = str(portfolio[0])
#As long as the company name is valid, not empty...
if company_name != '':
    print(f'Searching for and analyzing {company_name}, Please be patient, it might take a while...')

    #Extract News with Google News
    googlenews = GoogleNews(start=yesterday,end=now)
    googlenews.search(company_name)
    result = googlenews.result()
#     result = googlenews.get_texts()
    #store the results
#     df = pd.DataFrame(result)
#     k = (df[0:4])
    print((result))
#     for i in result:
#         print(i)
#         print("\n\n")
