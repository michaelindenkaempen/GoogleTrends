#Make regional comparison graph for spain and export it to /graphs_manual_regional_comparison
df = pd.read_csv(main_directory + 'csv_manual_regional_comparison/Spain_comparison_regions.csv', skiprows= 1)
df.rename(columns={df.columns[0]: 'region', df.columns[1]: 'calima'}, inplace=True)
df = df.drop(df.index[0])
df = df.drop(df.index[16])
df = df.drop(df.index[16])
df['calima'] = (df['calima'] / df['calima'].iloc[0]) * 100
plt.figure(figsize=(25, 10))
plt.xticks(rotation=45)
plt.bar(df['region'],df['calima'], color = 'navy' )
plt.title('Search Interest - Regional Comparison')
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.25, top=0.9)
plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_regional_comparison.pdf', format="pdf")

plt.close('all')
del df


#Make city comparison graph for spain and export it to /graphs_manual_regional_comparison
df = pd.read_csv(main_directory + 'csv_manual_regional_comparison/Spain_comparison_cities.csv', skiprows= 1)
df.rename(columns={df.columns[0]: 'city', df.columns[1]: 'calima'}, inplace=True)
df = df.iloc[:25]
plt.figure(figsize=(25, 10))
plt.xticks(rotation=75)
plt.bar(df['city'],df['calima'], color = 'navy' )
plt.title('Search Interest - Regional Comparison')
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.25, top=0.9)
plt.savefig(main_directory + 'graphs_manual_regional_comparison/Spain_cities_comparison.pdf', format="pdf")
