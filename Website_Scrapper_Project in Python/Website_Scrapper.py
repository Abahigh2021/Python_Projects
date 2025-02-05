import requests 
from bs4 import BeautifulSoup


response = requests.get("https://books.toscrape.com/")


soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")

for book in books:
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    print("book titled: " + title + "has a rating of: " + rating + " starts")