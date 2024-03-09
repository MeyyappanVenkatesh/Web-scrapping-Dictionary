# Word Definition Finder

This Python script allows users to retrieve the definition of a word from the Merriam-Webster dictionary website.

## Prerequisites

- Python 3.x installed on your system.
- Installation of required libraries: `requests` and `beautifulsoup4`.
  ```bash
  pip install requests beautifulsoup4
## Usage

1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script `Webscrapping Dictionary.py` using Python:
4. Follow the prompts to enter the word you want to search for.
5. The script will fetch the definition of the word from the Merriam-Webster website and display it on the console.

## How It Works

- The script utilizes the `requests` library to send an HTTP request to the Merriam-Webster website, requesting the definition of the entered word.
- It parses the HTML content of the response using the `BeautifulSoup` library to extract the definition from the webpage's DOM (Document Object Model).
- If the word is found in the dictionary, the script prints its definition. If not, it notifies the user that the definition is not available.

## Note

- This script relies on web scraping techniques to extract information from the Merriam-Webster website. Use it responsibly and be mindful of the website's terms of service.
- The accuracy of the definition retrieved depends on the website's content and structure, which may change over time.


