import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://books.toscrape.com/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the book titles and links on the page
    books = soup.find_all('h3')

    # Extract and print the titles and links
    for book in books:
        title = book.a.attrs['title']
        link = url + book.a['href']
        print(f"Title: {title}\nLink: {link}\n")

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


