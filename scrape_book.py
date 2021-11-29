"""
Task4
This module is to web scraping to find book text and get the dictionary
with words.
"""
import re
import requests
from bs4 import BeautifulSoup


def get_text_from_url(url: str) -> str:
    """Get book text from URL.
        Look for url with text book and get the text file.

    Args:
        url: url to open library to download the text book

    Returns:
         file with book text
    """
    soup_html = BeautifulSoup(requests.get(url).content, "lxml")
    url_text_book = soup_html.find(
        "a", title="Download a text version from Internet Archive"
    ).get("href")

    soup_txt = BeautifulSoup(requests.get(url_text_book).content, "lxml").text

    return soup_txt


def get_dictionary_line_of_words() -> None:
    """Get the dictionary of words and lines from book text.
        Get number of list and line of text. Split words from the line.
        Iterate on all word in line and append to dictionary.

    Returns:
         Print dictionary of words and lines
    Example:
        {
        'SEMICENTENNIAL':[4], 'almond': [4006, 15700],
        ...
        }
    """
    url_path = "https://openlibrary.org/works/OL1118938W/Pan_Tadeusz"

    words = {}

    for line_number, line_text in enumerate(get_text_from_url(url_path).split("\n")):
        for single_word in re.sub(r"[^\w]", " ", line_text).split():
            words[single_word] = words.get(single_word, []) + [line_number]

    print(words)


if __name__ == "__main__":
    get_dictionary_line_of_words()
