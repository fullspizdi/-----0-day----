```python
import json
import logging
import os

def load_config(config_path='config.json'):
    """
    Load the configuration file.
    
    Args:
        config_path (str): Path to the configuration file.
    
    Returns:
        dict: Configuration settings.
    """
    if not os.path.exists(config_path):
        logging.error(f"Configuration file not found at {config_path}")
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    return config

def setup_logging():
    """
    Setup basic logging configuration.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_url(url):
    """
    Validate the format of a URL.
    
    Args:
        url (str): The URL to validate.
    
    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:\S+(?::\S*)?@)?'  # user and password
        r'(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,6}'  # domain...
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def hash_string(input_string):
    """
    Generate a hash for the given string using SHA-256.
    
    Args:
        input_string (str): The string to hash.
    
    Returns:
        str: The resulting SHA-256 hash.
    """
    import hashlib
    return hashlib.sha256(input_string.encode()).hexdigest()
```
