import requests
import pandas as pd
import os


food_name = input('Input a type of food: ')

api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(food_name)
response = requests.get(api_url, headers={'X-Api-Key': os.environ.get('API_KEY')})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

food_data = response.json()
print(food_data)
# food_data_df = pd.DataFrame.from_dict(food_data)
# print(food_data_df)
# print(food_data_df['calories'])

