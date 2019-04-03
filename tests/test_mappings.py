import unittest
from src.purchase_analytics import map_orders_to_products
from src.purchase_analytics import map_department_to_orders
from src.order import Order

class TestMapping(unittest.TestCase):

    def setUp(self):
        self.orders = [
            ("2", "33120", "1","1"),
            ("3", "17668", "1","1"),
            ("3", "46667", "2","1")
        ]

        self.products = [
            ("33120","Organic Egg Whites","86","16"),
            ("17668","Unsweetened Chocolate Almond Breeze Almond Milk","91","16"),
            ("46667","Organic Ginger Root","83","4")
        ]

        self.order_to_product = {
            "33120":[Order("2","1")],
            "17668":[Order("3","1")],
            "46667":[Order("3","1")]
        }

    def test_map_order_to_products(self):
        
        self.assertEqual(self.order_to_product.keys(),
            map_orders_to_products(self.orders).keys())

    def test_map_department_to_orders(self):
        dept_to_order = {
            "16":[Order("2","1"), Order("3","1")],
            "4":[Order("3","1")]
        }
        self.assertEqual(dept_to_order.keys(),
            map_department_to_orders(self.products, self.order_to_product)
        )

if __name__ == "__main__":
    unittest.main()