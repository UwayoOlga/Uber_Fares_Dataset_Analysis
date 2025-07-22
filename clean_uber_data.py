import pandas as pd

df = pd.read_csv("uber_fares_dataset.csv")
 
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
 
df = df.dropna(subset=['dropoff_longitude', 'dropoff_latitude'])
 
df = df[df['fare_amount'] >= 0]
 
df = df[(df['passenger_count'] >= 1) & (df['passenger_count'] <= 6)]
 
df = df[df['pickup_latitude'].between(-90, 90) & df['dropoff_latitude'].between(-90, 90)]
df = df[df['pickup_longitude'].between(-180, 180) & df['dropoff_longitude'].between(-180, 180)]
 
print("Missing values after cleaning:\n", df.isnull().sum())
print("Duplicate rows after cleaning:", df.duplicated().sum())
 
df.to_csv("uber_fares_cleaned.csv", index=False)
print("Cleaned dataset saved as 'uber_fares_cleaned.csv'")
