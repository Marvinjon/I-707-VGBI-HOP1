import requests
import csv
import json

# Step 1: Define the JSON query
query = {
    "query": [
        {
            "code": "Mánuður",
            "selection": {
                "filter": "item",
                "values": [
                    "2014M12", "2015M01", "2015M02", "2015M03", "2015M04", "2015M05", "2015M06", "2015M07", "2015M08", "2015M09",
                    "2015M10", "2015M11", "2015M12", "2016M01", "2016M02", "2016M03", "2016M04", "2016M05", "2016M06", "2016M07",
                    "2016M08", "2016M09", "2016M10", "2016M11", "2016M12", "2017M01", "2017M02", "2017M03", "2017M04", "2017M05",
                    "2017M06", "2017M07", "2017M08", "2017M09", "2017M10", "2017M11", "2017M12", "2018M01", "2018M02", "2018M03",
                    "2018M04", "2018M05", "2018M06", "2018M07", "2018M08", "2018M09", "2018M10", "2018M11", "2018M12", "2019M01",
                    "2019M02", "2019M03", "2019M04", "2019M05", "2019M06", "2019M07", "2019M08", "2019M09", "2019M10", "2019M11",
                    "2019M12", "2020M01", "2020M02", "2020M03", "2020M04", "2020M05", "2020M06", "2020M07", "2020M08", "2020M09",
                    "2020M10", "2020M11", "2020M12", "2021M01", "2021M02", "2021M03", "2021M04", "2021M05", "2021M06", "2021M07",
                    "2021M08", "2021M09", "2021M10", "2021M11", "2021M12", "2022M01", "2022M02", "2022M03", "2022M04", "2022M05",
                    "2022M06", "2022M07", "2022M08", "2022M09", "2022M10", "2022M11", "2022M12", "2023M01", "2023M02", "2023M03",
                    "2023M04", "2023M05", "2023M06", "2023M07", "2023M08", "2023M09", "2023M10", "2023M11", "2023M12", "2024M01",
                    "2024M02", "2024M03", "2024M04", "2024M05", "2024M06", "2024M07", "2024M08", "2024M09", "2024M10", "2024M11",
                    "2024M12"
                ]
            }
        },
        {
            "code": "Kyn/aldur",
            "selection": {
                "filter": "item",
                "values": ["0"]
            }
        },
        {
            "code": "Eining",
            "selection": {
                "filter": "item",
                "values": ["3", "4"]
            }
        }
    ],
    "response": {
        "format": "json"
    }
}

# Step 2: Fetch the data from the URL
url = "https://px.hagstofa.is:443/pxis/api/v1/is/Samfelag/vinnumarkadur/vinnumarkadsrannsokn/1_manadartolur/VIN00001.px"
response = requests.post(url, json=query)
data = response.json()

# Step 3: Extract the relevant data
results = data['data']

# Step 4: Write the extracted data to a CSV file
csv_file = "atvinnuleysi_data.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Month", "Gender/Age", "Unit", "Value"])  # Write the header
    for result in results:
        key = result['key']
        value = result['values'][0]
        writer.writerow([key[0], key[1], key[2], value])

print(f"Data has been written to {csv_file}")