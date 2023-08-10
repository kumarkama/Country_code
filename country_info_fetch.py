import requests
import data.json

def fetch_country_info(country_code):
    api_url = f"https://www.travel-advisory.info/api/{country_code}"
    
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        
        if data:
            country_name = data[0]['name']['common']
            region = data[0]['region']
            capital = data[0]['capital'][0]
            
            result = (
                f"Country Code: {country_code}\n"
                f"Country Name: {country_name}\n"
                f"Region: {region}\n"
                f"Capital: {capital}"
            )
            return result
        else:
            return f"Country information not found for code: {country_code}"
    else:
        return f"Error fetching data for code: {country_code}"

# Main program
input_country_code = input("Enter a country code: ").upper()
result = fetch_country_info(input_country_code)
print(result)

