import requests as rq
import pandas as pd
import os
import sqlalchemy as db



#finds the total calories in the food
def total_calories(food_name):
        ninja_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(food_name)
        response = rq.get(ninja_url, headers={'X-Api-Key': os.environ.get('API_KEY')})
        if response.status_code == rq.codes.ok:
                print(response.text)
        else:
                print("Error:", response.status_code, response.text)

        food_data = response.json()
        food_data_df = pd.DataFrame.from_dict(food_data)
        calories = 0

        for x in range(len(food_data_df)):
                calories += food_data_df['calories'][x]

        return calories


#calculates how many calories are burned in an hour of this activity      
def calories_per_hour(activity, weight):
        calories_url = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'.format(activity)
        response = rq.get(calories_url, headers={'X-Api-Key': os.environ.get('API_KEY')})
        if response.status_code == rq.codes.ok:
                print(response.text)
        else:
                print("Error:", response.status_code, response.text)
        calories_data = response.json()
        calories_df = pd.DataFrame.from_dict(calories_data)
        cal_per_hour = calories_df['calories_per_hour'][0]

        return cal_per_hour

#updates and displays the database with the food eaten
def update_database(food_name):
        return

#returns the hours to spend on the activity
def hours_to_spend(food_name, activity, weight = 160):
        total_cal = total_calories(food_name)
        cal_p_h = calories_per_hour(activity, weight)
        hours = int(total_cal / cal_p_h)
        return hours

#tesing