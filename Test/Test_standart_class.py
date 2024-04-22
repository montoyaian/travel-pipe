import unittest
from Classes.standart_class import Standartclass
from datetime import date

class TestStandartclass(unittest.TestCase):
    def setUp(self):
        self.flight = Standartclass(1, "New York", "Los Angeles", date(2023, 10, 16), 100, 14, 1, 500)

    def test_instance(self):
        self.assertIsInstance(self.flight, Standartclass, "It's an instance of Standartclass")

    def test_standart_cost(self):
        self.assertEqual(self.flight.standart_cost, 500, "Standart cost matches")

    def test_standart_cost_setter(self):
        self.flight.standart_cost = 600
        self.assertEqual(self.flight.standart_cost, 600, "Standart cost setter works")

    def test__str__(self):
        expected_str = {
            "id": 1,
            "origin": "New York",
            "destination": "Los Angeles",
            "date": date(2023, 10, 16),
            "positions": 100,
            "hour": 14,
            "id_agency": 1,
            "standart_cost": 500
        }
        self.assertEqual(self.flight.__str__(), expected_str, "__str__ method matches")

if __name__ == '__main__':
    unittest.main()