from sqlalchemy.orm import sessionmaker
from models import *
def load_data_into_mysql(transformed_data):

    for flight in transformed_data:
        # Create a new Flight object for each flight data row
        flight_record = Flight(
            icao24=flight['icao24'],
            callsign=flight['callsign'],
            country=flight['country'],
            latitude=flight['latitude'],
            longitude=flight['longitude']
        )
        session.add(flight_record)
    
    # Commit the transaction to save the data to the database
    session.commit()

    print("Data loaded into MySQL successfully!")
