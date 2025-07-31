import pandas as pd

# 🔹 Step 1: Load the original files
games = pd.read_csv("games.csv")
sales = pd.read_csv("vgsales.csv")

# 🔹 Step 2: Print first few rows to check
print("📘 Games Data:")
print(games.head())

print("\n💿 Sales Data:")
print(sales.head())

# 🔹 Step 3: Print all column names to confirm them (important for beginners!)
print("\nColumns in games.csv:")
print(games.columns.tolist())

print("\nColumns in vgsales.csv:")
print(sales.columns.tolist())

# 🔹 Step 4: Clean games.csv
# Confirm the exact column names and update these if needed
# Common column names: Rating, Plays, Wishlist, Release Date
games_clean = games.dropna(subset=["Rating", "Plays", "Wishlist", "Release Date"])

# Convert Release Date to real datetime format
games_clean["Release Date"] = pd.to_datetime(games_clean["Release Date"], errors="coerce")

# 🔹 Step 5: Clean vgsales.csv
# Drop rows where important info is missing
sales_clean = sales.dropna(subset=["Name", "Genre", "Year", "Global_Sales"])

# 🔹 Step 6: Fix column names to remove spaces (very important for Power BI)
games_clean = games_clean.rename(columns=lambda x: x.strip().replace(" ", "_"))
sales_clean = sales_clean.rename(columns=lambda x: x.strip().replace(" ", "_"))

# 🔹 Step 7: Save the cleaned data
games_clean.to_csv("clean_games.csv", index=False)
sales_clean.to_csv("clean_vgsales.csv", index=False)

print("\n✅ Cleaned files saved as:")
print("- clean_games.csv")
print("- clean_vgsales.csv")