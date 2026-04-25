import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# =========================
# Load Dataset
# =========================
# Read CSV file

df = pd.read_csv("CSV Files/real_estate_data_2.csv")

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

# =========================
# Check null values
# =========================
print(df.isna().sum())

# =========================
# Drop null values
# =========================
df.drop(columns=['Non Use Code', 'Assessor Remarks', 'OPM remarks', 'Location' ],inplace=True)
print(df.columns) # valide removal

# =========================
# Fill null values
# =========================
df['Residential Type'] = df['Residential Type'].fillna(df['Residential Type'].mode()[0])
print (df.isna().sum()) # valide fillna

# =========================
# Convert column to date time.
# =========================
df['Date Recorded'] = pd.to_datetime(df['Date Recorded'],errors='coerce')

# =========================
df.rename(columns={
    'Serial Number':'serial_number',
    'List Year':'list_year',
    'Date Recorded':'date_recorded',
    'Assessed Value':'assess_value',
    'Sale Amount':'sale_amount',
    'Sales Ratio':'sales_ratio',
    'Property Type':'property_type',
    'Residential Type':'residential_type'
}, inplace=True)

# =========================
# Basic Analysis
# =========================
state1 = df.groupby('property_type')['sale_amount'].agg(['mean','median'])
print("\nMean ad Median of Sales_Amount:\n")
print(state1)


state2 = df.groupby('property_type')[['sale_amount','assess_value','sales_ratio']].agg(['mean','median'])
print("\nMean and Median of sale_amount, assess_value & sales_ratio:\n")
print(state2)

# =========================
# EDA Report
# =========================
print('\n=====EDA Report======\n')
cols = ['assess_value','sale_amount','sales_ratio']
for col in cols:
    mean_value = df[col].mean()
    median_value = df[col].median()
    std_value = df[col].std()
    skewness = df[col].skew()
    diff = mean_value - median_value
    count = df[col].value_counts()
    sample = abs(count.max()-count.min())
    Spread = df[col].std()/df[col].mean()*100

    print(f'{col.replace("_"," ").title()}:')
    print(f'mean_value: {mean_value:.2f}')
    print(f'median_value: {median_value:.2f}')
    print(f'std_value: {std_value:.2f}')

    # Outlier
    if diff < 2:
        print(f'As Difference is {diff:.2f} So, No Outlier Exist.')
    else:
        print(f'As Difference is {diff:.2f} So, Outlier Exist.')

    # Skewness
    if skewness < -0.5:
        print(f'As Skew Value is {skewness:.2f}, so Data is Left Skewed / Tilted Towards Left Side')
    elif skewness < 0.5:
        print(f'As Skew Value is {skewness:.2f}, so Data is Symmetric')
    else:
        print(f'As Skew Value is {skewness:.2f}, so Data is Right Skewed / Tilted Towards Right Side')

    # Sample Balanced
    if sample < 5:
        print(f'As Sample Result is {sample}, so Sample is Balanced')
    else:
        print(f'As Sample Result is {sample}, so Sample is Unbalanced')

    # Spreadness
    if Spread < 10:
        print(f'As Spread is {Spread:.2f}%, so Data is Tight Spread.')
    elif Spread < 20:
        print(f'As Spread is {Spread:.2f}%, so Data is Moderate Spread.')
    else:
        print(f'As Spread is {Spread:.2f}%, so Data is Wide Spreade')
    print('\n')


# =========================
# Seaborn Visualizations
# =========================

sns.set_theme(style="darkgrid")

# =========================
# 1. Distribution of Sale Amount
# =========================
sns.histplot(data=df, x='sale_amount', bins=30)
plt.title("Distribution of Sale Amount")
plt.show()


# =========================
# 2. KDE Plot (Smooth Distribution)
# =========================
sns.kdeplot(data=df, x='sale_amount', fill=True)
plt.title("KDE of Sale Amount")
plt.show()


# =========================
# 3. Sale Amount vs Assessed Value
# =========================
sns.scatterplot(data=df, x='assess_value', y='sale_amount', hue='property_type')
plt.title("Sale Amount vs Assessed Value")
plt.show()


# =========================
# 4. Trend Over Time
# =========================
sns.lineplot(
    data=df.sort_values('date_recorded'),
    x='date_recorded',
    y='sale_amount'
)
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)
plt.show()


# =========================
# 5. Average Sale Amount by Property Type
# =========================
sns.barplot(data=df, x='property_type', y='sale_amount')
plt.title("Average Sale Amount by Property Type")
plt.xticks(rotation=45)
plt.show()


# =========================
# 6. Residential Type vs Sale Amount
# =========================
sns.boxplot(data=df, x='residential_type', y='sale_amount')
plt.title("Residential Type vs Sale Amount")
plt.xticks(rotation=45)
plt.show()


# =========================
# 7. Correlation Heatmap
# =========================
corr = df[['sale_amount', 'assess_value', 'sales_ratio']].corr()

sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()


# =========================
# 8. Property Type Count
# =========================
sns.countplot(data=df, x='property_type')
plt.title("Number of Properties by Type")
plt.xticks(rotation=45)
plt.show()


# =========================
# 9. Sales Ratio Distribution
# =========================
sns.histplot(data=df, x='sales_ratio', bins=30)
plt.title("Sales Ratio Distribution")
plt.show()


# =========================
# 10. Pairplot (Deep Insight)
# =========================
sns.pairplot(df[['sale_amount', 'assess_value', 'sales_ratio']])
plt.show()