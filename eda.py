import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("uber_fares_cleaned.csv")

# A. DESCRIPTIVE STATISTICS
print("\n===== Descriptive Statistics =====")
print("Mean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nMode:\n", df.mode(numeric_only=True).iloc[0])
print("\nStandard Deviation:\n", df.std(numeric_only=True))
print("\nQuartiles:\n", df.select_dtypes(include='number').quantile([0.25, 0.5, 0.75]))

# Data Range
print("\n===== Data Ranges =====")
print("Min:\n", df.min(numeric_only=True))
print("Max:\n", df.max(numeric_only=True))

# B. OUTLIER DETECTION
# Using IQR for fare_amount
Q1 = df['fare_amount'].quantile(0.25)
Q3 = df['fare_amount'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['fare_amount'] < lower_bound) | (df['fare_amount'] > upper_bound)]
print(f"\nNumber of fare_amount outliers: {len(outliers)}")

# C. VISUALIZATIONS
sns.set(style="whitegrid")

# 1. Fare Amount Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['fare_amount'], bins=50, kde=True, color='skyblue')
plt.title("Fare Amount Distribution")
plt.xlabel("Fare Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 2. Fare Amount vs Distance
if 'distance_km' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='distance_km', y='fare_amount', data=df, alpha=0.5)
    plt.title("Fare Amount vs Distance")
    plt.xlabel("Distance (km)")
    plt.ylabel("Fare Amount")
    plt.tight_layout()
    plt.show()
else:
    print("[INFO] 'distance_km' column not found. Please add trip distance to the dataset to plot Fare Amount vs. Distance.")

# 3. Fare Amount vs Time of Day
if 'pickup_datetime' in df.columns:
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')
    df['hour'] = df['pickup_datetime'].dt.hour

    plt.figure(figsize=(8, 5))
    sns.boxplot(x='hour', y='fare_amount', data=df)
    plt.title("Fare Amount by Hour of Day")
    plt.xlabel("Hour of Day")
    plt.ylabel("Fare Amount")
    plt.tight_layout()
    plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 5. Fare Amount vs Passenger Count
if 'passenger_count' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='passenger_count', y='fare_amount', data=df)
    plt.title("Fare Amount by Passenger Count")
    plt.xlabel("Passenger Count")
    plt.ylabel("Fare Amount")
    plt.tight_layout()
    plt.show()

# 6. Distance vs Passenger Count
if 'passenger_count' in df.columns and 'distance_km' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='passenger_count', y='distance_km', data=df)
    plt.title("Distance by Passenger Count")
    plt.xlabel("Passenger Count")
    plt.ylabel("Distance (km)")
    plt.tight_layout()
    plt.show()

 
