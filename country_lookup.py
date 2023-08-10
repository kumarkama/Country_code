import data.json

# Dictionary to store country information
countries = {
    "USA": "United States of America",
    "CAN": "Canada",
    "UK": "United Kingdom",
    # Add more countries and their information here
}

# Function to perform country lookup
def lookup_country(country_code):
    if country_code in countries:
        return f"Country Code: {country_code}\nCountry Name: {countries[country_code]}"
    else:
        return f"Country not found for code: {country_code}"

# Main program
input_country_code = input("Enter a country code: ")
result = lookup_country(input_country_code)
print(result)

