# Importing required libraries
import requests
import pandas as pd
import time

# API Key for Census API
api_key = "4607a5fc83239c9bc97ddfe5debf4888e4badaa5"

# Variable to extract from ACS: Poverty Rate (% of population below poverty line)
pov_var = "S1701_C03_001E"

# Years to pull data for (2012 to 2023 inclusive)
years = list(range(2012, 2024))

# List of Florida counties considered (name and FIPS code)
counties = {
    "Hillsborough County": "057",
    "Miami-Dade County": "086",
    "Broward County": "011",
    "Duval County": "031",
    "Orange County": "095",
    "Lee County": "071"
}

# List of Florida cities considered (name and FIPS code)
cities = {
    "Tampa City": "71000",
    "Orlando City": "53000",
    "Jacksonville City": "35000",
    "St. Petersburg City": "63000",
    "Hialeah City": "30000",
    "Fort Lauderdale City": "24100"
}

# Function to fetch poverty data for a given county and year
def get_county_data(year, county_fips):
    url = f"https://api.census.gov/data/{year}/acs/acs5/subject"  # Using ACS 5-Year for all years

    params = {
        "get": pov_var,
        "for": f"county:{county_fips}",
        "in": "state:12",
        "key": api_key
    }

    # API request inside a try-except block to handle exceptions
    try:
        response = requests.get(url, params=params, timeout=15)
        if response.status_code == 200:
            data = response.json()
            return float(data[1][0])  # Extract the poverty rate
        else:
            print(f"Error fetching COUNTY {county_fips} for {year}: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"RequestException fetching COUNTY {county_fips} for {year}: {e}")
        return None

# Function to fetch poverty data for a given city and year
def get_city_data(year, place_fips):
    url = f"https://api.census.gov/data/{year}/acs/acs5/subject"  # Using ACS 5-Year for all years

    params = {
        "get": pov_var,
        "for": f"place:{place_fips}",
        "in": "state:12",
        "key": api_key
    }

    # API request inside a try-except block to handle exceptions
    try:
        response = requests.get(url, params=params, timeout=15)
        if response.status_code == 200:
            data = response.json()
            return float(data[1][0])  # Extract the poverty rate
        else:
            print(f"Error fetching CITY {place_fips} for {year}: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"RequestException fetching CITY {place_fips} for {year}: {e}")
        return None

# Empty list to store data for each year
all_data = []

# Loop through each year and pull data
for year in years:
    row = {"Year": year}  # Start a new row for the current year

    for county_name, county_fips in counties.items():
        poverty_rate = get_county_data(year, county_fips)
        row[county_name] = poverty_rate
        time.sleep(0.5)

    for city_name, place_fips in cities.items():
        poverty_rate = get_city_data(year, place_fips)
        row[city_name] = poverty_rate
        time.sleep(0.5)

    all_data.append(row)
    print(f"Fetched data for {year}")

# Converting collected data into a df
df = pd.DataFrame(all_data)

# Saving df to an Excel file
df.to_excel("florida_poverty_data_2012_2023.xlsx", index=False, sheet_name="County_City_Level_Poverty_Data")

print("Data collection completed. File 'florida_poverty_data_2012_2023.xlsx' created.")
