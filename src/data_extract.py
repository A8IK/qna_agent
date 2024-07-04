import requests
from bs4 import BeautifulSoup

def extract_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find(id="mw-content-text").get_text()
    return content

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Bangladesh"
    content = extract_content(url)
    with open("../data/bangladesh_wikipedia_content.txt", "w", encoding="utf-8") as file:
        file.write(content)
