from src.utils import read_file_streaming, write_results
from src.order import Order
from src.department import Department
import os
import logging

from typing import List, DefaultDict
from collections import defaultdict
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--product", required=True,
                help="Name of Products file")
parser.add_argument("-o", "--orders", required=True,
                help="Name of Orders file")
parser.add_argument("-r", "--results", required=True,
                help="Name of output result file")
args = vars(parser.parse_args())

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def map_orders_to_products(orders) -> DefaultDict[str, List]:
    """
    map_orders_to_products: This function reads in records pertaining
        to Instacart orders and aggregates orders based on the purchased product.

        Params:
            Orders: Generator object pointing to an input "orders" CSV file.
        Returns:
            Dictionary object mapping Product ID to a List of Orders that
                purchased the product.
    """
    prod_order_map = defaultdict(list)
    for order in orders:
        order_id, prod_id, add_to_cart, reorder = order
        prod_order_map[prod_id].append(Order(order_id, reorder))
    return prod_order_map


def map_department_to_orders(products, prod_order_map) -> DefaultDict[str, List]:
    """
    map_department_to_orders: This function reads in product information and matches
        department information to the Instacart orders.

        Params:
            Products: A Generator pointing to the Products CSV file where
                each row contains product information.
            Prod_Order_Map: Dictionary mapping a product ID to an Order.
            
        Returns:
            Dictionary object mapping Department ID (str) to a List of Orders that
                correspond to purchases in that department.
    """
    dept_product_map = defaultdict(list)
    for prod in products:
        prod_id, prod_name, aisle, dept = prod
        dept_product_map[dept].extend(
            prod_order_map[prod_id]
            )
    return dept_product_map

def create_departments(dept_product_map:DefaultDict[str, List]) -> List[Department]:
    """
    create_departments: Function to create a list of Departments for computing
        the resultant metrics.

        Params:
            Dept_Product_Map: Dictionary mapping Department IDs to a list of
                Orders pertaining to purchases of products located 
                in that department.
        Returns:
            A List of Department objects that compute the necessary metrics.
    """
    list_of_departments = [
        Department(
                    int(dept_id), 
                    orders
                    )
        for (dept_id, orders) in dept_product_map.items()
    ]
    return list_of_departments

def main():
    logger.info("Ingesting CSVs files")
    products = read_file_streaming(args["product"])
    orders = read_file_streaming(args["orders"])
   
    prod_order_map = map_orders_to_products(orders)
    dept_product_map = map_department_to_orders(products, prod_order_map)
    list_of_departments = create_departments(dept_product_map)

    logger.info("Writing results to output CSV file")
    headers = [
                "department_id",
                "number_of_orders",
                "number_of_first_orders",
                "percentage"
            ]
    list_of_departments = sorted(list_of_departments)
    write_results(args["results"], list_of_departments, headers)
    logger.info("Process has completed")
    
if __name__ == "__main__":
    main()
    