import requests
import json

# url = "https://apis.deutschebahn.com/db-api-marketplace/apis/station-data/v2/stations/"
# url = "https://apis.deutschebahn.com/db-api-marketplace/apis/station-data/v2/szentralen"
url = "https://apis.deutschebahn.com/db-api-marketplace/apis/station-data/v2/stations"

headers = {
    "DB-Client-ID": "5bbcb883a5566e9a8e2311e89e4aae78",
    "DB-Api-Key": "6e5b1b403a667a797ab2fe436bee3e17",
    "accept": "application/json"
}

# Make the API request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()
    
    # Write the JSON data to a file
    with open("station_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    print("Response saved to station_data.json")
else:
    print(f"Failed to get data: {response.status_code}")
    
