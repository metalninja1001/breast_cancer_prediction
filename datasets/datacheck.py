import numpy as np
import pandas as pd
import argparse

# Create the argument parser
parser = argparse.ArgumentParser(prog='datacheck.py', description='Check dataset for any NaN values', epilog='Please ensure the file entered is a csv file', usage='%(prog)s [options]')
parser.add_argument('-f', '--file', type=str, help='Path to CSV file')

# Parse the arguments
args = parser.parse_args()

# Load breast cancer dataset
data = pd.read_csv(args.file)
df = pd.DataFrame(data)
print(data)