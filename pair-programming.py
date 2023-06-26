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
food_data_df = pd.DataFrame.from_dict(food_data)

row_num = len(food_data_df)
total_calories = 0
for i in range(row_num):
    total_calories = total_calories + food_data_df['calories'][i]




