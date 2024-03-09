import requests
from bs4 import BeautifulSoup

def get_word_definition(word):
    # URL of the Merriam-Webster dictionary
    url = "https://www.merriam-webster.com/dictionary"
    
    # Sanitize the input and construct the complete URL
    sanitized_word = word.strip().lower().replace(" ", "-")
    url = f"{url}/{sanitized_word}"

    try:
        # Request the page
        page = requests.get(url)
        page.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)

        # Parse the HTML content
        soup = BeautifulSoup(page.content, "html.parser")

        # Find the definition
        definition = soup.find("span", class_="dtText")

        # Return the definition if found
        if definition:
            return definition.get_text(strip=True)  # Extract text content without extra whitespace
        else:
            return "Definition not found."
    except requests.RequestException as e:
        return f"Error occurred: {e}"

def main():
    # Prompt the user to enter a word
    user_word = input("Please enter a word to search: ")
    
    # Get and print the definition
    definition = get_word_definition(user_word)
    print(definition)

if __name__ == "__main__":
    main()
