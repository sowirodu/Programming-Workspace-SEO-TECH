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

def to_FoodDatabase(food_data):                       
        food_data_df = pd.DataFrame.from_dict(food_data)
        engine = db.create_engine('sqlite:///food_data.db')
        food_data_df.to_sql('food_table', con=engine, if_exists='replace', index=False)
        with engine.connect() as connection:
                query_result = connection.execute(db.text("SELECT * FROM food_table;")).fetchall()
                food_db = pd.DataFrame(query_result)
        return food_db

def main():
    user_Food = input("Enter a food name: ")
    food_data = retr_Food(user_Food)
    if food_data:
        food_db = to_FoodDatabase(food_data)
        print(food_db)

if __name__ == "__main__":
    main()