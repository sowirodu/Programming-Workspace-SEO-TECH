# MealFit

This Python script retrieves nutrition data for a given food item from the API-Ninjas API. It will be used to help people who want to gain/maintain weight.

## Prerequisites

- Python 3
- requests library
- pandas library 
- sqlalchemy library 

## Getting Started

1. Clone the repository.

2. Install the required libraries.

3. Obtain an API key from API-Ninjas (https://api-ninjas.com/) and set it as an environment variable named `API_KEY`. (Security Reasons)

4. Run the script by executing the following command:
   ```
   python pair-programming.py
   ```

5. Enter the name of a food item when prompted to retrieve its nutrition data. Ex: Brisket

6. The script will make an API request to API-Ninjas, retrieve the data, and display it in the console. 

7. The data will also be saved into a SQLite database file named `food_data.db`.