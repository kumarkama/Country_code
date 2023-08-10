#!/bin/bash

# Function to fetch country information from Rest Countries API
fetch_country_info() {
    local country_code="$1"
    local api_url="https://www.travel-advisory.info/api/$country_code"
    
    local response=$(curl -s "$api_url")
    
    if [[ -n "$response" ]]; then
        local country_name=$(echo "$response" | jq -r '.[0].name.common')
        local region=$(echo "$response" | jq -r '.[0].region')
        local capital=$(echo "$response" | jq -r '.[0].capital[0]')
        
        echo "Country Code: $country_code"
        echo "Country Name: $country_name"
        echo "Region: $region"
        echo "Capital: $capital"
    else
        echo "Country information not found for code: $country_code"
    fi
}

# Main program
read -p "Enter a country code: " input_country_code
fetch_country_info "$input_country_code"

