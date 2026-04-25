import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =========================
# Load Dataset
# =========================
df = pd.read_csv("CSV Files/fast_food_resturants.csv")

print("Raw Data:")
print(df.head())

# =========================
# Basic Inspection
# =========================
print("\nData Types:")
print(df.dtypes)

print("\nInfo:")
df.info()

print("\nShape:", df.shape)

# =========================
# Data Cleaning
# =========================

# Check null values
print("\nMissing Values:")
print(df.isna().sum())

# Drop unnecessary columns (keys, websites)
df.drop(columns=['keys', 'websites'], inplace=True, errors='ignore')

# Fill missing values (if any)
df['province'].fillna(df['province'].mode()[0], inplace=True)
df['city'].fillna(df['city'].mode()[0], inplace=True)

# =========================
# EDA Report
# =========================
print('\n=====EDA Report======\n')
print(df.describe())

# =========================
# Categorical Analysis
# =========================

print("\n===== TOP RESTAURANT CHAINS =====")
print(df['name'].value_counts().head(10))

print("\n===== TOP CITIES =====")
print(df['city'].value_counts().head(10))

print("\n===== TOP PROVINCES =====")
print(df['province'].value_counts().head(10))

# =========================
# Group Analysis
# =========================

# Restaurants per city
city_group = df.groupby('city')['name'].count().sort_values(ascending=False)
print("\n===== RESTAURANTS PER CITY =====")
print(city_group.head(10))

# Restaurants per province
province_group = df.groupby('province')['name'].count().sort_values(ascending=False)
print("\n===== RESTAURANTS PER PROVINCE =====")
print(province_group.head(10))

# =========================
# Geographic Insights
# =========================

print("\n===== LAT/LONG SUMMARY =====")
print(df[['latitude', 'longitude']].describe())

# Find extreme locations
print("\n===== EXTREME LOCATIONS =====")
print("Max Latitude:\n", df.loc[df['latitude'].idxmax()])
print("\nMin Latitude:\n", df.loc[df['latitude'].idxmin()])

# =========================
# Brand Distribution
# =========================

brand_counts = df['name'].value_counts()

print("\n===== BRAND DISTRIBUTION =====")
print(brand_counts.describe())

# Brands with only 1 outlet
single_outlets = brand_counts[brand_counts == 1]
print("\nBrands with single outlet:", len(single_outlets))

# =========================
# Country Analysis
# =========================

print("\n===== COUNTRY DISTRIBUTION =====")
print(df['country'].value_counts())

# =========================
# Final Summary
# =========================
print("\n===== FINAL SUMMARY =====")
print(f"Total Restaurants: {len(df)}")
print(f"Unique Brands: {df['name'].nunique()}")
print(f"Unique Cities: {df['city'].nunique()}")
print(f"Unique Provinces: {df['province'].nunique()}")



# =========================
# Seaborn Visualizations
# =========================

sns.set_theme(style="darkgrid")

# =========================
# 1. Top Restaurant Brands
# =========================
top_brands = df['name'].value_counts().head(10)

sns.barplot(x=top_brands.values, y=top_brands.index)
plt.title("Top 10 Fast Food Chains")
plt.xlabel("Count")
plt.ylabel("Brand")
plt.show()


# =========================
# 2. Restaurants by Province
# =========================
sns.countplot(data=df, x='province')
plt.title("Number of Restaurants per Province")
plt.xticks(rotation=45)
plt.show()


# =========================
# 3. Restaurants by City (Top 10)
# =========================
top_cities = df['city'].value_counts().head(10)

sns.barplot(x=top_cities.values, y=top_cities.index)
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("Count")
plt.ylabel("City")
plt.show()


# =========================
# 4. Geographic Scatter Plot
# =========================
sns.scatterplot(data=df, x='longitude', y='latitude', hue='province')
plt.title("Restaurant Locations (Geo Scatter)")
plt.show()


# =========================
# 5. Distribution of Latitude
# =========================
sns.histplot(data=df, x='latitude', bins=30)
plt.title("Latitude Distribution")
plt.show()


# =========================
# 6. KDE Plot (Density of Longitude)
# =========================
sns.kdeplot(data=df, x='longitude', fill=True)
plt.title("Longitude Density")
plt.show()


# =========================
# 7. Heatmap (Correlation)
# =========================
corr = df[['latitude', 'longitude']].corr()

sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()


# =========================
# 8. Pairplot (Location relationship)
# =========================
sns.pairplot(df[['latitude', 'longitude']])
plt.show()


# =========================
# Final Output
# =========================
print("\nAnalysis Completed Successfully")