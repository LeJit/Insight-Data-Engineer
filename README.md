# Insight-Data-Engineer
Private repo for Manojit Nandi's submission to the Insight Data Engineer fellowship coding challenge.

## Methodology

### File Streaming

In `src/utils.py`, I created two methods: `read_file_streaming` and `write_results`.

I chose to read the input CSV files in a streaming fashion due the large filesize of some of the potential input files, such as `order_products__prior.csv`. Loading the contents of this file entirely into memory would be CPU-intensive and wasteful for a file that will be processed only once.

### Purchase_Analytics

In the main script, my logic for computing the required metrics is as follows.

1. Read in `order_product.csv` (or other input Orders CSV file) and for each row, map the `product_id` to a List of Order objects that holds the `order_id` and `reordered` field for the order. This creates a dictionary mapping a `product_id` to all the orders that purchased that product.

2. Read in `products_small.csv` (or other input Product CSV file) and for each row, extract the `department_id` and the `product_id`. Using the dictionary mapping `product_id` to List of Orders from the previous step, I map each `department_id` to the List of Orders associated with each product in the department. This creates a dictionary mapping a `department_id` to all orders that purchase a product located in that department.

3. In the final step, I create a `Department` object that takes in the `department_id` and the List of Orders associated with that department. The `Department` class computes the three metrics: `number_of_orders`, `number_of_first_orders`, and `percentage`.

## Run Instructions

The main script is `src/purchase_analytics.py`. This script requires three command-line argument parameters.

1. `-p`: The name of the products CSV file, located in the `input/` directory.

2. `-o`: The name of the orders CSV file, located in the `input/` directory.

3. `-r`: The name of the results CSV file to write the output metrics. Will be created in the `output/` directory.

An example run of this script would be as follows:

`python3 scr/purchase_analytics.py -p "products.csv" -o "order_products.csv" -r "results.csv"`