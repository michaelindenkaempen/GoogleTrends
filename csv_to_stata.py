
#Overview: This script reads in the csv files and converts them to .dta files. The script also creates "master" files, that contain all regions.

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
master_export = pd.DataFrame()

#Import csv's and save them as .dta files
for region_i in region_code:
    df = pd.read_csv(main_directory + 'csv_export/' + region_i +'.csv')
    df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
    df = df.drop(df.columns[2], axis = 1)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['calima'] = df['calima'].replace('<1', '0')
    df['calima'] = df['calima'].astype(int)
    df['geocode'] = region_i
    master_export = pd.concat([master_export, df])
    df.to_stata(main_directory + 'dta_export/' + region_i + '.dta')


df = pd.read_csv(main_directory + 'csv_export/' + 'Spain' +'.csv')
df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
df = df.drop(df.columns[2], axis=1)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df['calima'] = df['calima'].replace('<1', '0')
df['calima'] = df['calima'].astype(int)
df['geocode'] = 'ES'
master_export = pd.concat([master_export, df])
df.to_stata(main_directory + 'dta_export/' + 'Spain' '.dta')

master_export.to_stata(main_directory + 'dta_master_files/' + 'master_export.dta')


#Regional timeseries, manual download (csv_manual)
master_manual = pd.DataFrame()

for region_i in region_code:
    df = pd.read_csv(main_directory + 'csv_manual/' + region_i +'_m.csv', skiprows = 1)
    df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['calima'] = df['calima'].replace('<1', '0')
    df['calima'] = df['calima'].astype(int)
    df['geocode'] = region_i
    master_manual = pd.concat([master_manual, df])
    df.to_stata(main_directory + 'dta_manual/' + region_i + '_m.dta')


df = pd.read_csv(main_directory + 'csv_manual/' + 'Spain' +'_m.csv', skiprows = 1)
df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df['calima'] = df['calima'].replace('<1', '0')
df['calima'] = df['calima'].astype(int)
df['geocode'] = 'ES'
master_manual = pd.concat([master_manual, df])
df.to_stata(main_directory + 'dta_manual/' + 'Spain' '_m.dta')

master_manual.to_stata(main_directory + 'dta_master_files/' + 'master_m.dta')


#Regional comparison timeseries, manual download (csv_manual_comparison)
master_manual_comparison = pd.DataFrame()

for region_i in region_code:
    df = pd.read_csv(main_directory + 'csv_manual_comparison/' + region_i +'_m_comp.csv', skiprows = 1)
    df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima', df.columns[2]: 'contaminacion'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['calima'] = df['calima'].replace('<1', '0')
    df['calima'] = df['calima'].astype(int)
    df['contaminacion'] = df['contaminacion'].replace('<1', '0')
    df['contaminacion'] = df['contaminacion'].astype(int)
    df['geocode'] = region_i
    master_manual_comparison = pd.concat([master_manual_comparison, df])
    df.to_stata(main_directory + 'dta_manual_comparison/' + region_i + '_m_comp.dta')


df = pd.read_csv(main_directory + 'csv_manual_comparison/' + 'Spain' +'_m_comp.csv', skiprows = 1)
df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima', df.columns[2]: 'contaminacion'}, inplace=True)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df['calima'] = df['calima'].replace('<1', '0')
df['calima'] = df['calima'].astype(int)
df['contaminacion'] = df['contaminacion'].replace('<1', '0')
df['contaminacion'] = df['contaminacion'].astype(int)
df['geocode'] = 'ES'
master_manual_comparison = pd.concat([master_manual_comparison, df])
df.to_stata(main_directory + 'dta_manual_comparison/' + 'Spain' '_m_comp.dta')

master_manual_comparison.to_stata(main_directory + 'dta_master_files/' + 'master_m_comparison.dta')




#Regional comparison timeseries, manual download (csv_manual_comparison)
master_manual_long = pd.DataFrame()

for region_i in region_code:
    df = pd.read_csv(main_directory + 'csv_manual_long/' + region_i +'_m_long.csv', skiprows = 1)
    df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['calima'] = df['calima'].replace('<1', '0')
    df['calima'] = df['calima'].astype(int)
    df['geocode'] = region_i
    master_manual_long = pd.concat([master_manual_long, df])
    df.to_stata(main_directory + 'dta_manual_long/' + region_i + '_m_long.dta')


df = pd.read_csv(main_directory + 'csv_manual_long/' + 'Spain' +'_m_long.csv', skiprows = 1)
df.rename(columns={df.columns[0]: 'date', df.columns[1]: 'calima'}, inplace=True)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df['calima'] = df['calima'].replace('<1', '0')
df['calima'] = df['calima'].astype(int)
df['geocode'] = 'ES'
master_manual_long = pd.concat([master_manual_long, df])
df.to_stata(main_directory + 'dta_manual_long/' + 'Spain' '_m_long.dta')

master_manual_long.to_stata(main_directory + 'dta_master_files/' + 'master_m_long.dta')




#Create master stata file that contains all variables:
master_manual_comparison.rename(columns={master_manual_comparison.columns[0]: 'calima_comparison', master_manual_comparison.columns[1]: 'contaminacion_comparison', master_manual_comparison.columns[2]: 'geocode'}, inplace=True)
master_manual.rename(columns={master_manual.columns[0]: 'calima_manual', master_manual_comparison.columns[1]: 'geocode'}, inplace=True)
master_export.rename(columns={master_export.columns[0]: 'calima_export', master_manual_comparison.columns[1]: 'geocode'}, inplace=True)

master = master_manual_comparison.reset_index().merge(master_manual.reset_index(), how='inner', on=['geocode', 'date'])
master = master.merge(master_export.reset_index(), how='inner', on=['geocode', 'date'])




#This section of the code creates the scaled variants of the variables. The variables are scaled by the regional search interest for the relevant time period (01.01.2005 - 31.12.2014 for the shorter period, 01.01.2005 - today (19.05.2023) for the 'long' period).

#Create scaled variables:

#Read in regional data: The regional comparison data serves as the scaling factor. The regional comparison data is the same that is used for the regional maps.
df = pd.read_csv(main_directory + 'csv_manual_regional_comparison/Spain_comparison_regions_en.csv', skiprows= 1)
df.rename(columns={df.columns[0]: 'region', df.columns[1]: 'scaling_factor'}, inplace=True)

# I drop regions with no observations for the regional search interest. (Ceuta and Melilla)
df = df.drop(df.index[17])
df = df.drop(df.index[17])

#I convert the scaling value to an integer value.
df['scaling_factor'] = df['scaling_factor'].astype(int)

#String cleaning:
df['region'] = df['region'].replace('Castile and León', 'Castile and Leon')

#I merge the regional data/ the scaling factor values with the master dataset:
region_info = region_info.rename(columns={region_info.columns[0]: 'geocode', region_info.columns[1]: 'region'})
df = df.merge(region_info, how = 'left', on = ['region'])
master = master.merge(df, how = 'left', on = ['geocode'])

#Compute scaled versions of the variables:
master['calima_comparison_scaled'] = master['calima_comparison'] * master['scaling_factor'] / 100
master['contaminacion_comparison_scaled'] = master['contaminacion_comparison'] * master['scaling_factor'] / 100
master['calima_export_scaled'] = master['calima_export'] * master['scaling_factor'] / 100
master['calima_manual_scaled'] = master['calima_manual'] * master['scaling_factor'] / 100



#Move geocode and region column to the end of the dataframe (entirely cosmetic)
cols = list(master.columns)
cols.append(cols.pop(cols.index('geocode')))
cols.append(cols.pop(cols.index('region')))
master = master[cols]

#Drop region column (cosmetic)
master = master.drop('region', axis = 1)

#Set the date variable as the index and export the dataframe to the .dta format.
master.set_index('date').to_stata(main_directory + 'dta_master_files/master_all_variables.dta')



#I then create rescaled version of the 'long' version.

#Create scaled variables:

#Read in regional data: I drop regions with no active search interest. The regional comparison data serves as the scaling factor. The regional comparison data is the same that is used for the regional maps.
df = pd.read_csv(main_directory + 'csv_manual_regional_comparison/spain_comparison_regions_long_en.csv', skiprows= 1)
df.rename(columns={df.columns[0]: 'region', df.columns[1]: 'scaling_factor'}, inplace=True)


#I convert the scaling value to an integer value.
df['scaling_factor'] = df['scaling_factor'].astype(int)

#String cleaning:
df['region'] = df['region'].replace('Castile and León', 'Castile and Leon')
df['region'] = df['region'].replace('Melilla', 'Melila')

#I merge the regional data/ the scaling factor values with the master dataset:
region_info = region_info.rename(columns={region_info.columns[0]: 'geocode', region_info.columns[1]: 'region'})
df = df.merge(region_info, how = 'left', on = ['region'])
master_manual_long = master_manual_long.reset_index().merge(df, how = 'left', on = ['geocode'])

#Compute scaled versions of the variables:
master_manual_long['calima_scaled'] = master_manual_long['calima'] * master_manual_long['scaling_factor'] / 100

#Drop region column
master_manual_long = master_manual_long.drop('region', axis = 1)

#Set date as the index and export the dataframe to the .dta format.
master_manual_long.set_index('date').to_stata(main_directory + 'dta_master_files/master_m_long.dta')



#Clear datasets from memory

del master_manual_comparison
del master_manual
del master_export
del master_manual_long
