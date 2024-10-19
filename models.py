from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flights'  # Name of the table in the database

    icao24 = Column(String, primary_key=True)  # Primary key
    callsign = Column(String)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self):
        return f"<Flight(icao24={self.icao24}, callsign={self.callsign},country={self.country} ,latitude={self.latitude}, longitude={self.longitude})>"
