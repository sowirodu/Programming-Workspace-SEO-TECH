import unittest
from mealFit import *


class TestFoodProject(unittest.TestCase):

    def test_retr_Food_invalid_response(self):
        food_data = retr_Food('Test Food')
        self.assertFalse(food_data)

    def test_retr_Food_valid_response(self):
        food_data = retr_Food('brisket')
        self.assertTrue(food_data)

    def test_calories_per_hour_invalid_response(self):
        cal_per_hour = calories_per_hour('unknown_activity')
        self.assertFalse(cal_per_hour)
