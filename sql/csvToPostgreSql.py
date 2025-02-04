import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

# Step 1: Read the data from both CSV files
atvinnuleysi_data = pd.read_csv('csv files/atvinnuleysiData.csv')
sedlabanki_data = pd.read_csv('csv files/sedlabankiData.csv')

# Step 2: Format the dates to a consistent format
if 'Year-Month' in atvinnuleysi_data.columns:
    atvinnuleysi_data['Year-Month'] = pd.to_datetime(atvinnuleysi_data['Year-Month'], format='%YM%m').dt.strftime('%Y-%m-%d')
else:
    print("Error: 'Year-Month' column not found in atvinnuleysiData.csv")

if 'Date' in sedlabanki_data.columns:
    sedlabanki_data['Date'] = pd.to_datetime(sedlabanki_data['Date']).dt.strftime('%Y-%m-%d')
else:
    print("Error: 'Date' column not found in sedlabankiData.csv")

# Step 3: Create a connection to the PostgreSQL database
engine = create_engine(f'postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# Step 4: Write the data to the SQL database
atvinnuleysi_data.to_sql('atvinnuleysi', engine, if_exists='replace', index=False)
sedlabanki_data.to_sql('sedlabanki', engine, if_exists='replace', index=False)

print("Data has been written to the SQL database")