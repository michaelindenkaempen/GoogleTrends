
#This section imports the packages that are requires to run this script.
import pytrends
import pandas as pd
from pytrends.request import TrendReq
from matplotlib import pyplot as plt



#Change the variable 'main_directory' to your local export path:
main_directory  = '/Users/michaelindenkampen/PycharmProjects/GoogleTrends/'

#Set the relevant keyword, e.g. 'Calima'
search_term = 'Calima'

#To access the regional data using the pytrends package, the user needs to use the relevant geocode.
#Google geocodes can be obtained from: https://www.serpwow.com/docs/search-api/reference/google-trends-geos
region_code = ['AN','AR','AS','IB','PV','CN','CB','CL','CM','CT','EX','GA','RI','MD','MC','NC','VC','CE','ML']
region_name = ['Andalusia','Aragon','Asturias','Balearic Islands','Basque Country','Canary Islands','Cantabria','Castile and Leon','Castile-La Mancha','Catalonia','Extremadura','Galicia','La Rioja','Community of Madrid','Region of Murcia','Navarre','Valencian Community','Ceuta','Melila']
region_info = pd.DataFrame({'region_code': region_code, 'region_name': region_name})

pytrend = TrendReq()


#Download the timeseries data for all spanish regions (2005 - 2014) and save them to the file directory saved in 'main_directory'
for region_i in region_code:
    pytrend.build_payload(kw_list= [search_term], timeframe='2005-01-01 2014-12-31', geo= 'ES-' + region_i)

    df = pytrend.interest_over_time()

    df.to_csv(main_directory+ 'csv_export/' + region_i + '.csv')


#Download the timeseries for spain and save it to the file directory saved in 'main_directory'.
pytrend.build_payload(kw_list= [search_term] , timeframe='2005-01-01 2014-12-31', geo= 'ES')

df = pytrend.interest_over_time()

df.to_csv(main_directory + 'csv_export/' + 'Spain' + '.csv')

del df


#Make regional graphs and export them to /graphs.
for region_i in region_code:
    df = pd.read_csv(main_directory + 'csv_export/' + region_i +'.csv', parse_dates= ['date'], index_col = ['date'])
    df.plot(y = search_term, legend = None,  color='black', figsize=(10, 6))
    plt.title(region_info.loc[region_info['region_code'] == region_i, 'region_name'].values[0])
    plt.xlabel('')
    plt.ylabel('Search Interest')
    plt.savefig(main_directory + 'graphs/' + region_info.loc[region_info['region_code'] == region_i, 'region_name'].values[0] + '.pdf', format="pdf")

#Make graph for spain and export it to /graphs
df = pd.read_csv(main_directory + 'csv_export/Spain.csv', parse_dates=['date'], index_col=['date'])
plt.style.use('ggplot')
df.plot(y= search_term, legend=None,  color='black', figsize=(10, 6))
plt.title('Spain')
plt.xlabel('')
plt.ylabel('Search Interest')
plt.savefig(main_directory + 'graphs/Spain.pdf', format="pdf")
