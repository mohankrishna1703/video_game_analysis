import pandas as pd
import sqlite3

# Load cleaned CSV files
games = pd.read_csv("clean_games.csv")
sales = pd.read_csv("clean_vgsales.csv")

# Connect to SQLite database (or create one)
conn = sqlite3.connect("videogames.db")
cursor = conn.cursor()

# Save dataframes to SQL tables
games.to_sql("games", conn, if_exists="replace", index=False)
sales.to_sql("sales", conn, if_exists="replace", index=False)

# Confirm tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(" Tables created:", cursor.fetchall())

# Optional: Show first few rows
print("\n First rows from games table:")
print(pd.read_sql("SELECT * FROM games LIMIT 5", conn))

print("\n First rows from sales table:")
print(pd.read_sql("SELECT * FROM sales LIMIT 5", conn))

# Close connection
conn.close()