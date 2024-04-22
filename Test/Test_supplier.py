import unittest
from Classes.supplier import Supplier 

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier(1, "ABC Suppliers", 987654321, "Supplier of various products")

    def test_instance(self):
        self.assertIsInstance(self.supplier, Supplier, "It's an instance of Supplier")

    def test_id_property(self):
        self.assertEqual(self.supplier.id, 1, "id property matches")

    def test_id_property_setter(self):
        self.supplier.id = 2
        self.assertEqual(self.supplier.id, 2, "id property setter works")

    def test_name_property(self):
        self.assertEqual(self.supplier.name, "ABC Suppliers", "name property matches")

    def test_name_property_setter(self):
        self.supplier.name = "XYZ Corporation"
        self.assertEqual(self.supplier.name, "XYZ Corporation", "name property setter works")

    def test_contact_property(self):
        self.assertEqual(self.supplier.contact, 987654321, "contact property matches")

    def test_contact_property_setter(self):
        self.supplier.contact = 123456789
        self.assertEqual(self.supplier.contact, 123456789, "contact property setter works")

    def test_description_property(self):
        self.assertEqual(self.supplier.description, "Supplier of various products", "description property matches")

    def test_description_property_setter(self):
        self.supplier.description = "Provider of quality goods"
        self.assertEqual(self.supplier.description, "Provider of quality goods", "description property setter works")

    def test__str__(self):
        expected_str = {
            "id": 1,
            "name": "ABC Suppliers",
            "contact": 987654321,
            "description": "Supplier of various products"
        }
        self.assertEqual(self.supplier.__str__(), expected_str, "__str__ method matches")

if __name__ == '__main__':
    unittest.main()