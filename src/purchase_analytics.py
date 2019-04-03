from utils import read_file_streaming, write_results
from order import Order
from department import Department
import os
import logging

from typing import List, DefaultDict
from collections import defaultdict
import argparse


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
##
## Order <--> Product ID <--> DeparmentID
##


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
            Products:

            Prod_Order_Map:

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

def create_departments(dept_product_map) -> List[Department]:
    """
    create_departments:


        Params:
            Dept_Product_Map
        Returns:
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
    products = read_file_streaming("{0}/input/products_small.csv".format(os.getcwd()))
    orders = read_file_streaming("{0}/input/order_products.csv".format(os.getcwd()))
   
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
    write_results(list_of_departments, headers)
    logger.info("Process has completed")
    
if __name__ == "__main__":
    main()