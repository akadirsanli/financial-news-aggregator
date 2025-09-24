# Financial News Headlines Scraper

## Description

This project is a Python-based web scraper designed to automatically fetch the latest financial news headlines from the markets section of Reuters. It extracts the headline text and the corresponding URL, structures the data, and saves it into a timestamped CSV file for easy access and analysis.

This script is built to be modular and robust, incorporating best practices such as error handling for network requests and clear separation of concerns.

---

## Features

- **Targeted Scraping**: Focuses specifically on the content from `reuters.com/markets`.
- **Data Structuring**: Parses raw HTML into a structured format (list of headlines and links).
- **Persistent Storage**: Saves the extracted data into a clean, timestamped `.csv` file (e.g., `reuters_headlines_2025-09-24.csv`).
- **Robust Error Handling**: Gracefully manages potential network issues and HTTP errors.
- **Modular Code**: The script is organized into distinct functions for fetching, parsing, and saving data, making it easy to read and maintain.

---

## Installation

To run this scraper on your local machine, please follow these steps.

**1. Clone the repository:**
```bash
git clone [https://github.com/akadirsanli/financial-news-aggregator.git](https://github.com/akadirsanli/financial-news-aggregator.git)
cd financial-news-aggregator
````

**2. Create and activate a virtual environment:**

  * On macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
  * On Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

**3. Install the required dependencies:**

```bash
pip install -r requirements.txt
```

-----

## Usage

Once the setup is complete, you can run the scraper with a single command:

```bash
python scraper.py
```

Upon successful execution, a new CSV file with the day's headlines will be created in the project's root directory.

-----

## Disclaimer

/This script is intended for educational purposes only. Web scraping can be demanding on server resources. Please use this script responsibly and be mindful of the terms of service of the website you are scraping. The structure of websites changes frequently, which may require updates to the parsing logic in this script./
