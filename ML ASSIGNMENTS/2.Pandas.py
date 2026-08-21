import pandas as pd
import numpy as np

data = {
    "Name": ["Arun", "Bala", "Cathy", "Dinesh", "Elango"],
    "Department": ["IT", "CSE", "IT", "CSE", "IT"],
    "Marks": [85, 90, np.nan, 75, 80],
    "Age": [20, np.nan, 21, 20, np.nan]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

print("\n1. Detect and Count Missing Values")
print(df.isnull().sum().to_string())

print("\n2. Removing Missing Values")
print(df.dropna().to_string(index=False))

print("\n3. Filling Missing Values")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df.to_string(index=False))

print("\n4. Grouping Data")
result = df.groupby("Department")["Marks"].mean()
print(result.to_string())
