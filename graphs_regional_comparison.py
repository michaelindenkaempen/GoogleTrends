
#Overview: The purpose of this script is to create the barplots for the city- and regional level comparison. The folder
#csv_manual_regional_comparison contains the manually downloaded datasets obtained from the 'Google Trends' website.
#The script imports csv's from the csv_manual_regional_comparison folder and exports the graph to the /graphs_manual_regional_comparison folder.


#This section imports the packages that are requires to run this script.
import pandas as pd
import plotly_express as px
from matplotlib import pyplot as plt
import geopandas as gpd
import pandas as pd
import seaborn as sns

#Setup: To create the graphs, please enter your local directory below.
#Change the variable 'main_directory' to your local export path:
main_directory  = '/Users/michaelindenkampen/PycharmProjects/GoogleTrends/'



#Make regional comparison graph for spain and export it to /graphs_manual_regional_comparison. I drop regions with no active search interest.
df = pd.read_csv(main_directory + 'csv_manual_regional_comparison/Spain_comparison_regions_en.csv', skiprows= 1)
df.rename(columns={df.columns[0]: 'region', df.columns[1]: 'calima'}, inplace=True)

#To rescale the data, such that the largest item after the canary islands is scaled to index value  = 100, I drop the value for the canary islands,
#aswell as the two regions without any observation. I then rescale the entire column.
df = df.drop(df.index[0])
df = df.drop(df.index[16])
df = df.drop(df.index[16])
df['calima'] = df['calima'].astype(int)
df['calima'] = (df['calima'] / df['calima'].iloc[0]) * 100


#This section creates the final barplot.
plt.style.use('ggplot')
plt.figure(figsize=(25, 10))
plt.xticks(rotation=45)
plt.bar(df['region'],df['calima'], color = 'navy' )
plt.title('Search Interest - Autonomous Communities')
plt.ylabel('Search Interest')
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.25, top=0.9)
plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_regional_comparison.pdf', format="pdf")

plt.close('all')
del df


#Make city comparison graph for spain and export it to /graphs_manual_regional_comparison. The bar plot displays the search interest for the top 25 cities in spain by search interest.
#I drop cities with no active search interest.

df = pd.read_csv(main_directory + 'csv_manual_regional_comparison/Spain_comparison_cities.csv', skiprows= 1)
df.rename(columns={df.columns[0]: 'city', df.columns[1]: 'calima'}, inplace=True)

#I select top 25 cities by search interest in the dataset.
df = df.iloc[:25]

#This section creates the final barplot.
df['calima'] = df['calima'].astype(int)
plt.style.use('ggplot')
plt.figure(figsize=(25, 10))
plt.xticks(rotation=75)
plt.bar(df['city'],df['calima'], color = 'navy' )
plt.title('Search Interest - Top 25 Cities ')
plt.ylabel('Search Interest')
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.25, top=0.9)
plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_cities_comparison.pdf', format="pdf")


plt.close('all')
del df



#Make regional comparison graphs:
#Boundary shp. files found in ESP_adm are available at: http://www.diva-gis.org/gdata

boundary_shp = gpd.read_file(main_directory + '/csv_manual_regional_comparison/ESP_adm/ESP_adm1.shp')


#Read in regional data / I drop regions with no active search interest.
df = pd.read_csv(main_directory + 'csv_manual_regional_comparison/Spain_comparison_regions_en.csv', skiprows= 1)
df.rename(columns={df.columns[0]: 'region', df.columns[1]: 'calima'}, inplace=True)

#To rescale the data, such that the largest item after the canary islands is scaled to index value  = 100, I drop the value for the canary islands,
#aswell as the two regions without any observation. I then rescale the entire column.
df = df.drop(df.index[0])
df = df.drop(df.index[16])
df = df.drop(df.index[16])
df['calima'] = df['calima'].astype(int)
df['calima'] = (df['calima'] / df['calima'].iloc[0]) * 100

ID_1 = [11,3,10,13,1,8,17,6,16,12,2,4,18,5,9,15]

df['ID_1'] = ID_1


# Merge dataframes
map = boundary_shp.set_index('ID_1').join(df.set_index('ID_1'))
map = map.dropna(subset=['calima'])

# Plot
fig, ax = plt.subplots(1, 1)
map.plot(column='calima', ax=ax, legend=False, cmap='Blues')

for idx, row in map.iterrows():
    centroid = row['geometry'].centroid
    value = round(row['calima'])
    ax.text(centroid.x, centroid.y, str(value), ha='center', va='center', weight='bold')

# Remove the axis
ax.axis('off')
plt.title('Search Interest - Autonomous Communities')
plt.subplots_adjust(left=0.005, right=0.995, bottom=0.005, top=0.9)
plt.show()

plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_regions_comparison_map.pdf', format="pdf")

plt.close('all')

del map
del df