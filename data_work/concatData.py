import pandas as pd
from collectData import crime_list

for crime in crime_list:
    print(crime.dataFrame)


# df = pd.read_csv('./data/Assualt.csv')
# print(df.columns)
