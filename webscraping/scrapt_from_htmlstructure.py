import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import urllib

# Prompt the user for information about the website and product details
url = input("Enter the URL of the website: ")
product_name_tag = input("Enter the HTML tag for the product name: ")
description_tag = input("Enter the HTML tag for the product description: ")
image_tag = input("Enter the HTML tag for the product image: ")
product_category_tag = input("Enter the HTML tag for the product category: ")
short_description_tag = input("Enter the HTML tag for the product short description: ")
price_tag = input("Enter the HTML tag for the product price: ")
currency = input("Enter the desired currency code (e.g., USD, EUR): ")

# Send a GET request to the website
# response = requests.get(url)
response = requests.get(url, timeout=10)  # Increase the timeout value as needed


# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product containers
product_containers = soup.find_all('div', class_='col-md-3')

# Lists to store the extracted data
product_titles = []
product_descriptions = []
image_links = []
product_categories = []
short_descriptions = []
prices = []

# Extract product information from each container
for container in product_containers:
    title_element = container.find(product_name_tag)
    description_element = container.find(description_tag)
    image_element = container.find(image_tag)
    category_element = container.find(product_category_tag)
    short_description_element = container.find(short_description_tag)
    price_element = container.find(price_tag)

    # Extract the text from the elements
    if title_element:
        product_titles.append(title_element.get_text(strip=True))
    else:
        product_titles.append("N/A")
        
    if description_element:
        product_descriptions.append(description_element.get_text(strip=True))
    else:
        product_descriptions.append("N/A")
        
    if image_element:
        image_links.append(image_element['src'])
    else:
        image_links.append("N/A")
        
    if category_element:
        product_categories.append(category_element.get_text(strip=True))
    else:
        product_categories.append("N/A")
        
    if short_description_element:
        short_descriptions.append(short_description_element.get_text(strip=True))
    else:
        short_descriptions.append("N/A")
        
    if price_element:
        prices.append(price_element.get_text(strip=True))
    else:
        prices.append("N/A")

# Convert prices if the desired currency is not FCFA
if currency != "FCFA":
    # Use an external API to convert the prices to the desired currency
    conversion_url = f"https://api.exchangerate-api.com/v4/latest/USD"
    conversion_response = requests.get(conversion_url)
    conversion_data = json.loads(conversion_response.content)

    # Extract the desired currency rate
    desired_currency_rate = conversion_data["rates"][currency]

    # Convert the prices to the desired currency
    converted_prices = [round(float(price) * desired_currency_rate, 2) if price != "N/A" else "N/A" for price in prices]
else:
    converted_prices = prices

# Create a pandas DataFrame with the extracted data
data = {
    'Product Name': product_titles,
    'Description': product_descriptions,
    'Image': image_links,
    'Product Category': product_categories,
    'Short Description': short_descriptions,
    'Price': converted_prices
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
# df.to_csv('.csv', index=False)

csv_filename = url.split("/")[-1].split("?")[0] + ".csv"

# Save the DataFrame to a CSV file
df.to_csv(csv_filename, index=False)

print("Data extraction and CSV creation completed successfully.")
