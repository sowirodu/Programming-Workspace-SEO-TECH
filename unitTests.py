import unittest
from mealFit import *

class TestFoodProject(unittest.TestCase):
    def test_retr_Food_valid_response(self):
        food_data = retr_Food('brisket')
        self.assertEqual(food_data, {'food_name': 'brisket', 'calories': 289.3})

    def test_retr_Food_invalid_response(self):
        food_data = retr_Food('Test Food')
        self.assertFalse(food_data)