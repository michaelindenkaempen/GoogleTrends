
#Overview: The purpose of this script is to create the barplots for the city- and regional level comparison. The folder
#csv_manual_regional_comparison contains the manually downloaded datasets obtained from the 'Google Trends' website.
#The script imports csv's from the csv_manual_regional_comparison folder and exports the graph to the /graphs_manual_regional_comparison folder.


#This section imports the packages that are requires to run this script.
import pandas as pd
import plotly_express as px
from matplotlib import pyplot as plt
import geopandas as gpd
import numpy as np
import seaborn as sns
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable

#Setup: To create the graphs, please enter your local directory below.
#Change the variable 'main_directory' to your local export path:
main_directory  = '/Users/michaelindenkampen/PycharmProjects/GoogleTrends/'

#Comparison graph without canary islands

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
plt.title('Search Interest - Autonomous Communities (excl. Canary Islands)')
plt.ylabel('Search Interest')
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.25, top=0.9)
plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_regional_comparison.pdf', format="pdf")

plt.close('all')
del df

#Comparison graph with canary islands

#Make regional comparison graph for spain and export it to /graphs_manual_regional_comparison. I drop regions with no active search interest.
df = pd.read_csv(main_directory + 'csv_manual_regional_comparison/Spain_comparison_regions_en.csv', skiprows= 1)
df.rename(columns={df.columns[0]: 'region', df.columns[1]: 'calima'}, inplace=True)

#To rescale the data, such that the largest item after the canary islands is scaled to index value  = 100, I drop the value for the canary islands,
#aswell as the two regions without any observation. I then rescale the entire column.
df = df.drop(df.index[17])
df = df.drop(df.index[17])
df['calima'] = df['calima'].astype(int)


#This section creates the final barplot.
plt.style.use('ggplot')
plt.figure(figsize=(25, 10))
plt.xticks(rotation=45)
plt.bar(df['region'],df['calima'], color = 'navy' )
plt.title('Search Interest - Autonomous Communities')
plt.ylabel('Search Interest')
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.25, top=0.9)
plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_regional_comparison_with_ci.pdf', format="pdf")

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
fig, ax = plt.subplots(1, 1, figsize = (12,12))

map.plot(column='calima', ax=ax, legend=False, cmap='Blues')

for idx, row in map.iterrows():
    centroid = row['geometry'].centroid
    value = round(row['calima'])
    ax.text(centroid.x, centroid.y, str(value), ha='center', va='center', weight='bold')


# Remove the axis
ax.axis('off')
plt.title('Search Interest - Autonomous Communities')

plt.subplots_adjust(left=0, right=1, bottom=0, top=0.95)  # adjust as needed
plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_regions_comparison_map.pdf', format="pdf")
plt.show()


plt.close('all')

del map
del df


#Make regional comparison graphs with canary islands:
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#Boundary shp. files found in ESP_adm are available at: http://www.diva-gis.org/gdata
boundary_shp = gpd.read_file(main_directory + '/csv_manual_regional_comparison/ESP_adm/ESP_adm1.shp')


#Read in regional data / I drop regions with no active search interest.
df = pd.read_csv(main_directory + 'csv_manual_regional_comparison/Spain_comparison_regions_en.csv', skiprows= 1)
df.rename(columns={df.columns[0]: 'region', df.columns[1]: 'calima'}, inplace=True)

#To rescale the data, such that the largest item after the canary islands is scaled to index value  = 100, I drop the value for the canary islands,
#aswell as the two regions without any observation. I then rescale the entire column.
df = df.drop(df.index[17])
df = df.drop(df.index[17])
df['calima'] = df['calima'].astype(int)

ID_1 = [14,11,3,10,13,1,8,17,6,16,12,2,4,18,5,9,15]

df['ID_1'] = ID_1


# Merge dataframes
map = boundary_shp.set_index('ID_1').join(df.set_index('ID_1'))
map = map.dropna(subset=['calima'])
vmin = map['calima'].min()
vmax = map['calima'].max()

canary_islands = map[map['NAME_1'] == 'Islas Canarias']
map = map[map['NAME_1'] != 'Islas Canarias']



# Create a colormap
cmap = plt.cm.get_cmap('Blues')
norm = colors.Normalize(vmin=vmin, vmax=vmax)

# Plot
fig, ax = plt.subplots(1, 1, figsize = (12,12))
map.plot(column='calima', ax=ax, legend=False, cmap=cmap, norm=norm)

for idx, row in map.iterrows():
    centroid = row['geometry'].centroid
    value = round(row['calima'])
    ax.text(centroid.x, centroid.y, str(value), ha='center', va='center', weight='bold')

plt.title('Search Interest - Autonomous Communities')


# create an inset ax in the bottom right corner, with a width of 30% of the main ax
ax_ins = inset_axes(ax, width="30%", height="30%", loc='lower right')

# plot Canary Islands on the inset ax
canary_islands.plot(column='calima', ax=ax_ins, legend=False, cmap=cmap, norm=norm)

for idx, row in canary_islands.iterrows():
    centroid = row['geometry'].centroid
    value = round(row['calima'])
    ax_ins.text(centroid.x, centroid.y, str(value), ha='center', va='center', weight='bold')

# remove ticks and labels from the inset axes
ax_ins.set_xticks([])
ax_ins.set_yticks([])

# set the background color of the inset axes
ax_ins.patch.set_facecolor('white')


# set the outline color to black
for spine in ax_ins.spines.values():
    spine.set_edgecolor('black')


# Remove the axis
ax.axis('off')

plt.subplots_adjust(left=0, right=1, bottom=0, top=0.95)  # adjust as needed
plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_regions_comparison_map_with_ci.pdf', format="pdf")
plt.show()


plt.close('all')

del map
del df



#Plot map of invidual cities:

from shapely.geometry import Point
from geopy.geocoders import Nominatim
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable



#Initialize the geolocator
geolocator = Nominatim(user_agent="michaelindenkaempen")

#Define function to obtain coordinates for each city
def get_geocode(city):
    location = geolocator.geocode(city + ', Spain')
    if location is not None:
        return location.longitude, location.latitude

df = pd.read_csv(main_directory + 'csv_manual_regional_comparison/Spain_comparison_cities.csv', skiprows= 1)
df.rename(columns={df.columns[0]: 'city', df.columns[1]: 'calima'}, inplace=True)

#Request coordinates:
df['coordinates'] = df['city'].apply(get_geocode)

#Read in boundary file for spain:
boundary_shp = gpd.read_file(main_directory + '/csv_manual_regional_comparison/ESP_adm/ESP_adm1.shp')
#cd = pd.read_csv(main_directory + 'csv_manual_regional_comparison/cities_coordinates.csv', sep = ';')
#cd['coordinates'] = list(zip(cd.longitude, cd.latitude))
#cd['coordinates'] = cd['coordinates'].apply(Point)
#cd = cd.loc[cd['canary_islands'] != 'yes']

#Transform coordinates to Point objects
df['coordinates'] = df['coordinates'].apply(Point)
df_geo = gpd.GeoDataFrame(df, geometry='coordinates', crs=boundary_shp.crs)
df_geo = df_geo.dropna(subset=['calima'])
df_geo = df_geo.loc[df_geo['calima'] != '<1']
df_geo['calima'] = df_geo['calima'].astype(int)


#Log - Normalize the 'numeric_value' column
norm = Normalize(vmin=df_geo['calima'].min(), vmax=df_geo['calima'].max())

#Create the colormap
cmap = ScalarMappable(norm=norm, cmap='Blues')


fig, ax = plt.subplots( figsize = (12,12))
ax.set_xlim([-10, 5])
ax.set_ylim([34.5, 44])

ax.axis('off')
plt.title('Search Interest - Cities (excl. Canary Islands)')


boundary_shp.plot(ax=ax, color='darkgrey', edgecolor='grey',  legend = True)

df_geo.plot( ax=ax, marker='o',color= cmap.to_rgba(df_geo['calima']),edgecolor='black', linewidth=0.5, markersize=30)

#plot colorbar
divider = make_axes_locatable(ax)
cax = divider.append_axes("left", size="2.5%", pad=0.05)
cbar = fig.colorbar(cmap, cax=cax, orientation='vertical')
cbar.set_ticks([vmin, vmax])
cbar.ax.tick_params(color='black', labelcolor='black')

for l in cbar.ax.yaxis.get_ticklabels():
    l.set_weight('bold')

plt.subplots_adjust(left=0, right=1, bottom=0, top=0.95)
plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_cities_comparison_map.pdf', format="pdf")
plt.show()

plt.close('all')



#City plot, including Canary Islands
map = boundary_shp
canary_islands = map[map['NAME_1'] == 'Islas Canarias']
map = map[map['NAME_1'] != 'Islas Canarias']

df_geo['latitude'] = df_geo.geometry.y
vmin = df_geo['calima'].min()
vmax = df_geo['calima'].max()

#Log - Normalize the 'numeric_value' column
norm = Normalize(vmin=df_geo['calima'].min(), vmax=df_geo['calima'].max())

#Create the colormap
cmap = ScalarMappable(norm=norm, cmap='Blues')


cities_canary_islands = df_geo[df_geo['latitude'] <= 33]
df_geo = df_geo[df_geo['latitude'] > 33]

fig, ax = plt.subplots( figsize = (12,12))

ax.axis('off')
plt.title('Search Interest - Cities')


map.plot(ax=ax, color='darkgrey', edgecolor='grey',  legend = True)
df_geo.plot( ax=ax, marker='o',color= cmap.to_rgba(df_geo['calima']), edgecolor='black', linewidth=0.5,  markersize=30)

# plot colorbar
divider = make_axes_locatable(ax)
cax = divider.append_axes("left", size="2.5%", pad=0.05)
cbar = fig.colorbar(cmap, cax=cax, orientation='vertical')
cbar.set_ticks([vmin, vmax])
cbar.ax.tick_params(color='black', labelcolor='black')

for l in cbar.ax.yaxis.get_ticklabels():
    l.set_weight('bold')

# create an inset ax in the bottom right corner, with a width of 30% of the main ax
ax_ins = inset_axes(ax, width="30%", height="30%", loc='lower right')

# remove ticks and labels from the inset axes
ax_ins.set_xticks([])
ax_ins.set_yticks([])

# set the background color of the inset axes
ax_ins.patch.set_facecolor('white')

# set the outline color to black
for spine in ax_ins.spines.values():
    spine.set_edgecolor('black')

# plot Canary Islands on the inset ax
canary_islands.plot( ax=ax_ins, legend=False, color='darkgrey', edgecolor='grey')

cities_canary_islands.plot(column='calima', ax=ax_ins, marker='o', cmap = 'Blues',edgecolor='black', linewidth=0.5,  markersize=30)


plt.subplots_adjust(left=0, right=1, bottom=0, top=0.95)


plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_cities_comparison_map_with_ci.pdf', format="pdf")
plt.show()

plt.close('all')



#Make city comparison graph for spain and export it to /graphs_manual_regional_comparison. The bar plot displays the search interest for the top 25 cities in spain by search interest.
#I drop cities with no active search interest.

df = df_geo

#I select top 25 cities by search interest in the dataset.
df = df.iloc[:25]

#This section creates the final barplot.
df['calima'] = df['calima'].astype(int)
plt.style.use('ggplot')
plt.figure(figsize=(25, 10))
plt.xticks(rotation=75)
plt.bar(df['city'],df['calima'], color = 'navy' )
plt.title('Search Interest - Top 25 Cities (excl. Canary Islands)')
plt.ylabel('Search Interest')
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.25, top=0.9)
plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_cities_comparison_without_CI.pdf', format="pdf")


plt.close('all')
del df