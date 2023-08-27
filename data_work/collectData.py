import requests
import pandas as pd

url = 'https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Major_Crime_Indicators_Open_Data/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'

response = requests.get(url)
data = response.json()

features = data['features']
records = [feature['attributes'] for feature in features]
df = pd.DataFrame(records)


# general_crimes includes: assualt, robbery, break and enter, auto theft, theft over
# resultOffset=400 can be changed to choose from 400 - 2400 so you can iterivly change the value
crime_api_data = {
    'assualt': ('https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Assault_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson', 173238),
    'auto_theft': ('https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Auto_Theft_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson', 46048),
    'break_and_enter': ('https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Break_and_Enter_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson', 62527),
    'homicide': ('https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Homicides_Open_Data_ASR_RC_TBL_002/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson', 1322),
    'robbery': ('https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Robbery_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson', 30738),
    'theft_over': ('https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Theft_Over_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson', 10745),
    'bicycle_theft': ('https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Bicycle_Thefts_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson', 31970),
    'shootings': ('https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Shooting_and_Firearm_Discharges_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson',  5707),
    'theft_from_motor': ('https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Theft_From_Motor_Vehicle_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson', 81651)}


def fetchCrimeDataFromApi(url):
    response = requests.get(url)
    data = response.json()
    entries = data['features']
    cleaned_entries = []
    for entry in entries:
        cleaned_entries.append(entry['properties'])
    df = pd.DataFrame(cleaned_entries)
    return df


def collectData(url, data_length):
    df = pd.DataFrame()
    url = url + '&resultOffset={0}'
    resultOffset = 0
    while len(df) < data_length:
        iterativeResponse = fetchCrimeDataFromApi(url.format(resultOffset))
        df = pd.concat([df, iterativeResponse], ignore_index=True)
        resultOffset += 2000
        # print(len(df))
    return df


class Crime:
    def __init__(self, type, apiURL, dataLength, headers=None, dataFrame=None):
        self.type = type
        self.apiURL = apiURL
        self.dataLength = dataLength
        self.headers = headers
        self.dataFrame = dataFrame

    def createDataframe(self):
        self.dataFrame = collectData(self.apiURL, self.dataLength)
        self.headers = self.dataFrame.columns

    def compareHeaders(self, crime):
        return 'not made yet'

    def combineDfs(self, crime):
        # combines both crime's dataframes
        # AND RETURNS A DATAFRAME
        return 'not made yet'


# homicide = Crime(type="Robbery", apiURL="https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Robbery_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson", dataLength=30738)
# homicide.createDataframe()
# print(homicide.headers)


Assualt = Crime(
    'Assualt', crime_api_data['assualt'][0], crime_api_data['assualt'][1])
AutoTheft = Crime(
    'Auto Theft', crime_api_data['auto_theft'][0], crime_api_data['auto_theft'][1])
BreakAndEnter = Crime(
    'Break And Enter', crime_api_data['break_and_enter'][0], crime_api_data['break_and_enter'][1])
Homicide = Crime(
    'Homicide', crime_api_data['homicide'][0], crime_api_data['homicide'][1])
Robbery = Crime(
    'Robbery', crime_api_data['robbery'][0], crime_api_data['robbery'][1])
TheftOver = Crime(
    'Theft Over', crime_api_data['theft_over'][0], crime_api_data['theft_over'][1])
BicycleTheft = Crime(
    'Bicycle Theft', crime_api_data['bicycle_theft'][0], crime_api_data['bicycle_theft'][1])
Shootings = Crime(
    'Shootings', crime_api_data['shootings'][0], crime_api_data['shootings'][1])
TheftFromMotor = Crime(
    'theft_from_motor', crime_api_data['theft_from_motor'][0], crime_api_data['theft_from_motor'][1])

crime_list = [Assualt, AutoTheft, BreakAndEnter, Homicide, Robbery,
              TheftOver, BicycleTheft, Shootings, TheftFromMotor]

# for crime in crime_list:
#     crime.createDataframe()
#     crime.dataFrame.to_csv(crime.type + '.csv', index=False)
