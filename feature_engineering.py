import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load your dataset (adjust the filename if needed)
df = pd.read_csv("uber_fares_cleaned.csv")

# Rename 'index' to 'ride_index' if it exists
if 'index' in df.columns:
    df = df.rename(columns={'index': 'ride_index'})

# Rename 'Unnamed: 0' to 'ride_index' if it exists (for safety)
if 'Unnamed: 0' in df.columns:
    df = df.rename(columns={'Unnamed: 0': 'ride_index'})

# Convert pickup_datetime to datetime format
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')

# Drop rows with invalid or missing datetime values
df = df.dropna(subset=['pickup_datetime'])

# Extract date and time features
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['year'] = df['pickup_datetime'].dt.year
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek  # Monday=0
df['day_name'] = df['pickup_datetime'].dt.day_name()

# Create Peak/Off-Peak time indicator
def is_peak(hour):
    return 'Peak' if (7 <= hour <= 9 or 16 <= hour <= 19) else 'Off-Peak'

df['peak_time'] = df['hour'].apply(is_peak)

# Encode categorical variables (optional)
label_encoder = LabelEncoder()
df['peak_time_encoded'] = label_encoder.fit_transform(df['peak_time'])
df['day_name_encoded'] = label_encoder.fit_transform(df['day_name'])

# Save the enhanced dataset to a new CSV
df.to_csv("uber_fares_enhanced.csv", index=False)

print("Feature engineering complete. Saved to 'uber_fares_enhanced.csv'")
