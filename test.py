import requests
from bs4 import BeautifulSoup
import csv

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

    # Create a list to store the data
    data = []

    # Extract titles and links and append to the data list
    for book in books:
        title = book.a.attrs['title']
        link = url + book.a['href']
        data.append([title, link])

    # Specify the CSV file name
    csv_file = 'books_data.csv'

    # Write the data to the CSV file with UTF-8 encoding
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['Title', 'Link'])
        # Write data
        writer.writerows(data)

    print(f'Data has been successfully exported to {csv_file}')

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


