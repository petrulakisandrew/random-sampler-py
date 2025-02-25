#Importing Packages

import os
import pandas as pd 
import random
from datetime import datetime, timedelta

#Setting Excel File Directory
REPORT_DIRECTORY = "C:/Users/Andrew Petrulakis/Desktop/Reports/SEMAP/SEMAP 3 AND 10/DHA/2025/Jan/Jan_Activity.xlsx"

CASEWORKERS = ['Candice', 'Morgan', 'Ozury', 'Nida', 'Scott']
DATE_RANGE = ('01-01-2024', '12-31-2024')
NUM_SAMPLES = 2

def random_date(start_date: str, end_date: str, date_format: str = "%m-%d-%Y") -> str:
    """ Generate a random date between two given dates.
        - start_date: The start date of the range.
        - end_date: The end date of the range.
        - date_format: The format of the input and output dates.
    """
    try:
        start = datetime.strptime(start_date, date_format)
        end = datetime.strptime(end_date, date_format)
        
    except ValueError as e:
        raise ValueError(f"Incorrect date format, should be {date_format}") from e

    if start > end:
        raise ValueError("start_date must be earlier than end_date")

    random_date = start + timedelta(days=random.randint(0, (end - start).days))
    return random_date.strftime(date_format)

#Reading in Excel File 
data = pd.read_excel(REPORT_DIRECTORY)
data.fillna('N/A', inplace=True)

#Random Sampling Testing
for caseworker in CASEWORKERS:
    for _ in range(NUM_SAMPLES):
        sample_date = random_date(DATE_RANGE[0], DATE_RANGE[1])
        print(f'{caseworker} {sample_date}')
