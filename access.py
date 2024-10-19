import os

def get_opensky_credentials():
    """
    Retrieve OpenSky API credentials from environment variables.
    
    Returns:
    tuple: A tuple containing (username, password).
    """
    username = os.getenv('OPEN_SKY_USER')
    password = os.getenv('OPEN_SKY_PASS')
    
    if not username or not password:
        raise ValueError("OpenSky API credentials are not set in environment variables.")
    
    return username, password
