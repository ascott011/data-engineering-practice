import requests
import os

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]



def main():
    # download the files
    # using python, check if the folder exits and create a new directory called "downloads"
    # check for validity of urls before downloading
    # extract csv file from zip
    # rename csv file to just file name without path
    if not os.path.exists("downloads"):
        os.mkdir("downloads")
    for uri in download_uris:
        response = requests.head(uri)
        if response.status_code == 200:
            print(f"Downloading from {uri}...")
            r = requests.get(uri)
            file_name = uri.split("/")[-1]
            zip_path = os.path.join("downloads", file_name)
            with open(zip_path, "wb") as f:
                f.write(r.content)
            print(f"Downloaded {file_name} to downloads/")
        else:
            print(f"URL {uri} is not valid. Skipping download.")


if __name__ == "__main__":
    main()
