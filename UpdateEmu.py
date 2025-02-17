import requests
import os
import zipfile
from datetime import datetime

#unified area for all updaters rather than separte files.

def duckstationUpdater():
    pass

def pcsx2Updater():
    pass

def ppssppUpdater():
    pass

def rpcs3Updater():
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

def shadPS4Updater():
    pass

def xemuUpdater():
    pass

def xeniaUpdater():
    # Define a function to download Xenia builds
    def download_xenia_build(build):
        # Create the directory if it doesn't exist
        if not os.path.exists(build.folder_name):
            os.makedirs(build.folder_name)

        # Use requests to download the build
        response = requests.get(build.url)
        if response.status_code == 200:
            with open(f"{build.folder_name}/{build.zip_name}.zip", 'wb') as f:
                f.write(response.content)
            print("Download completed.")
            extract_build(build)
        else:
            print("Failed to download the build.")

    # Define a function to extract Xenia builds
    def extract_build(build):
        zip_file_path = f"{build.folder_name}/{build.zip_name}.zip"
        #target_directory = r"D:\EMULATORS\(Xbox360) Xenia_Canary" #needs to be changed to the correct path
        
        # Ensure the target directory exists
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        
        # Extract the zip file to the target directory
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(target_directory)
        print("Extraction completed.")

    # Define a class to represent Xenia builds
    class XeniaBuild:
        def __init__(self, name, url, description, folder_name, zip_name):
            self.name = name
            self.url = url
            self.description = description
            self.folder_name = folder_name
            self.zip_name = zip_name

    # Define the list of Xenia builds
    xenia_canary = XeniaBuild("Canary",
                            "https://github.com/xenia-canary/xenia-canary-releases/releases/download/canary_experimental/xenia_canary_windows.zip",
                            "Xenia Canary is a build intended for testing features with a small subset of users.",
                            "XeniaCanary", "xenia_canary")

    # Download and extract Xenia Canary build
    download_xenia_build(xenia_canary)


