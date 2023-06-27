import requests as rq
import pandas as pd
import os
import sqlalchemy as db

def hours_needed(food_name):
        ninja_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(food_name)
        response = rq.get(ninja_url, headers={'X-Api-Key': os.environ.get('API_KEY')})
        if response.status_code == rq.codes.ok:
                print(response.text)
        else:
            print("Error:", response.status_code, response.text)

        food_data = response.json()
        food_data_df = pd.DataFrame.from_dict(food_data)
        engine = db.create_engine('sqlite:///food_data.db')
        food_data_df.to_sql('food_table', con=engine, if_exists='replace', index=False)
        with engine.connect() as connection:
                result = connection.execute(db.text("SELECT * FROM food_table;")).fetchall()
                food_db = pd.DataFrame(result)
                print(food_db)

#tesing
hours_needed('brisket')