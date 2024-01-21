import pandas as pd

# Use the full path to ensure the file can be found
pumpkins = pd.read_csv("./2-Regression/2-Data/pumpkins.csv")
pumpkins.head()

pumpkins.isnull().sum()