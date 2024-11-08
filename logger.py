import logging
import configparser
import os

# Function to map numeric log levels
def get_log_level(loglevel):
    try:
        # Convert the loglevel to an integer if it's a string numeric value
        loglevel = int(loglevel)
    except ValueError:
        # If not a number, assume it's a string log level like 'DEBUG', 'INFO', etc.
        numeric_level = getattr(logging, loglevel.upper(), None)
        if isinstance(numeric_level, int):
            return numeric_level
        else:
            logging.error(f"Invalid log level string: {loglevel}")
            return logging.INFO  

    # Map numeric log levels to specific ranges
    if loglevel == 0:
        return logging.NOTSET
    elif 1 <= loglevel <= 10:
        return logging.DEBUG
    elif 11 <= loglevel <= 20:
        return logging.INFO
    elif 21 <= loglevel <= 30:
        return logging.WARNING
    elif 31 <= loglevel <= 40:
        return logging.ERROR
    elif 41 <= loglevel <= 50:
        return logging.CRITICAL
    else:
        return logging.CRITICAL 

# Setup logging configuration
def setup_logging():
    # Parse configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    loglevel = os.getenv('LOG_LEVEL', config.get('LOGGING', 'Level', fallback='INFO'))

    # loglevel to the appropriate numeric level
    numeric_level = get_log_level(loglevel)

    # setup basic logging configuration
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler() 
        ]
    )
