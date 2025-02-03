import requests
import os
import json


for key, value in os.environ.items():
    print(f"{key}: {value}")
 
# Load API key from environment variable
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Set the GOOGLE_MAPS_API_KEY environment variable.")

# Library of Lat/Lng for San Francisco and New York City
city_coordinates = {
    "San Francisco": {
        "lat": 37.7749,
        "lng": -122.4194
    },
    "New York City": {
        "lat": 40.7128,
        "lng": -74.0060
    }
}

# Function to fetch places for a given city
def fetch_places(city_name, radius=5000):  # Reduced radius to 5 km
    if city_name not in city_coordinates:
        print(f"Error: {city_name} not found in the library.")
        return

    # Get Lat/Lng for the city
    lat = city_coordinates[city_name]["lat"]
    lng = city_coordinates[city_name]["lng"]

    # Build the API URL
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&key={API_KEY}"

    # Fetch data
    response = requests.get(url).json()

    # Check for errors in the API response
    if response.get("status") != "OK":
        print(f"Error: {response.get('error_message', 'Unknown error')}")
        return

    # Save results to a JSON file
    with open(f"{city_name}_places.json", "w") as f:
        json.dump(response, f, indent=4)  # Pretty-print JSON

    print(f"Data saved to {city_name}_places.json")

# Example usage
fetch_places("San Francisco")  # Fetch places in San Francisco
fetch_places("New York City")  # Fetch places in New York City


