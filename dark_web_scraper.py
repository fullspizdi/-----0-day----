```python
import requests
from bs4 import BeautifulSoup
import logging
from utils import load_config, setup_logging, validate_url

def scrape_dark_web():
    """
    Scrape the dark web market and vulnerability forum for zero-day vulnerabilities.
    """
    setup_logging()
    config = load_config()

    # URLs from the config file
    market_url = config['dark_web_market_url']
    forum_url = config['vulnerability_forum_url']

    # Validate URLs
    if not validate_url(market_url) or not validate_url(forum_url):
        logging.error("Invalid URL(s) in configuration.")
        return

    # Scrape the dark web market
    try:
        market_response = requests.get(market_url)
        market_response.raise_for_status()  # Raise an HTTPError for bad responses
        market_data = market_response.text
        logging.info("Successfully scraped the dark web market.")
    except requests.RequestException as e:
        logging.error(f"Failed to scrape the dark web market: {e}")
        return

    # Scrape the vulnerability forum
    try:
        forum_response = requests.get(forum_url)
        forum_response.raise_for_status()
        forum_data = forum_response.text
        logging.info("Successfully scraped the vulnerability forum.")
    except requests.RequestException as e:
        logging.error(f"Failed to scrape the vulnerability forum: {e}")
        return

    # Process the scraped data
    process_scraped_data(market_data, "market")
    process_scraped_data(forum_data, "forum")

def process_scraped_data(html_data, source):
    """
    Process the HTML data scraped from the dark web.

    Args:
        html_data (str): HTML content as a string.
        source (str): Source of the data ('market' or 'forum').
    """
    soup = BeautifulSoup(html_data, 'html.parser')
    if source == "market":
        items = soup.find_all('div', class_='item')
        for item in items:
            title = item.find('h2').text
            price = item.find('span', class_='price').text
            logging.info(f"Found item in market: {title} priced at {price}")
    elif source == "forum":
        posts = soup.find_all('div', class_='post')
        for post in posts:
            title = post.find('h2').text
            description = post.find('p').text
            logging.info(f"Found post in forum: {title} - {description}")

if __name__ == "__main__":
    scrape_dark_web()
```
