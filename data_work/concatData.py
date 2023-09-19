import pandas as pd


crime_dataframes = ['Assualt', 'Auto Theft', 'Bicycle Theft', 'Break And Enter',
                    'Homicide', 'Motor Theft', 'Robbery', 'Shootings', 'Theft Over']
for i in range(len(crime_dataframes)):
    df = pd.read_csv(f'data/{crime_dataframes[i]}.csv')
    crime_dataframes[i] = df

crime_headers_list = []
for crime in crime_dataframes:
    crime_headers_list.append(crime.columns)


def find_set_intersection(los, item):
    if len(los) == 0:
        return True
    return item in los[0] and find_set_intersection(los[1:], item)


crime_header_intersections = []
for headers in crime_headers_list:
    for i in range(len(headers)):
        if find_set_intersection(crime_headers_list, headers[i]):
            if headers[i] not in crime_header_intersections:
                crime_header_intersections.append(headers[i])

# checks if intersection_headers are in all dfs
# for intersection_header in crime_header_intersections:
#     for header_list in crime_headers_list:
#         if intersection_header not in header_list:
#             print(False)


for df in crime_dataframes:
    for header in df.columns:
        if header not in crime_header_intersections:
            df = df.drop(columns=[header])

for df in crime_dataframes:
    print(len(df.columns))

combined_crime_df = pd.DataFrame()

for df in crime_dataframes:
    combined_crime_df = pd.concat([combined_crime_df, df])
