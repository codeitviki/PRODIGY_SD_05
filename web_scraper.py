import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Rating"])

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        rating_class = book.find("p", class_="star-rating")["class"][1]
        rating = rating_class  # One, Two, Three, Four, Five

        writer.writerow([title, price, rating])

print(" Data scraped successfully and saved to products.csv")
