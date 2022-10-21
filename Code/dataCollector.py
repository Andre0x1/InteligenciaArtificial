import pandas as pd


Dev_file_path = '..input/devImpactDataSet.csv'
# read the data and store data in DataFrame titled melbourne_data
DevImpact = pd.read_csv(Dev_file_path) 
# print a summary of the data in Melbourne data
DevImpact.describe()