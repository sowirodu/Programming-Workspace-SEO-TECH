import requests as rq
import pandas as pd
import os
import sqlalchemy as db


def retr_Food(user_Food):
    ninja_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(user_Food)
    response = rq.get(ninja_url, headers={'X-Api-Key': os.environ.get('API_KEY')})
    if response.status_code == 200:
        food_data = response.json()
        return food_data
    else:
        print("Error:", response.status_code, response.text)
        return False


def calories_per_hour(activity):
    cal_url = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'.format(activity)
    cal_response = rq.get(cal_url, headers={'X-Api-Key': os.environ.get('API_KEY')})
    if cal_response.status_code == 200:
        activity_data = cal_response.json()
        if activity_data:
            activity_df = pd.DataFrame.from_dict(activity_data)
            cal_per_hour = activity_df['total_calories'][0]
            return cal_per_hour
        else:
            return False
    else:
        return False


def to_FoodDatabase(food_data):
    food_data_df = pd.DataFrame.from_dict(food_data)
    engine = db.create_engine('sqlite:///food_data.db')
    food_data_df.to_sql('food_table', con=engine, if_exists='append', index=False)
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM food_table;")).fetchall()
        food_db = pd.DataFrame(query_result)
    return food_db


def query_FoodDatabase():
    engine = db.create_engine('sqlite:///food_data.db')
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM food_table ORDER BY calories DESC;")).fetchall()
        food_db = pd.DataFrame(query_result)
    return food_db


def main():
    while True:
        user_input = input("Enter a food name (type 'log' to exit): ")

        if user_input.lower() == "log":
            print(query_FoodDatabase())
            break

        user_Food = user_input
        user_activity = input("Enter desired activity: ")
        cals_per_hour = calories_per_hour(user_activity)
        food_data = retr_Food(user_Food)

        if food_data and cals_per_hour:
            food_db = to_FoodDatabase(food_data)
            cal_col = food_db['calories']
            total_cals = cal_col.sum()
            hours = int(total_cals / cals_per_hour)
            print("Total hours needed to burn calories:", hours)


if __name__ == "__main__":
    main()
