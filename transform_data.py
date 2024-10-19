def transform_flight_data(raw_data):
    # Initialize an empty list to store transformed data
    transformed_data = []

    # Check if 'states' is in the raw data
    if 'states' in raw_data:
        for flight in raw_data['states']:
            # Create a dictionary with only the relevant fields
            flight_info = {
                'icao24': flight[0],
                'callsign': flight[1],
                'country': flight[2],
                'latitude': flight[6],
                'longitude': flight[5]
            }
            transformed_data.append(flight_info)

    return transformed_data
