import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

BASE_URL = "http://books.toscrape.com/"

def get_soup(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching {url}")
        return None
    # Use the built-in html.parser instead of lxml
    return BeautifulSoup(response.text, "html.parser")

def scrape_books():
    books = []
    page_url = BASE_URL  # Start with the homepage

    while page_url:
        print(f"Scraping: {page_url}")
        soup = get_soup(page_url)
        if soup is None:
            break

        # Extract all book containers on the page
        articles = soup.find_all("article", class_="product_pod")
        for article in articles:
            title = article.h3.a["title"]
            price = article.find("p", class_="price_color").text.strip()
            # Rating is encoded in class names (e.g., "star-rating Three")
            rating_class = article.find("p", class_="star-rating")["class"]
            # Remove 'star-rating' and take the rating word
            rating = [r for r in rating_class if r != "star-rating"][0]
            availability = article.find("p", class_="instock availability").text.strip()
            books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability
            })

        # Find the "next" button and build the next page URL
        next_li = soup.find("li", class_="next")
        if next_li:
            next_link = next_li.find("a")["href"]
            # Use urljoin to handle relative URLs correctly
            page_url = urljoin(page_url, next_link)
        else:
            page_url = None  # No more pages

    return books

def save_to_csv(data, filename="raw_books.csv"):
    if not data:
        print("No data to save.")
        return

    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    books_data = scrape_books()
    if books_data:
        save_to_csv(books_data)