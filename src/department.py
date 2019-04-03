from collections import defaultdict
from order import Order

class Department(object):

    def __init__(self, department_id, orders):
        self.department_id = department_id
        self.orders = orders

    def _validate_departmentid(self, department_id):
        pass


    @property
    def number_of_orders(self):
        """
        number_of_orders: Computes the number of orders for the department.
        """
        return len(self.orders)

    @property
    def number_of_first_orders(self):
        """
        number_of_first_orders: Computes the number of first orders 
            for the department. First orders are orders where the
            "reordered" property is False.
        """
        return len([order for order in self.orders if order.reordered == False])

    @property
    def percentage(self):
        """
        percentage: Function to compute the fraction of orders for a 
        department that are first orders. If there are no orders for the
        department, then the percentage is 0.
        """
        if self.number_of_orders == 0:
            return "0.00"
        else:
            return round(self.number_of_first_orders/self.number_of_orders, 2)

    def _asdictionary(self):
        """
        _asdictionary: Helper Function to output Department order metrics
        in a dictionary format. This function is to be used when writing
        out the key metrics to the output file.
        """
        return {
            "department_id": self.department_id,
            "number_of_orders": self.number_of_orders,
            "number_of_first_orders": self.number_of_first_orders,
            "percentage": "{:.2f}".format(self.percentage)
        }

    def __gt__(self, department_2):
        return self.department_id > department_2.department_id

    def __str__(self):
        return "{0},{1},{2},{3}".format(
            self.department_id,
            self.number_of_orders,
            self.number_of_first_orders,
            self.percentage
        )
    