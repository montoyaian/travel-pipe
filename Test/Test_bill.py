import unittest
from Classes.bill import Bill  

class TestBill(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(1, 100, 12345, "Credit Card")

    def test_instance(self):
        self.assertIsInstance(self.bill, Bill, "It's an instance of Bill")

    def test_id_property(self):
        self.assertEqual(self.bill.id, 1, "id property matches")

    def test_id_property_setter(self):
        self.bill.id = 2
        self.assertEqual(self.bill.id, 2, "id property setter works")

    def test_total_price_property(self):
        self.assertEqual(self.bill.total_price, 100, "total_price property matches")

    def test_total_price_property_setter(self):
        self.bill.total_price = 200
        self.assertEqual(self.bill.total_price, 200, "total_price property setter works")

    def test_id_booking_property(self):
        self.assertEqual(self.bill.id_booking, 12345, "id_booking property matches")

    def test_id_booking_property_setter(self):
        self.bill.id_booking = 54321
        self.assertEqual(self.bill.id_booking, 54321, "id_booking property setter works")

    def test_payment_method_property(self):
        self.assertEqual(self.bill.payment_method, "Credit Card", "payment_method property matches")

    def test_payment_method_property_setter(self):
        self.bill.payment_method = "PayPal"
        self.assertEqual(self.bill.payment_method, "PayPal", "payment_method property setter works")

    def test__str__(self):
        expected_str = {
            "id": 1,
            "total_price": 100,
            "id_booking": 12345,
            "payment_method": "Credit Card"
        }
        self.assertEqual(self.bill.__str__(), expected_str, "__str__ method matches")

if __name__ == '__main__':
    unittest.main()