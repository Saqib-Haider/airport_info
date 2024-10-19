from access import get_opensky_credentials
from transform_data import transform_flight_data
import requests

def extract_opensky_data(bbox):
    # Retrieve OpenSky API credentials from environment variables
    username, password = get_opensky_credentials()

    if not username or not password:
        raise ValueError("OpenSky API credentials are missing.")

    url = 'https://opensky-network.org/api/states/all'
    params = {
        'lamin': bbox[0],   # Minimum latitude
        'lamax': bbox[1],   # Maximum latitude
        'lomin': bbox[2],   # Minimum longitude
        'lomax': bbox[3]    # Maximum longitude
    }

    # Send the request with basic authentication
    try:
        response = requests.get(url, params=params, auth=(username, password))
        
        if response.status_code == 200:
            # Return the JSON response if the request was successful
            return response.json()
        elif response.status_code == 401:
            print("Authentication failed. Check your OpenSky API credentials.")
        elif response.status_code == 429:
            print("Rate limit exceeded. Try again later.")
        else:
            print(f"Error: Unable to fetch data. Status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    return None

if __name__ == "__main__":
    bbox = (30.0, 50.0, -130.0, -60.0)  # Example bounding box
    raw_data = extract_opensky_data(bbox)

    if raw_data:
        # Transform the extracted data
        flight_data = transform_flight_data(raw_data)

        # Print the transformed data
        for flight in flight_data:
            print(flight)  # Display the cleaned flight data
