
#Overview: This script creates the graphs for the comparison between the 'calima' and 'contaminacion' search interest, for year 2005 - 2014.
#I chose to manually download the data due to data issues which are discussed in the following
# thread: https://github.com/GeneralMills/pytrends/issues/577 . The script imports files from /csv_manual_comparisonand exports the graphs
#to the /graphs_manual_comparison folder.


#This section imports the packages that are requires to run this script.
import pytrends
import pandas as pd
from pytrends.request import TrendReq
from matplotlib import pyplot as plt


#Change the variable 'main_directory' to your local export path:
main_directory  = '/Users/michaelindenkampen/PycharmProjects/GoogleTrends/'


#To access the regional data using the pytrends package, the user needs to use the relevant geocode.
#Google geocodes can be obtained from: https://www.serpwow.com/docs/search-api/reference/google-trends-geos
region_code = ['AN','AR','AS','IB','PV','CN','CB','CL','CM','CT','EX','GA','RI','MD','MC','NC','VC','CE','ML']
region_name = ['Andalusia','Aragon','Asturias','Balearic Islands','Basque Country','Canary Islands','Cantabria','Castile and Leon','Castile-La Mancha','Catalonia','Extremadura','Galicia','La Rioja','Community of Madrid','Region of Murcia','Navarre','Valencian Community','Ceuta','Melila']
region_info = pd.DataFrame({'region_code': region_code, 'region_name': region_name})


#Make regional graphs and export them to /graphs.
for region_i in region_code:
    df = pd.read_csv(main_directory + 'csv_manual_comparison/' + region_i +'_m_comp.csv', skiprows = 1)
    df.rename(columns={'Monat': 'date', df.columns[1]: 'calima', df.columns[2]: 'contaminacion'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['calima'] = df['calima'].replace('<1', '0')
    df['calima'] = df['calima'].astype(int)
    df['contaminacion'] = df['contaminacion'].replace('<1', '0')
    df['contaminacion'] = df['contaminacion'].astype(int)
    plt.style.use('ggplot')
    df.plot(y= ['calima','contaminacion'],  color=['black','red'], figsize=(10, 6))
    plt.title(region_info.loc[region_info['region_code'] == region_i, 'region_name'].values[0])
    plt.xlabel('')
    plt.ylabel('Search Interest')
    plt.savefig(main_directory + 'graphs_manual_comparison/' + region_info.loc[region_info['region_code'] == region_i, 'region_name'].values[0] + '_m_comp.pdf', format="pdf")
    plt.close('all')

#Make graph for Spain and export it to /graphs
df = pd.read_csv(main_directory + 'csv_manual_comparison/Spain_m_comp.csv', skiprows= 1)
df.rename(columns={'Monat': 'date', 'Calima: (Spanien)': 'calima', 'contaminacion: (Spanien)':'contaminacion'}, inplace=True)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
plt.style.use('ggplot')
df.plot(y= ['calima','contaminacion'],  color=['black','red'], figsize=(10, 6))
plt.title('Spain')
plt.xlabel('')
plt.ylabel('Search Interest')
plt.savefig(main_directory + 'graphs_manual_comparison/Spain_m_comp.pdf', format="pdf")
