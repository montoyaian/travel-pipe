import unittest
from Classes.standart_client import Standardclient 

class TestStandardclient(unittest.TestCase):
    def setUp(self):
        self.client = Standardclient(1, "Jane Smith", 987654321, 3, "jane@example.com")

    def test_instance(self):
        self.assertIsInstance(self.client, Standardclient, "It's an instance of Standardclient")

    def test_id_property(self):
        self.assertEqual(self.client.id, 1, "id property matches")

    def test_id_property_setter(self):
        self.client.id = 2
        self.assertEqual(self.client.id, 2, "id property setter works")

    def test_name_property(self):
        self.assertEqual(self.client.name, "Jane Smith", "name property matches")

    def test_name_property_setter(self):
        self.client.name = "Alice Johnson"
        self.assertEqual(self.client.name, "Alice Johnson", "name property setter works")

    def test_contact_property(self):
        self.assertEqual(self.client.contact, 987654321, "contact property matches")

    def test_contact_property_setter(self):
        self.client.contact = 123456789
        self.assertEqual(self.client.contact, 123456789, "contact property setter works")

    def test_bookings_property(self):
        self.assertEqual(self.client.bookings, 3, "bookings property matches")

    def test_bookings_property_setter(self):
        self.client.bookings = 5
        self.assertEqual(self.client.bookings, 5, "bookings property setter works")

    def test_email_property(self):
        self.assertEqual(self.client.email, "jane@example.com", "email property matches")

    def test_email_property_setter(self):
        self.client.email = "alice@example.com"
        self.assertEqual(self.client.email, "alice@example.com", "email property setter works")

    def test__str__(self):
        expected_str = {
            "id": 1,
            "name": "Jane Smith",
            "contact": 987654321,
            "bookings": 3,
            "email": "jane@example.com"
        }
        self.assertEqual(self.client.__str__(), expected_str, "__str__ method matches")

if __name__ == '__main__':
    unittest.main()