import unittest
from Classes.booking import Booking 

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.booking = Booking(1, 2, 3, 4, "standart client", "standart class", 250)

    def test_instance(self):
        self.assertIsInstance(self.booking, Booking, "It's an instance of Booking")

    def test_id_property(self):
        self.assertEqual(self.booking.id, 1, "id property matches")

    def test_id_property_setter(self):
        self.booking.id = 2
        self.assertEqual(self.booking.id, 2, "id property setter works")

    def test_cant_positions_property(self):
        self.assertEqual(self.booking.cant_positions, 2, "cant_positions property matches")

    def test_cant_positions_property_setter(self):
        self.booking.cant_positions = 3
        self.assertEqual(self.booking.cant_positions, 3, "cant_positions property setter works")

    def test_id_flight_property(self):
        self.assertEqual(self.booking.id_flight, 3, "id_flight property matches")

    def test_id_flight_property_setter(self):
        self.booking.id_flight = 4
        self.assertEqual(self.booking.id_flight, 4, "id_flight property setter works")

    def test_id_client_property(self):
        self.assertEqual(self.booking.id_client, 4, "id_client property matches")

    def test_id_client_property_setter(self):
        self.booking.id_client = 5
        self.assertEqual(self.booking.id_client, 5, "id_client property setter works")

    def test_type_flight_property(self):
        self.assertEqual(self.booking.type_flight, "standart class", "type_flight property matches")

    def test_type_flight_property_setter(self):
        self.booking.type_flight= "Business"  
        self.assertEqual(self.booking.type_flight, "Business", "type_flight property setter works")

    def test_type_client_property(self):
        self.assertEqual(self.booking.type_client, "standart client", "type_client property matches")

    def test_type_client_property_setter(self):
        self.booking.type_client = "VIP"
        self.assertEqual(self.booking.type_client, "VIP", "type_client property setter works")

    def test_cost_position_property(self):
        self.assertEqual(self.booking.cost_position, 200.0, "cost_position property matches")

    def test_cost_position_property_setter(self):
        self.booking.cost_position = 250
        self.assertEqual(self.booking.cost_position, 250, "cost_position property setter works")

    def test__str__(self):
        expected_str = {
            "id": 1,
            "cant_positions": 2,
            "id_flight": 3,
            "id_client": 4,
            "type_flight": "standart class",
            "type_client": "standart client",
            "cost_position": 200.0
        }
        self.assertEqual(self.booking.__str__(), expected_str, "__str__ method matches")

if __name__ == '__main__':
    unittest.main()