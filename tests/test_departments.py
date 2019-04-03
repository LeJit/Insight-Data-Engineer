import unittest
from src.department import Department
from src.order import Order


class TestDepartment(unittest.TestCase):

    def setUp(self):
        self.department_id = "10"
        self.orders = [
            Order("151", True),
            Order("249", False)
        ]
        self.department = Department(self.department_id, self.orders)

    def test_number_of_orders(self):
        self.assertEqual(2, self.department.number_of_orders)

    def test_number_of_first_orders(self):
        self.assertEqual(1, self.department.number_of_first_orders)

if __name__ == "__main__":
    unittest.main()