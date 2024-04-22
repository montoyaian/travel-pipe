import unittest
from Classes.offers import Offer  # Asegúrate de importar la clase Offer desde tu módulo

class TestOffer(unittest.TestCase):
    def setUp(self):
        self.offer = Offer(1, 2, 10, "standart client", "standart class")

    def test_instance(self):
        self.assertIsInstance(self.offer, Offer, "It's an instance of Offer")

    def test_id_property(self):
        self.assertEqual(self.offer.id, 1, "id property matches")

    def test_id_property_setter(self):
        self.offer.id = 2
        self.assertEqual(self.offer.id, 2, "id property setter works")

    def test_id_flight_property(self):
        self.assertEqual(self.offer.id_flight, 2, "id_flight property matches")

    def test_id_flight_property_setter(self):
        self.offer.id_flight = 3
        self.assertEqual(self.offer.id_flight, 3, "id_flight property setter works")

    def test_discount_property(self):
        self.assertEqual(self.offer.discount, 10, "discount property matches")

    def test_discount_property_setter(self):
        self.offer.discount = 20
        self.assertEqual(self.offer.discount, 20, "discount property setter works")

    def test_customer_type_property(self):
        self.assertEqual(self.offer.customer_type, "standart client", "customer_type property matches")

    def test_customer_type_property_setter(self):
        self.offer.customer_type = "VIP"
        self.assertEqual(self.offer.customer_type, "VIP", "customer_type property setter works")

    def test_flight_type_property(self):
        self.assertEqual(self.offer.flight_type, "standart class", "flight_type property matches")

    def test_flight_type_property_setter(self):
        self.offer.flight_type = "Business"
        self.assertEqual(self.offer.flight_type, "Business", "flight_type property setter works")

    def test__str__(self):
        expected_str = {
            "id": 1,
            "id_flight": 2,
            "discount": 10,
            "customer_type": "standart client",
            "flight_type": "standart class"
        }
        self.assertEqual(self.offer.__str__(), expected_str, "__str__ method matches")

if __name__ == '__main__':
    unittest.main()