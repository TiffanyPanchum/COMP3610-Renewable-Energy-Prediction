import requests
import time
import pandas as pd
from meteostat import Stations

# Your Meteostat API Key
API_KEY = "573595f6c3mshce92959d517ebcep1d0ba2jsn31025acc266e"

# Base URL for Meteostat API
BASE_URL = "https://meteostat.p.rapidapi.com/stations/hourly"

# Headers for the API request
headers = {
    "x-rapidapi-host": "meteostat.p.rapidapi.com",
    "x-rapidapi-key": API_KEY
}

date_ranges = [
    ("2016-01-01", "2016-01-31"),("2016-02-01", "2016-02-29"),("2016-03-01", "2016-03-31"),("2016-04-01", "2016-04-30"),("2016-05-01", "2016-05-31"),("2016-06-01", "2016-06-30"),("2016-07-01", "2016-07-31"),("2016-08-01", "2016-08-31"),("2016-09-01", "2016-09-30"),("2016-10-01", "2016-10-31"),("2016-11-01", "2016-11-30"),("2016-12-01", "2016-12-31"),
    ("2017-01-01", "2017-01-31"),("2017-02-01", "2017-02-28"),("2017-03-01", "2017-03-31"),("2017-04-01", "2017-04-30"),("2017-05-01", "2017-05-31"),("2017-06-01", "2017-06-30"),("2017-07-01", "2017-07-31"),("2017-08-01", "2017-08-31"),("2017-09-01", "2017-09-30"),("2017-10-01", "2017-10-31"),("2017-11-01", "2017-11-30"),("2017-12-01", "2017-12-31"),
    ("2018-01-01", "2018-01-31"),("2018-02-01", "2018-02-28"),("2018-03-01", "2018-03-31"),("2018-04-01", "2018-04-30"),("2018-05-01", "2018-05-31"),("2018-06-01", "2018-06-30"),("2018-07-01", "2018-07-31"),("2018-08-01", "2018-08-31"),("2018-09-01", "2018-09-30"),("2018-10-01", "2018-10-31"),("2018-11-01", "2018-11-30"),("2018-12-01", "2018-12-31"),
    ("2019-01-01", "2019-01-31"),("2019-02-01", "2019-02-28"),("2019-03-01", "2019-03-31"),("2019-04-01", "2019-04-30"),("2019-05-01", "2019-05-31"),("2019-06-01", "2019-06-30"),("2019-07-01", "2019-07-31"),("2019-08-01", "2019-08-31"),("2019-09-01", "2019-09-30"),("2019-10-01", "2019-10-31"),("2019-11-01", "2019-11-30"),("2019-12-01", "2019-12-31"),
    ("2020-01-01", "2020-01-31"),("2020-02-01", "2020-02-29"),("2020-03-01", "2020-03-31"),("2020-04-01", "2020-04-30"),("2020-05-01", "2020-05-31"),("2020-06-01", "2020-06-30"),("2020-07-01", "2020-07-31"),("2020-08-01", "2020-08-31"),("2020-09-01", "2020-09-30"),("2020-10-01", "2020-10-31"),("2020-11-01", "2020-11-30"),("2020-12-01", "2020-12-31"),
    ("2021-01-01", "2021-01-31"),("2021-02-01", "2021-02-28"),("2021-03-01", "2021-03-31"),("2021-04-01", "2021-04-30"),("2021-05-01", "2021-05-31"),("2021-06-01", "2021-06-30"),("2021-07-01", "2021-07-31"),("2021-08-01", "2021-08-31"),("2021-09-01", "2021-09-30"),("2021-10-01", "2021-10-31"),("2021-11-01", "2021-11-30"),("2021-12-01", "2021-12-31"),
    ("2022-01-01", "2022-01-31"),("2022-02-01", "2022-02-28"),("2022-03-01", "2022-03-31"),("2022-04-01", "2022-04-30"),("2022-05-01", "2022-05-31"),("2022-06-01", "2022-06-30"),("2022-07-01", "2022-07-31"),("2022-08-01", "2022-08-31"),("2022-09-01", "2022-09-30"),("2022-10-01", "2022-10-31"),("2022-11-01", "2022-11-30"),("2022-12-01", "2022-12-31")
]

# Fetching Data for Italy
df = pd.DataFrame()
for start_date, end_date in date_ranges:
    
    querystring = {"station": "16235", "start": start_date, "end": end_date}
    
    response = requests.get(BASE_URL, headers=headers, params=querystring)
    
    if response.status_code == 200:

        data = response.json() 
        if 'data' in data:
            hourly_df = pd.DataFrame(data['data'])
            df = pd.concat([df, hourly_df], ignore_index=True)
    else:
        print(f"Failed to fetch data for {start_date} to {end_date}")

    time.sleep(2)

df.to_csv("data/raw/weather_data_italy.csv", index=False)



# Fetching Data for Spain
df = pd.DataFrame()
for start_date, end_date in date_ranges:
    
    querystring = {"station": "08314", "start": start_date, "end": end_date}
    
    response = requests.get(BASE_URL, headers=headers, params=querystring)
    
    if response.status_code == 200:

        data = response.json() 
        if 'data' in data:
            hourly_df = pd.DataFrame(data['data'])
            df = pd.concat([df, hourly_df], ignore_index=True)
    else:
        print(f"Failed to fetch data for {start_date} to {end_date}")

    time.sleep(2)

df.to_csv("data/raw/weather_data_spain.csv", index=False)


# Fetching Data for France
df = pd.DataFrame()
for start_date, end_date in date_ranges:
    
    querystring = {"station": "07156", "start": start_date, "end": end_date}
    
    response = requests.get(BASE_URL, headers=headers, params=querystring)
    
    if response.status_code == 200:

        data = response.json() 
        if 'data' in data:
            hourly_df = pd.DataFrame(data['data'])
            df = pd.concat([df, hourly_df], ignore_index=True)
    else:
        print(f"Failed to fetch data for {start_date} to {end_date}")

    time.sleep(2)

df.to_csv("data/raw/weather_data_france.csv", index=False)
