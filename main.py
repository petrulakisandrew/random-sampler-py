#Importing Packages

import os
import pandas as pd 
import random
from datetime import datetime, timedelta
import subprocess
import time

# Run the GUI script first to collect the inputs
subprocess.run(["python", "C:/Users/Andrew Petrulakis/Development/random-sampler-py/Input_GUI.py"])

# After the GUI finishes, read the input values from the text file
input_file = "input_values.txt"


# Read input values from the text file
input_file = "input_values.txt"

try:
    with open(input_file, "r") as f:
        lines = f.readlines()
        if len(lines) < 3:
            raise ValueError("Input file does not contain enough values.")
        
        REPORT_DIRECTORY = lines[0].strip()  # File path (Previously hardcoded)
        column_name = lines[1].strip()  # Column name
        sample_size = int(lines[2].strip())
        sampled_data = lines[3].strip()  # The name for the output file


except FileNotFoundError:
    print(f"Error: The file {input_file} was not found.")
except ValueError as ve:
    print(f"Value error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    


#Setting Excel File Directory
#REPORT_DIRECTORY = "C:/Users/Andrew Petrulakis/Desktop/Reports/SEMAP/SEMAP 3 AND 10/DHA/2025/Jan/Jan_Activity.xlsx"

def random_sample(data: str, column: str, sample_size: int, sampled_data: str) -> str:
    """ Generate a random sample based on excel column criteria.
        - data: active dataframe being used for the sample
        - column: the desired column in excel to be used for sample critera.
        - sample_size: number of samples desired per object.
        - sampled_data: name of newly created dataframe
    """
    try:
        #Ensure the original data exists as a dataframe
        if data.empty:
            raise ValueError("The provided 'data' does not exist")
        
        # Ensure sample_size is a valid integer and greater than zero
        if not isinstance(sample_size, int) or sample_size <= 0:
            raise ValueError("sample_size must be a positive whole number.")
        
        #Ensure the naming convention of the new dataframe is a character string
        if not isinstance(sampled_data, str):
            raise ValueError("Sampled data frame name must be a character string")
        
        # Ensure the column exists in the DataFrame
        if column not in data.columns:
            raise ValueError(f"Column '{column}' not found in data.")
        
        #Proceed with sample
        sampled_data = data.groupby(column).apply(lambda x: x.sample(n=min(len(x), sample_size),)).reset_index(drop=True)
        print(sampled_data)
        return sampled_data
    
        
    
    #Display error message and terminates
    except ValueError as ve:
        print(f"Error: {ve}")
        return None


#Reading in Excel File 
data_test = pd.read_excel(REPORT_DIRECTORY)
data_test.fillna('N/A', inplace=True)

#Using definition to Sample Data
random_sample(data_test, column_name, 2, sampled_data)


