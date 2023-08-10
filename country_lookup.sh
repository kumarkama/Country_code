#!/bin/bash

# Associative array to store country information
declare -A countries
countries["USA"]="United States of America"
countries["CAN"]="Canada"
countries["UK"]="United Kingdom"
countries["AU"]="Australia"
countries["SA"]="South Africa"
# Add more countries and their information here

# Function to perform country lookup
lookup_country() {
    local country_code="$1"
    if [[ -n "${countries[$country_code]}" ]]; then
        echo "Country Code: $country_code"
        echo "Country Name: ${countries[$country_code]}"
    else
        echo "Country not found for code: $country_code"
    fi
}

# Main program
read -p "Enter a country code: " input_country_code
lookup_country "$input_country_code"
