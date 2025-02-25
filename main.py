#Importing Packages

import os
import pandas as pd 
import random
from datetime import datetime, timedelta

#Setting Excel File Directory
REPORT_DIRECTORY = "C:/Users/Andrew Petrulakis/Desktop/Reports/SEMAP/SEMAP 3 AND 10/DHA/2025/Jan/Jan_Activity.xlsx"

def random_sample(data: str, column: str, sample_size: int, sampled_data: str) -> str:
    """ Generate a random sample based on excel column criteria.
        - data: active dataframe being used for the sample
        - column: the desired column in excel to be used for sample critera.
        - sample_size: number of samples desired per object.
        - sampled_data: name of newly created dataframe
    """
    sampled_data = data.groupby(column).apply(lambda x: x.sample(n=min(len(x), sample_size),)).reset_index(drop=True)
    print(sampled_data)

#Reading in Excel File 
data_test = pd.read_excel(REPORT_DIRECTORY)
data_test.fillna('N/A', inplace=True)

# #Isolatiing Column that will be used for sampling 
# caseworkers = data_test["Caseworker58"]

# #Random Sampling Based On Caseworker (2 for each person):
# sampled_data = data_test.groupby("Caseworker58").apply(lambda x: x.sample(n=min(len(x), 2),)).reset_index(drop=True)

random_sample(data_test, "Caseworker58", 2, "sampled_test")
# #Random Sampling Testing
# for caseworker in CASEWORKERS:
#     for _ in range(NUM_SAMPLES):
#         sample_date = random_date(DATE_RANGE[0], DATE_RANGE[1])
#         print(f'{caseworker} {sample_date}')
