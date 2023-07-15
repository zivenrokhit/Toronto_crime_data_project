import requests
import pandas as pd

url = 'https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Major_Crime_Indicators_Open_Data/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'

response = requests.get(url)
data = response.json()

features = data['features']
records = [feature['attributes'] for feature in features]
df = pd.DataFrame(records)
print(len(df.columns))
