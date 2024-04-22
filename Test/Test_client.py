import unittest
from Classes.client import Client  

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client(1, "ian", 123456789, 5, "ian@hotmail.com")

    def test_instance(self):
        self.assertIsInstance(self.client, Client, "It's an instance of Client")

    def test_id_property(self):
        self.assertEqual(self.client.id, 1, "id property matches")

    def test_id_property_setter(self):
        self.client.id = 2
        self.assertEqual(self.client.id, 2, "id property setter works")

    def test_name_property(self):
        self.assertEqual(self.client.name, "ian", "name property matches")

    def test_name_property_setter(self):
        self.client.name = "Jane Smith"
        self.assertEqual(self.client.name, "Jane Smith", "name property setter works")

    def test_contact_property(self):
        self.assertEqual(self.client.contact, 123456789, "contact property matches")

    def test_contact_property_setter(self):
        self.client.contact = 987654321
        self.assertEqual(self.client.contact, 987654321, "contact property setter works")

    def test_bookings_property(self):
        self.assertEqual(self.client.bookings, 5, "bookings property matches")

    def test_bookings_property_setter(self):
        self.client.bookings = 10
        self.assertEqual(self.client.bookings, 10, "bookings property setter works")

    def test_email_property(self):
        self.assertEqual(self.client.email, "ian@hotmail.com", "email property matches")

    def test_email_property_setter(self):
        self.client.email = "jane@example.com"
        self.assertEqual(self.client.email, "jane@example.com", "email property setter works")

    def test__str__(self):
        expected_str = {
            "id": 1,
            "name": "ian",
            "contact": 123456789,
            "bookings": 5,
            "email": "ian@hotmail.com"
        }
        self.assertEqual(self.client.__str__(), expected_str, "__str__ method matches")

if __name__ == '__main__':
    unittest.main()