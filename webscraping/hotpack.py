
# import csv
# import requests
# from bs4 import BeautifulSoup

# # Get user input for the website product link, category, and price
# product_link = input("Enter the website product link: ")
# category = input("Enter the product category: ")
# price = input("Enter the default price: ")

# # Send HTTP GET request to fetch the HTML content
# response = requests.get(product_link)
# html = response.text

# # Parse the HTML using Beautiful Soup
# soup = BeautifulSoup(html, 'html.parser')

# # Extract the product name, image URL, and modify the product name
# product_name = soup.find('h6').find('span').get_text()
# image_url = soup.find('img')['src']
# modified_product_name = product_name + "-by camairetech"

# # Create a dictionary with the data
# data = {
#     'Category': category,
#     'Product Name': modified_product_name,
#     'Price': price,
#     'Image URL': image_url
# }

# # Save the data to a CSV file
# with open('hotpack.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=data.keys())
#     writer.writeheader()
#     writer.writerow(data)

# print("Data saved successfully!")
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get the input from the user for the website URL
url = input("Enter the URL where the products are accessible: ")
category = input("Enter the product category: ")

# Send a GET request to the website
response = requests.get(url.strip())

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product boxes
product_boxes = soup.find_all('div', class_='prodBox')

# Lists to store the extracted data
product_titles = []
image_links = []
price = 1000

# Extract product information from each box
for box in product_boxes:
    image_element = box.find('img', class_='img-fluid rounded')
    h6_elements = box.find_all('h6')
    product_name = None
    
    # Find the second occurrence of the <h6> tag
    if len(h6_elements) >= 2:
        product_name = h6_elements[1].find('span').get_text()

    # Extract the text and URLs from the elements
    if product_name:
        product_titles.append(product_name)
    else:
        product_titles.append("N/A")

    if image_element:
        image_links.append(image_element['src'])
    else:
        image_links.append("N/A")

# Create a pandas DataFrame with the extracted data
data = {'Product': product_titles, 'Image Link': image_links, 'Category': category, 'Price': price}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('hotpack product.csv', index=False)

print("Data extraction and CSV creation completed successfully.")

