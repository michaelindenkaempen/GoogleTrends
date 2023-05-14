import pytrends
import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

#pytrend.build_payload(kw_list = ['Corona'], geo = 'DE')

pytrend.build_payload(kw_list= ['Calima'], cat=0, timeframe='all', geo='ES', gprop='')

df = pytrend.interest_over_time()
#df = pytrend.interest_by_region(resolution='CITY')


df = pytrend.interest_over_time()


df = pytrend.top_charts(2019, hl='en-US', tz=300, geo='US-CA')
df = pytrend.interest_over_time()

df.head(10)

df = pytrend.interest_by_region()

df['Calima'].plot()


df.plot(y  = 'Calima')
