import pandas as pd

# CSV file read
df = pd.read_csv("mumbai student.csv")

# Column names ke extra spaces remove
df.columns = df.columns.str.strip()

# City values ke extra spaces remove
df["City"] = df["City"].str.strip()

# Full data show
print("Full Data:")
print(df)

# First 5 rows
print("\nHead:")
print(df.head())

# Last 5 rows
print("\nTail:")
print(df.tail())

# Mumbai students filter
print("\nMumbai Students:")
mumbai = df[df["City"] == "Mumbai"]
print(mumbai)

# New CSV file save
mumbai.to_csv("mumbai_students.csv", index=False)

print("\nFiltered file saved successfully")