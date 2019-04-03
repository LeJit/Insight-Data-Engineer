import csv
from typing import List
from src.department import Department
import os

INPUT_DIR = "{0}/input".format(os.getcwd())
OUTPUT_DIR = "{0}/output".format(os.getcwd())


def read_file_streaming(filename:str):
    """
    Read_File_Streaming: Reads an input CSV file. This function skips
    the first row (headers) and returns a Generator that yields each
    remaining row in the CSV file.

        Params:
            filename: Name of input CSV file.
        Return:
            Generator: generator object 
    """
    with open("{0}/{1}".format(INPUT_DIR, filename), "r") as text_file:
        csv_file = csv.reader(text_file, delimiter=",", quotechar='"')
        next(csv_file)
        for line in csv_file:
            yield line
    text_file.close()


def write_results(filename:str, results:List[Department], columns:List[str]):
    """
    Write_Results: Writes results to an output CSV file. This function
    takes in a list of Department objects and outputs the relevant metrics
    for each row.

        Params:
            filename: Name of the output CSV File.
            results: List of Departments found in the orders.
            columns: Column headers for the output CSV file.
        Return:
            None, but outputs a CSV to the output/ directory.
    """
    with open("{0}/{1}".format(OUTPUT_DIR, filename), "w") as results_file:
        writer = csv.DictWriter(results_file, fieldnames=columns)
        writer.writeheader()
        for result in results:
            writer.writerow(result._asdictionary())
        

