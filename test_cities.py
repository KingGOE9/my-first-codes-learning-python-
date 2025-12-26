import unittest
from city_functions import get_formatted_city_details

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""
    
    def test_city_country(self):
        """Test to see if city and country pair work"""
        formatted_location = get_formatted_city_details('santiago', 'chile')
        self.assertEqual(formatted_location, 'Santiago, Chile')

    def test_city_country_population(self):
        """Test to see if city, country and population work"""
        formatted_location = get_formatted_city_details('santiago', 'chile', 5000000)
        self.assertEqual(formatted_location, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()