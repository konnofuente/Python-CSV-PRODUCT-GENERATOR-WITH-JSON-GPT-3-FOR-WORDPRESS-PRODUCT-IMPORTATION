import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from tqdm import tqdm
from openpyxl import load_workbook
from openpyxl.worksheet.datavalidation import DataValidation
from urllib.parse import quote  # Importing the quote function

def download_image(image_url, sku):
    # Encode the URL
    encoded_image_url = quote(image_url, safe=":/")
    
    image_path = f'product_images_test/{sku}.jpg'
    urllib.request.urlretrieve(encoded_image_url, image_path)  # Using encoded_image_url

def main():
    urls = input("Enter the URLs separated by commas: ").split(',')
    excel_name = input("Enter the name for the Excel file: ")
    sku_prefix = input("Enter a prefix for the SKU: ")
    
    # Initialize lists to store scraped data
    product_names = []
    product_descriptions = []
    product_prices = []
    product_skus = []
    product_images_test = []

    # Create a folder to store product images
    if not os.path.exists('product_images_test'):
        os.makedirs('product_images_test')

    # Loop through each URL
    for url in urls:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")

        if response.status_code != 200:
            print("Failed to retrieve the webpage.")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        product_containers = soup.select('li.product.type-product')
        print(f"Number of product containers found: {len(product_containers)}")

        with ThreadPoolExecutor() as executor:
            futures = []
            for container in tqdm(product_containers, desc=f"Processing {url}"):
                try:
                    name = container.find('h2', class_='woocommerce-loop-product__title').text
                    description_div = container.find('div', class_='product-description')
                    description = description_div.find('p').text if description_div else "No description available"
                    price = container.find('span', class_='woocommerce-Price-amount').text
                    sku = sku_prefix + container.find('a', class_='button product_type_simple add_to_cart_button ajax_add_to_cart')['data-product_sku']
                    image_url = container.find('img', class_='attachment-woocommerce_thumbnail')['src']

                    product_names.append(name)
                    product_descriptions.append(description)
                    product_prices.append(price)
                    product_skus.append(sku)
                    product_images_test.append(image_url)

                    futures.append(executor.submit(download_image, image_url, sku))

                except UnicodeEncodeError as uee:
                    print(f"Unicode Encode Error: {uee}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Downloading images"):
                future.result()

    df = pd.DataFrame({
        'Product Name': product_names,
        'Product Description': product_descriptions,
        'Product Price': product_prices,
        'Product SKU': product_skus,
        'Image URL': product_images_test
    })

    df.to_excel(f'{excel_name}.xlsx', index=False)


    print("Data extraction and Excel creation completed successfully.")

if __name__ == "__main__":
    main()
