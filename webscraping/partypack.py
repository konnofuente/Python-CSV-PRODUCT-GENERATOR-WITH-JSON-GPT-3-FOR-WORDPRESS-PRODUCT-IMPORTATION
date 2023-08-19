import csv
import requests
from bs4 import BeautifulSoup
import re

# URL of the website to scrape
url = "https://www.partypacks.co.uk/collections/birthday-balloons"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all product articles on the page
product_articles = soup.find_all("article", class_="prd-Card")

# List to store product data
products = []

# Iterate over each product article and extract the required information
for article in product_articles:
    sku = article.find("p", class_="prd-Card_Sku").text.strip()
    title = article.find("h3", class_="prd-Card_Title").text.strip()
    price = article.find("span", class_="mon-Money").text.strip()
    image_url = article.find("img", class_="rsp-Image_Image")["src"]

    # Convert price to FCFA
    match = re.search(r"£(\d+\.\d+)", price)
    if match:
        price_fcfa = float(match.group(1)) * 708.82  # Conversion rate from GBP to FCFA
        price = f"{price_fcfa:.2f} FCFA"

    # Append the product data to the list
    products.append([sku, title, price, image_url])

# Save the product data to a CSV file
filename = "product_data.csv"
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["SKU", "Title", "Price (FCFA)", "Image URL"])
    writer.writerows(products)

print(f"Product data has been saved to {filename}.")
