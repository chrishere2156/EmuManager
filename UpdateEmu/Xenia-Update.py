import requests
import os
import zipfile

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