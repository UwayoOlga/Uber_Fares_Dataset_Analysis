import pandas as pd
import numpy as np

def haversine(lon1, lat1, lon2, lat2):
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  # Radius of earth in kilometers
    return c * r

df = pd.read_csv("uber_fares_dataset.csv")

df = df[
    df['pickup_latitude'].between(-90, 90) &
    df['pickup_longitude'].between(-180, 180) &
    df['dropoff_latitude'].between(-90, 90) &
    df['dropoff_longitude'].between(-180, 180)
]
 
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
 
df = df.dropna(subset=['dropoff_longitude', 'dropoff_latitude'])
 
df = df[df['fare_amount'] >= 0]
 
df = df[(df['passenger_count'] >= 1) & (df['passenger_count'] <= 6)]
 
df['distance_km'] = haversine(
    df['pickup_longitude'], df['pickup_latitude'],
    df['dropoff_longitude'], df['dropoff_latitude']
)
 
print("Missing values after cleaning:\n", df.isnull().sum())
print("Duplicate rows after cleaning:", df.duplicated().sum())
print(df[
    (df['pickup_latitude'] > 90) | (df['pickup_latitude'] < -90) |
    (df['pickup_longitude'] > 180) | (df['pickup_longitude'] < -180) |
    (df['dropoff_latitude'] > 90) | (df['dropoff_latitude'] < -90) |
    (df['dropoff_longitude'] > 180) | (df['dropoff_longitude'] < -180)
])
df.to_csv("uber_fares_cleaned.csv", index=False)
print("Cleaned dataset saved as 'uber_fares_cleaned.csv' with distance_km column.")
