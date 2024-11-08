import logging
import configparser
import os

def get_log_level(loglevel):
    if loglevel is None:
        return None

    try:
        level = int(loglevel)
        if level <= 10:
            return logging.DEBUG
        elif level <= 20:
            return logging.INFO
        elif level <= 30:
            return logging.WARNING
        elif level <= 40:
            return logging.ERROR
        else:
            return logging.CRITICAL
    except ValueError:
        return getattr(logging, loglevel.upper(), logging.DEBUG)

def parse_levels(levels_str):
    levels = []
    for level in levels_str.split(','):
        level = level.strip()
        numeric_level = get_log_level(level)
        if numeric_level is not None:
            levels.append(numeric_level)
    return levels if levels else [logging.DEBUG]  

class MultiLevelFilter(logging.Filter):
    def __init__(self, levels):
        self.levels = levels

    def filter(self, record):
        return record.levelno in self.levels

def setup_logging():
    # check for environment variables
    env_levels = os.getenv('LOG_LEVELS') 
    env_level = os.getenv('LOG_LEVEL')    

    if env_levels is not None:
        log_levels = parse_levels(env_levels)
        print(f"Using multiple log levels from environment variable: {env_levels}")
    elif env_level is not None:
        log_levels = [get_log_level(env_level)]
        print(f"Using single log level from environment variable: {env_level}")
    else:
        # If environment variables are not set, check config.ini
        config = configparser.ConfigParser()
        config_path = 'config.ini'
        
        if os.path.exists(config_path):
            config.read(config_path)
            # Try to get multiple levels first 
            config_levels = config.get('LOGGING', 'Levels', fallback=None)
            if config_levels is not None:
                log_levels = parse_levels(config_levels)
                print(f"Using multiple log levels from config.ini: {config_levels}")
            else:
                # show the single level
                config_level = config.get('LOGGING', 'Level', fallback='10')
                log_levels = [get_log_level(config_level)]
                print(f"Using single log level from config.ini: {config_level}")
        else:
            log_levels = [logging.DEBUG]  
            print("config.ini not found, defaulting to DEBUG level.")

    # Remove all handlers
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)

    console_handler = logging.StreamHandler()
    # formatter = logging.Formatter('%(message)s')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    level_filter = MultiLevelFilter(log_levels)
    console_handler.addFilter(level_filter)

    root.setLevel(min(log_levels))  
    root.addHandler(console_handler)
    
    

    
# # Different formatter examples:

# basic_formatter = logging.Formatter('%(message)s')
# # Output: Hello World

# detailed_formatter = logging.Formatter('%(levelname)s: %(message)s')
# # Output: INFO: Hello World

# full_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# summary_
# Output: 2024-10-10 14:30:45 - INFO - Hello World