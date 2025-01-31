import requests
import xml.etree.ElementTree as ET
import csv

# Step 1: Fetch the XML data from the URL
url = "https://www.sedlabanki.is/xmltimeseries/Default.aspx?DagsFra=2014-12-01&DagsTil=2024-12-31&GroupID=10&Type=xml"
response = requests.get(url)
xml_data = response.content

# Step 2: Parse the XML data
root = ET.fromstring(xml_data)

# Step 3: Extract the relevant data (dates and values)
entries = root.findall(".//Entry")
data = []
for entry in entries:
    date = entry.find("Date").text
    value = entry.find("Value").text
    data.append([date, value])

# Step 4: Write the extracted data to a CSV file
csv_file = "output.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Value"])  # Write the header
    writer.writerows(data)  # Write the data

print(f"Data has been written to {csv_file}")