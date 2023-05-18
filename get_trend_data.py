import pytrends
import pandas as pd
from pytrends.request import TrendReq
from matplotlib import pyplot as plt

#Change the variable 'exportpath' to your local export path:
exportpath  = '/Users/michaelindenkampen/PycharmProjects/GoogleTrends/csv_export/'

#To access the regional data using the pytrends package, the user needs to use the relevant geocode.
#Google geocodes can be obtained from: https://www.serpwow.com/docs/search-api/reference/google-trends-geos
region_code = ['AN','AR','AS','IB','PV','CN','CB','CL','CM','CT','EX','GA','RI','MD','MC','NC','VC','CE','ML']
region_name = ['Andalusia','Aragon','Asturias','Balearic Islands','Basque Country','Canary Islands','Cantabria','Castile and Leon','Castile-La Mancha','Catalonia','Extremadura','Galicia','La Rioja','Community of Madrid','Region of Murcia','Navarre','Valencian Community','Ceuta','Melila']

pytrend = TrendReq()

#Download the timeseries data for all spanish regions (2005 - 2014) and save them to the file directory saved in 'exportpath'
for region_i in region_code:
    pytrend.build_payload(kw_list= ['Calima'], cat=0, timeframe='2005-01-01 2014-12-31', geo= 'ES-' + region_i, gprop='')

    df = pytrend.interest_over_time()
    #df = pytrend.interest_by_region(resolution='CITY')

    df.to_csv(exportpath + region_i + '.csv')

#Download the timeseries for spain and save it to the file directory saved in 'exportpath'.
pytrend.build_payload(kw_list= ['Calima'], cat=0, timeframe='2005-01-01 2014-12-31', geo= 'ES', gprop='')

df = pytrend.interest_over_time()
#df = pytrend.interest_by_region(resolution='CITY')

df.to_csv(exportpath + "Spain" + '.csv')

del df

#Make graphs and export them to /graphs.
for region_i in region_code:
    df = pd.read_csv(exportpath + region_i +'.csv')
    df.plot(y = 'Calima')
    plt.savefig
