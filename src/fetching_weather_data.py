import requests
import time
import pandas as pd

# Your Meteostat API Key
API_KEY = "51a1a1385amsh8a2062112967694p11c6c0jsncc63f327d026"

# Base URL for Meteostat API
BASE_URL = "https://meteostat.p.rapidapi.com/point/monthly"

# List of countries with their latitude, longitude, and altitude (you can expand this list)
countries = [
    {"name": "Germany", "lat": 52.5244, "lon": 13.4105, "alt": 43},  # Example: Berlin
    {"name": "United States", "lat": 40.7128, "lon": -74.0060, "alt": 10},  # Example: New York
    {"name": "Brazil", "lat": -15.7801, "lon": -47.9292, "alt": 1172},  # Example: Brasília
    # Add more countries here with their latitudes, longitudes, and altitudes
]

# Parameters (for the time range)
start_year = 2016
end_year = 2022

# Headers for the API request
headers = {
    "x-rapidapi-host": "meteostat.p.rapidapi.com",
    "x-rapidapi-key": API_KEY
}

# Fetch data year by year for each country
for country in countries:
    country_name = country["name"]
    latitude = country["lat"]
    longitude = country["lon"]
    altitude = country["alt"]
    
    for year in range(start_year, end_year + 1):
        start_date = f"{year}-01-01"
        end_date = f"{year}-12-31"
        
        params = {
            "lat": latitude,
            "lon": longitude,
            "alt": altitude,
            "start": start_date,
            "end": end_date
        }
        
        print(f"Fetching data for {country_name} in {year}...")
        
        response = requests.get(BASE_URL, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if the 'data' key exists in the response
            if 'data' in data:
                df = pd.DataFrame(data['data'])  # Convert the data to a pandas DataFrame
                
                # Save the DataFrame as a CSV file
                df.to_csv(f"weather_data_{country_name}_{year}.csv", index=False)
                print(f"Data for {country_name} in {year} saved as CSV successfully!")
            else:
                print(f"No data available for {country_name} in {year}")
        else:
            print(f"Failed to fetch data for {country_name} in {year}: {response.status_code}")
        
        # To avoid hitting API limits, wait for 2 seconds between requests
        time.sleep(2)

print("All data fetched and saved as CSV successfully!")
