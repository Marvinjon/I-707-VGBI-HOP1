import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database credentials
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

# Read CSV files
atvinnuleysi_data = pd.read_csv('csv files/atvinnuleysiData.csv')
sedlabanki_data = pd.read_csv('csv files/sedlabankiData.csv')

# Process atvinnuleysi_data: Format dates and calculate percentage
if 'Year-Month' in atvinnuleysi_data.columns:
    atvinnuleysi_data['Year-Month'] = pd.to_datetime(
        atvinnuleysi_data['Year-Month'], format='%YM%m'
    )
    atvinnuleysi_data['Atvinnulausir_Percentage'] = (
        atvinnuleysi_data['Atvinnulausir'] / 
        (atvinnuleysi_data['Atvinnulausir'] + atvinnuleysi_data['Starfandi'])
    )
else:
    raise KeyError("'Year-Month' column not found in atvinnuleysiData.csv")

# Process sedlabanki_data: Format dates and calculate monthly averages
if 'Date' in sedlabanki_data.columns:
    sedlabanki_data['Date'] = pd.to_datetime(
        sedlabanki_data['Date'], format='%m/%d/%Y %I:%M:%S %p'
    )
    # Create 'Year-Month' column (first day of each month)
    sedlabanki_data['Year-Month'] = sedlabanki_data['Date'].dt.to_period('M').dt.to_timestamp()
    monthly_avg_sedlabanki = sedlabanki_data.groupby('Year-Month', as_index=False)['Value'].mean()
else:
    raise KeyError("'Date' column not found in sedlabankiData.csv")

# Create SQL engine
engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# Write atvinnuleysi_data to SQL table (monthly data with percentage)
atvinnuleysi_data.to_sql(
    'atvinnuleysi', 
    engine, 
    if_exists='replace', 
    index=False
)

# Write monthly_avg_sedlabanki to SQL table
monthly_avg_sedlabanki.to_sql(
    'sedlabanki', 
    engine, 
    if_exists='replace', 
    index=False
)

print("Data written to SQL")