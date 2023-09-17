import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import urllib.request
import time
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation


# Get user inputs
urls = input("Enter the URLs separated by commas: ").split(',')
excel_name = input("Enter the name for the CSV file: ")
sku_prefix = input("Enter a prefix for the SKU: ")

# Initialize lists to store scraped data
product_names = []
product_descriptions = []
product_prices = []
product_skus = []
product_images = []


# Create a folder to store product images
if not os.path.exists('product_images'):
    os.makedirs('product_images')

# Loop through each URL
for url in urls:
    
    # # # Headers to include in the request
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# # # Send a GET request to the website
    response = requests.get(url, headers=headers)
    # Send a GET request to the website
    # response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        continue

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all product containers
    product_containers = soup.select('li.product.type-product')
    print(f"Number of product containers found: {len(product_containers)}")

    # Loop through each product container to extract data
    for container in product_containers:
        try:
            # Get product name, price, SKU, and image URL
            name = container.find('h2', class_='woocommerce-loop-product__title').text
            # Get product description
            description_div = container.find('div', class_='product-description')
            if description_div:
                description = description_div.find('p').text
            else:
                description = "No description available"
            price = container.find('span', class_='woocommerce-Price-amount').text
            sku = sku_prefix + container.find('a', class_='button product_type_simple add_to_cart_button ajax_add_to_cart')['data-product_sku']
            image_url = container.find('img', class_='attachment-woocommerce_thumbnail')['src']

            # Append to lists
            product_names.append(name)
            product_descriptions.append(description)
            product_prices.append(price)
            product_skus.append(sku)
            product_images.append(image_url)

            # Download the image
            image_path = f'product_images/{sku}.jpg'
            urllib.request.urlretrieve(image_url, image_path)
            
             # Simulate a delay (optional)
            time.sleep(0.5)

        except Exception as e:
            print(f"An error occurred: {e}")

# Create a DataFrame and save to CSV
df = pd.DataFrame({
    'Product Name': product_names,
    'Product Description': product_descriptions, 
    'Product Price': product_prices,
    'Product SKU': product_skus,
    'Image URL': product_images
})
df.to_excel(f'{excel_name}.xlsx', index=False)


print("Data extraction and Excel creation completed successfully.")







