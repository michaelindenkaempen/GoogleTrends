


#This section imports the packages that are requires to run this script.
import pytrends
import pandas as pd


#To access the regional data using the pytrends package, the user needs to use the relevant geocode.
#Google geocodes can be obtained from: https://www.serpwow.com/docs/search-api/reference/google-trends-geos
region_code = ['AN','AR','AS','IB','PV','CN','CB','CL','CM','CT','EX','GA','RI','MD','MC','NC','VC','CE','ML']
region_name = ['Andalusia','Aragon','Asturias','Balearic Islands','Basque Country','Canary Islands','Cantabria','Castile and Leon','Castile-La Mancha','Catalonia','Extremadura','Galicia','La Rioja','Community of Madrid','Region of Murcia','Navarre','Valencian Community','Ceuta','Melila']
region_info = pd.DataFrame({'region_code': region_code, 'region_name': region_name})

#Change the variable 'main_directory' to your local export path:
main_directory  = '/Users/michaelindenkampen/PycharmProjects/GoogleTrends/'


#Regional timeseries, obtained from API (csv_export)

#Import csv's and save them as .dta files
for region_i in region_code:
    df = pd.read_csv(main_directory + 'csv_export/' + region_i +'.csv', skiprows = 1)
    df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
    df = df.drop(df.columns[2], axis = 1)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['calima'] = df['calima'].replace('<1', '0')
    df['calima'] = df['calima'].astype(int)
    df['geocode'] = region_i
    df.to_stata(main_directory + 'dta_export/' + region_i + '.dta')


df = pd.read_csv(main_directory + 'csv_export/' + 'Spain' +'.csv', skiprows = 1)
df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df['calima'] = df['calima'].replace('<1', '0')
df['calima'] = df['calima'].astype(int)
df['geocode'] = 'Spain'
df.to_stata(main_directory + 'dta_export/' + 'Spain' '.dta')


#Regional timeseries, manual download (csv_manual)
for region_i in region_code:
    df = pd.read_csv(main_directory + 'csv_manual/' + region_i +'_m.csv', skiprows = 1)
    df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['calima'] = df['calima'].replace('<1', '0')
    df['calima'] = df['calima'].astype(int)
    df['geocode'] = region_i
    df.to_stata(main_directory + 'dta_manual/' + region_i + '_m.dta')


df = pd.read_csv(main_directory + 'csv_manual/' + 'Spain' +'_m.csv', skiprows = 1)
df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df['calima'] = df['calima'].replace('<1', '0')
df['calima'] = df['calima'].astype(int)
df['geocode'] = 'Spain'
df.to_stata(main_directory + 'dta_manual/' + 'Spain' '_m.dta')



#Regional comparison timeseries, manual download (csv_manual_comparison)
for region_i in region_code:
    df = pd.read_csv(main_directory + 'csv_manual_comparison/' + region_i +'_m_comp.csv', skiprows = 1)
    df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima', df.columns[2]: 'contaminacion'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['calima'] = df['calima'].replace('<1', '0')
    df['calima'] = df['calima'].astype(int)
    df['geocode'] = region_i
    df.to_stata(main_directory + 'dta_manual_comparison/' + region_i + '_m_comp.dta')


df = pd.read_csv(main_directory + 'csv_manual_comparison/' + 'Spain' +'_m_comp.csv', skiprows = 1)
df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima', df.columns[2]: 'contaminacion'}, inplace=True)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df['calima'] = df['calima'].replace('<1', '0')
df['calima'] = df['calima'].astype(int)
df['geocode'] = 'Spain'
df.to_stata(main_directory + 'dta_manual_comparison/' + 'Spain' '_m_comp.dta')



#Regional comparison timeseries, manual download (csv_manual_comparison)
for region_i in region_code:
    df = pd.read_csv(main_directory + 'csv_manual_long/' + region_i +'_m_long.csv', skiprows = 1)
    df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['calima'] = df['calima'].replace('<1', '0')
    df['calima'] = df['calima'].astype(int)
    df['geocode'] = region_i
    df.to_stata(main_directory + 'dta_manual_long/' + region_i + '_m_long.dta')


df = pd.read_csv(main_directory + 'csv_manual_long/' + 'Spain' +'_m_long.csv', skiprows = 1)
df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df['calima'] = df['calima'].replace('<1', '0')
df['calima'] = df['calima'].astype(int)
df['geocode'] = 'Spain'
df.to_stata(main_directory + 'dta_manual_long/' + 'Spain' '_m_long.dta')
