import pandas as pd


Dev_file_path = 'Code\web_dev.csv'
DevImpact = pd.read_csv(Dev_file_path) 
DevImpact.describe()