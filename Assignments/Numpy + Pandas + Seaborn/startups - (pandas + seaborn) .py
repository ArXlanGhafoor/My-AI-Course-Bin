import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =========================
# Load Dataset
# =========================
# Reading startups dataset
# CSV contains information about global unicorn startups

# Note: first unnamed column is index, so we handle it using index_col=0

df = pd.read_csv('CSV Files/startups.csv', index_col=0)

print("Raw DataFrame:")
print(df)

# =========================
# Basic Inspection
# =========================
print("\nData Types:")
print(df.dtypes)

print("\nDataFrame Info:")
df.info()

print("\nFirst 3 Rows:")
print(df.head(3))

print("\nLast 3 Rows:")
print(df.tail(3))

print("\nShape of Dataset:")
print(df.shape)

# =========================
# Data Cleaning (Important for real-world CSVs)
# =========================

# Remove '$' and convert Valuation to numeric
# This is necessary because valuation is stored as string

df['Valuation ($B)'] = df['Valuation ($B)'].replace('[\$,]', '', regex=True).astype(float)

# Convert Date Joined to datetime format
# Helps in time-based analysis later

df['Date Joined'] = pd.to_datetime(df['Date Joined'])

print("\nCleaned Data Types:")
print(df.dtypes)

# =========================
# Column Selection
# =========================

print("\nCompany column:")
print(df['Company'])

print("\nMultiple columns (Company + Country):")
print(df[['Company', 'Country']])

# =========================
# .loc Operations (Label-based selection)
# =========================

print("\nSingle row using .loc:")
print(df.loc[0])

print("\nMultiple rows using .loc:")
print(df.loc[[1, 3]])

print("\nConditional selection (.loc): United States companies")
print(df.loc[df['Country'] == 'United States'])

print("\nSelect specific columns (.loc):")
print(df.loc[:, ['Company', 'Industry']])

# =========================
# .iloc Operations (Position-based selection)
# =========================

print("\nSingle row (.iloc):")
print(df.iloc[0])

print("\nMultiple rows (.iloc):")
print(df.iloc[[1, 3, 5]])

print("\nRow slice (.iloc):")
print(df.iloc[0:4])

print("\nColumn selection (.iloc):")
print(df.iloc[:, [0, 2]])

# =========================
# Sorting Data
# =========================

# Sort by valuation (largest startups first)
sorted_df = df.sort_values(by='Valuation ($B)', ascending=False)

print("\nTop valued startups:")
print(sorted_df)

# Sort by Country and Valuation
multi_sorted = df.sort_values(by=['Country', 'Valuation ($B)'], ascending=[True, False])

print("\nSorted by Country and Valuation:")
print(multi_sorted)

# =========================
# Filtering Data
# =========================

# Filter high value startups (>50B)
high_value = df.query('`Valuation ($B)` > 50')

print("\nHigh value startups (>50B):")
print(high_value)

# =========================
# Grouping Data
# =========================

# Total valuation per country
grouped_country = df.groupby('Country')['Valuation ($B)'].sum()

print("\nTotal valuation by country:")
print(grouped_country)

# =========================
# DataFrame Manipulation
# =========================

# Add a new row (example startup)
df.loc[len(df.index)] = [
    "NewAI Startup", 10.5, pd.to_datetime("2024-01-01"),
    "Pakistan", "Lahore", "Artificial intelligence",
    "Local Investors"
]

print("\nAfter adding new startup:")
print(df.tail(2))

# =========================
# Remove Data
# =========================

# Remove a row safely
if 0 in df.index:
    df.drop(index=0, inplace=True)

# Drop a column (example: Select Investors)
# Keeping dataset simpler for analysis

df.drop(columns=['Select Investors'], inplace=True)

print("\nAfter removing column:")
print(df.head())

# =========================
# Renaming Columns
# =========================

df.rename(columns={
    'Date Joined': 'Join_Date'
}, inplace=True)

print("\nAfter renaming columns:")
print(df.head())

# =========================
# Missing Values Handling
# =========================

print("\nMissing values count:")
print(df.isnull().sum())

# Fill missing values (if any)
df.fillna('Unknown', inplace=True)


# =========================
# EDA Report
# =========================
print('\n=====EDA Report======\n')
cols = ['Valuation ($B)']
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
# Final Summary
# =========================

print("\nFinal dataset shape:", df.shape)
print("\nCleaned and processed dataset ready for analysis")
print("CSV Saved",df.to_csv("clean_startups.csv"))
print(df.columns)



# =========================
# Load and clean dataset
# =========================
df = pd.read_csv("clean_startups.csv", index_col=0)
print(df.columns)

# Filter dataset (optional subset for cleaner plots)
dffilter = df.copy()

sns.set_theme(style="darkgrid")

# =========================
# 1. Histogram (distribution of valuation)
# =========================
sns.histplot(data=dffilter, x="Valuation ($B)")
plt.title("Startup Valuation Distribution")
plt.show()


# =========================
# 2. KDE Plot (smooth distribution)
# =========================
sns.kdeplot(data=dffilter, x="Valuation ($B)", fill=True)
plt.title("KDE of Startup Valuation")
plt.show()


# =========================
# 3. Scatter Plot (valuation vs time)
# =========================
sns.scatterplot(
    data=dffilter,
    x="Join_Date",
    y="Valuation ($B)",
    hue="Country"
)


plt.title("Valuation Over Time by Country")
plt.xticks(rotation=45)
plt.show()


# =========================
# 4. Line Plot (trend over time)
# =========================
sns.lineplot(
    data=dffilter.sort_values("Join_Date"),
    x="Join_Date",
    y="Valuation ($B)",
    estimator=None
)
plt.title("Startup Valuation Trend Over Time")
plt.xticks(rotation=45)
plt.show()


# =========================
# 5. Bar Plot (average valuation per country)
# =========================
country_avg = dffilter.groupby("Country")["Valuation ($B)"].mean().reset_index()

sns.barplot(data=country_avg, x="Country", y="Valuation ($B)")
plt.title("Average Startup Valuation by Country")
plt.xticks(rotation=45)
plt.show()


# =========================
# 6. Count Plot (industry distribution)
# =========================
sns.countplot(data=dffilter, x="Industry")
plt.title("Number of Startups per Industry")
plt.xticks(rotation=45)
plt.show()

# =========================
# 7. Catplot (industry vs valuation)
# =========================
sns.catplot(
    data=dffilter,
    x="Industry",
    y="Valuation ($B)",
    kind="bar",
    height=5,
    aspect=2
)
plt.xticks(rotation=45)
plt.title("Industry vs Valuation")
plt.show()


# =========================
# 8. Heatmap (Country vs Industry avg valuation)
# =========================
pivot_data = dffilter.pivot_table(
    index="Country",
    columns="Industry",
    values="Valuation ($B)",
    aggfunc="mean"
)

sns.heatmap(pivot_data, cmap="YlGnBu")
plt.title("Country vs Industry Valuation Heatmap")
plt.show()