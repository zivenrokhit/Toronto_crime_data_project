import folium
from concatData import combined_crime_df

map = folium.Map(location=[43.6532, -79.3832])

for index, row in combined_crime_df.iterrows():
    if index == 100:
        break
    # folium.Marker((row['LAT_WGS84'], row['LONG_WGS84']),
    #               popup=row['EVENT_UNIQUE_ID']).add_to(map)
    folium.Marker((row['LAT_WGS84'], row['LONG_WGS84']),
                  popup=row['PRIMARY_OFFENCE']).add_to(map)


print(combined_crime_df.columns)
# map.save('index.html')
