# scraper.py

import requests
from bs4 import BeautifulSoup
import urllib.parse
import pandas as pd
import datetime

# --- CONFIGURATION ---
# The target URL for scraping news headlines.
URL = "https://www.reuters.com/markets/"
# The base URL is used to construct absolute links from relative ones.
BASE_URL = "https://www.reuters.com"
# Headers to mimic a browser visit, which can help avoid being blocked.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# --- MODULES ---

def get_html(url, headers):
    """
    Fetches the HTML content of a given URL with robust error handling.

    :param url: The URL of the webpage to scrape.
    :type url: str
    :param headers: The HTTP headers to send with the request.
    :type headers: dict
    :return: The HTML content of the page as a string, or None if an error occurs.
    :rtype: str or None
    """
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the HTTP request: {e}")
        return None

def parse_headlines(html_content, base_url):
    """
    Parses the HTML content to extract news headlines and their corresponding links.

    :param html_content: The raw HTML of the webpage as a string.
    :type html_content: str
    :param base_url: The base URL to resolve relative links.
    :type base_url: str
    :return: A list of dictionaries, where each dictionary contains a 'headline' and a 'link'.
    :rtype: list
    """
    if not html_content:
        return []
        
    soup = BeautifulSoup(html_content, 'html.parser')
    headlines_data = []
    
    # Based on inspection of the site, headlines are contained within these specific elements.
    story_cards = soup.find_all('div', attrs={'data-testid': 'StoryCard'})

    for card in story_cards:
        link_element = card.find('a', attrs={'data-testid': 'Link'})
        if link_element:
            headline = link_element.get_text(strip=True)
            relative_link = link_element.get('href')
            
            if headline and relative_link:
                absolute_link = urllib.parse.urljoin(base_url, relative_link)
                headlines_data.append({
                    'headline': headline,
                    'link': absolute_link
                })
    return headlines_data

def save_to_csv(data_list):
    """
    Saves a list of headline data to a timestamped CSV file.

    :param data_list: A list of dictionaries with 'headline' and 'link' keys.
    :type data_list: list
    """
    if not data_list:
        print("No data to save.")
        return

    df = pd.DataFrame(data_list)
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"reuters_headlines_{today_date}.csv"

    try:
        # Save the DataFrame to a CSV file without the default index column.
        # The 'utf-8-sig' encoding helps ensure compatibility with spreadsheet software like Excel.
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"Successfully saved {len(df)} articles to '{filename}'.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    """
    Main execution block that orchestrates the scraping process.
    """
    print("Starting the news scraping process for Reuters Markets...")
    
    # Step 1: Fetch the HTML content from the URL.
    html = get_html(URL, HEADERS)
    
    if html:
        # Step 2: Parse the HTML to extract headlines.
        articles = parse_headlines(html, BASE_URL)
        
        if articles:
            # Step 3: Save the extracted data to a CSV file.
            save_to_csv(articles)
        else:
            print("Could not find any headlines to parse. The website structure may have changed.")
    else:
        print("Failed to retrieve HTML content. Halting execution.")
    
    print("Scraping process finished.")