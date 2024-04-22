import unittest
from Classes.flight import Flight  
from datetime import date

class TestFlight(unittest.TestCase):
    def setUp(self):
        self.flight = Flight(1, "New York", "Los Angeles", date(2023, 10, 16), 100, 14.5, 1)

    def test_instance(self):
        self.assertIsInstance(self.flight, Flight, "It's an instance of Flight")

    def test_id_property(self):
        self.assertEqual(self.flight.id, 1, "id property matches")

    def test_id_property_setter(self):
        self.flight.id = 2
        self.assertEqual(self.flight.id, 2, "id property setter works")

    def test_origin_property(self):
        self.assertEqual(self.flight.origin, "New York", "origin property matches")

    def test_origin_property_setter(self):
        self.flight.origin = "Los Angeles"
        self.assertEqual(self.flight.origin, "Los Angeles", "origin property setter works")

    def test_destination_property(self):
        self.assertEqual(self.flight.destination, "Los Angeles", "destination property matches")

    def test_destination_property_setter(self):
        self.flight.destination = "Chicago"
        self.assertEqual(self.flight.destination, "Chicago", "destination property setter works")

    def test_date_property(self):
        self.assertEqual(self.flight.date, date(2023, 10, 16), "date property matches")

    def test_date_property_setter(self):
        new_date = date(2023, 11, 1)
        self.flight.date = new_date
        self.assertEqual(self.flight.date, new_date, "date property setter works")

    def test_positions_property(self):
        self.assertEqual(self.flight.positions, 100, "positions property matches")

    def test_positions_property_setter(self):
        self.flight.positions = 200
        self.assertEqual(self.flight.positions, 200, "positions property setter works")

    def test_hour_property(self):
        self.assertEqual(self.flight.hour, 14.5, "hour property matches")

    def test_hour_property_setter(self):
        self.flight.hour = 15.5
        self.assertEqual(self.flight.hour, 15.5, "hour property setter works")

    def test_id_agency_property(self):
        self.assertEqual(self.flight.id_agency, 1, "id_agency property matches")

    def test_id_agency_property_setter(self):
        self.flight.id_agency = 2
        self.assertEqual(self.flight.id_agency, 2, "id_agency property setter works")

    def test__str__(self):
        expected_str = {
            "id": 1,
            "origin": "New York",
            "destination": "Los Angeles",
            "date": date(2023, 10, 16),
            "positions": 100,
            "hour": 14.5,
            "id_agency": 1
        }
        self.assertEqual(self.flight.__str__(), expected_str, "__str__ method matches")

if __name__ == '__main__':
    unittest.main()
