from bs4 import BeautifulSoup  # noqa
import requests
import sqlite3
import pandas as pd


source = "https://books.toscrape.com/"

response = requests.get(source).text


soup = BeautifulSoup(response, "lxml")

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS books(title TEXT, price TEXT)")

for article in soup.find_all("article", class_="product_pod"):
    h3_tag = article.find("h3")

    if h3_tag:
        link = h3_tag.find("a")

    if link:
        bookName = link["title"]

    try:
        price_tag = article.find("p", class_="price_color")
        assert price_tag is not None
        price = price_tag.text
        price = price.replace("Â", "")

        cursor.execute(
            "INSERT INTO books (title, price) VALUES (?, ?)", (bookName, price)
        )

    except (AttributeError, AssertionError) as e:
        print("Can't find Data because :", e)

conn.commit()

df = pd.read_sql_query("SELECT * FROM books", conn)
df["price"] = df["price"].str.replace("£", "").str.replace("Â", "")
df.to_csv("books_data.csv", index=False)

conn.close()
