import csv
from typing import List
from department import Department


def read_file_streaming(filename:str):
    """
    Read_File_Streaming: Reads an input CSV file. This function skips
    the first row (headers) and returns a Generator that yields each
    remaining row in the CSV file.

        Params:
            filename:
        Return:
            Generator: generator object 
    """
    with open(filename, "r") as text_file:
        csv_file = csv.reader(text_file, delimiter=",", quotechar='"')
        next(csv_file)
        for line in csv_file:
            yield line
    text_file.close()


def write_results(results:List[Department], columns:List[str]):
    """
    Write_Results: Writes results to an output CSV file. This function
    takes in a list of Department objects and outputs the relevant metrics
    for each row.

        Params:
            results:

            columns:

        Return:
            None, but outputs a CSV to the output/ directory.
    """
    with open("output/results.csv", "w") as results_file:
        writer = csv.DictWriter(results_file, fieldnames=columns)
        writer.writeheader()
        for result in results:
            writer.writerow(result._asdictionary())
        

