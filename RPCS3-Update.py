import requests
from datetime import datetime

api_url = "https://update.rpcs3.net/?api=v2&c=bf8621c9"
response = requests.get(api_url)

# Ensure the response is successful
if response.status_code == 200:
    data = response.json()

    # Current and latest build datetime
    current_datetime_str = data['current_build']['datetime']
    latest_datetime_str = data['latest_build']['datetime']
    
    # Compare the datetimes
    current_datetime = datetime.strptime(current_datetime_str, '%Y-%m-%d %H:%M:%S')
    latest_datetime = datetime.strptime(latest_datetime_str, '%Y-%m-%d %H:%M:%S')    
    if latest_datetime > current_datetime:
        print("A newer build is available.")
        windows_download_url = data['latest_build']['windows']['download']
        print(f"Download the new version from: {windows_download_url}")
    else:
        print("The current version is up-to-date.")
else:
    print(f"Failed to fetch data from the API. Status code: {response.status_code}")
