#Loading data
import pandas as pd
df = pd.read_csv("uber_fares_dataset.csv") 
df.head()
# Understanding the data (EDA)
print("Shape:", df.shape)
df.info()
print(df.describe())
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
