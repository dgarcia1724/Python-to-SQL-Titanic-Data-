import pandas as pd
from db_connection import get_db_engine

# Load the CSV file into a DataFrame
df = pd.read_csv('titanic.csv')
df.columns = df.columns.str.lower() #Convert DataFrame column names to lowercase

# Get the database engine
engine = get_db_engine()

# Insert data into the PostgreSQL table (if the table already exists, set `if_exists='append'`)
df.to_sql('titanic', engine, index=False, if_exists='append')

print("Data successfully imported into the 'titanic' table.")
