import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://thewire.in/"

# Send a GET request to the URL
response = requests.get(url)
html=response.text
print(html)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the article titles and URLs on the page
    articles = soup.find_all('article')

    # Extract and print the titles and URLs
    for article in articles:
        title = article.find('h2').text.strip()
        article_url = article.find('a')['href']
        print(f"Title: {title}\nURL: {article_url}\n")

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


