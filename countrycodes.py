import argparse
import json
import requests

API_URL = "https://www.travel-advisory.info/api"
DATA_FILE = "data.json"

def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from API")
        return None

def save_data_to_file(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def load_data_from_file():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def lookup_country_name(country_codes, data):
    country_names = {}
    for code in country_codes:
        if code in data['data']:
            country_names[code] = data['data'][code]['name']
        else:
            country_names[code] = "Country not found"
    return country_names

def main():
    parser = argparse.ArgumentParser(description="Country Lookup Service")
    parser.add_argument("--countryCodes", nargs="+", help="List of country codes", required=True)
    args = parser.parse_args()

    data = load_data_from_file()

    if data is None:
        print("Fetching data from API...")
        data = fetch_data()
        if data:
            save_data_to_file(data)
    else:
        print("Using data from file...")

    country_names = lookup_country_name(args.countryCodes, data)
    for code, name in country_names.items():
        print(f"{code}: {name}")

if __name__ == "__main__":
    main()
