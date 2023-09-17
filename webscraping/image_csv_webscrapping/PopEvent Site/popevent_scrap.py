import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import urllib.request

# Create a folder to store product images
if not os.path.exists('product_images'):
    os.makedirs('product_images')

# Initialize lists to store scraped data
product_names = []
product_prices = []
product_skus = []
product_images = []

# URL of the website to scrape
url = 'https://boutique.popevents.nc/categorie-produit/ballons/ballons-aluminium/anniversaire/'

# # Headers to include in the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# # Send a GET request to the website
response = requests.get(url, headers=headers)
print(f"Status Code: {response.status_code}")

# Check if the request was successful
if response.status_code != 200:
    print("Failed to retrieve the webpage.")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Write the entire HTML content to a file for inspection
with open("output.html", "w", encoding='utf-8') as f:
    f.write(str(soup))

# Find all product containers using CSS selector
product_containers = soup.select('li.product.type-product')
print(f"Number of product containers found: {len(product_containers)}")

# Loop through each product container to extract data
for container in product_containers:
    try:
        # Get product name
        name = container.find('h2', class_='woocommerce-loop-product__title').text
        product_names.append(name)
        print(f"Extracted Name: {name}")

        # Get product price
        price = container.find('span', class_='woocommerce-Price-amount').text
        product_prices.append(price)
        print(f"Extracted Price: {price}")

        # Get or generate product SKU
        sku = container.find('a', class_='button product_type_simple add_to_cart_button ajax_add_to_cart')['data-product_sku']
        product_skus.append(sku)
        print(f"Extracted SKU: {sku}")

        # Get product image URL
        image_url = container.find('img', class_='attachment-woocommerce_thumbnail')['src']
        product_images.append(image_url)
        print(f"Extracted Image URL: {image_url}")

        # Download the image and save it in the 'product_images' folder
        image_path = f'product_images/{sku}.jpg'
        urllib.request.urlretrieve(image_url, image_path)
        print(f"Downloaded image for SKU: {sku}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Create a DataFrame to store the scraped data
df = pd.DataFrame({
    'Product Name': product_names,
    'Product Price': product_prices,
    'Product SKU': product_skus,
    'Image URL': product_images
})

# Save the DataFrame to a CSV file
df.to_csv('products.csv', index=False)

print("Data extraction and CSV creation completed successfully.")















# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import os
# import urllib.request

# # Create a folder to store product images
# if not os.path.exists('product_images'):
#     os.makedirs('product_images')

# # Initialize lists to store scraped data
# product_names = []
# product_prices = []
# product_skus = []
# product_images = []

# # URL of the website to scrape
# url = 'https://boutique.popevents.nc/categorie-produit/decoration-generale/ballons-et-accessoires/ballons-ballons-et-accessoires/'  # Replace with the actual URL

# # Headers to include in the request
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# # Send a GET request to the website
# response = requests.get(url, headers=headers)
# print(f"Status Code: {response.status_code}")  # Should print 200 if successful

# # Check if the request was successful
# if response.status_code != 200:
#     print("Failed to retrieve the webpage.")
#     exit()

# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all product containers
# product_containers = soup.find_all('li', class_='product type-product')
# print(f"Number of product containers found: {len(product_containers)}")

# # Loop through each product container to extract data
# for container in product_containers:
#     try:
#         # Get product name
#         name = container.find('h2', class_='woocommerce-loop-product__title').text
#         product_names.append(name)
#         print(f"Extracted Name: {name}")

#         # Get product price
#         price = container.find('span', class_='woocommerce-Price-amount').text
#         product_prices.append(price)
#         print(f"Extracted Price: {price}")

#         # Get or generate product SKU
#         sku = container.find('a', class_='button product_type_simple add_to_cart_button ajax_add_to_cart')['data-product_sku']
#         product_skus.append(sku)
#         print(f"Extracted SKU: {sku}")

#         # Get product image URL
#         image_url = container.find('img', class_='attachment-woocommerce_thumbnail')['src']
#         product_images.append(image_url)
#         print(f"Extracted Image URL: {image_url}")

#         # Download the image and save it in the 'product_images' folder
#         urllib.request.urlretrieve(image_url, f'product_images/{sku}.jpg')
#         print(f"Downloaded image for SKU: {sku}")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Create a DataFrame to store the scraped data
# df = pd.DataFrame({
#     'Product Name': product_names,
#     'Product Price': product_prices,
#     'Product SKU': product_skus,
#     'Image URL': product_images
# })

# # Save the DataFrame to a CSV file
# df.to_csv('products.csv', index=False)

# print("Data extraction and CSV creation completed successfully.")
