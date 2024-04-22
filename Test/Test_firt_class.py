import unittest
from Classes.first_class import Firtsclass 
from datetime import date

class TestFirtsclass(unittest.TestCase):
    def setUp(self):
        self.flight = Firtsclass(1, "New York", "Los Angeles", date(2023, 10, 16), 100, 14, 1, 1000)

    def test_instance(self):
        self.assertIsInstance(self.flight, Firtsclass, "It's an instance of Firtsclass")

    def test_premium_cost_property(self):
        self.assertEqual(self.flight.premium_cost, 1000, "Premium cost property matches")

    def test_premium_cost_property_setter(self):
        self.flight.premium_cost = 1200
        self.assertEqual(self.flight.premium_cost, 1200, "Premium cost property setter works")

    def test__str__(self):
        expected_str = {
            "id": 1,
            "origin": "New York",
            "destination": "Los Angeles",
            "date": date(2023, 10, 16),
            "positions": 100,
            "hour": 14,
            "id_agency": 1,
            "premium_cost": 1000  
        }
        self.assertEqual(self.flight.__str__(), expected_str, "__str__ method matches")

if __name__ == '__main__':
    unittest.main()


