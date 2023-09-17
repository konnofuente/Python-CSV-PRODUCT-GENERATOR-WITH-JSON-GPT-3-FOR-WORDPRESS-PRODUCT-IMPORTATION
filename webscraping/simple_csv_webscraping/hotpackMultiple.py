import requests
from bs4 import BeautifulSoup
import pandas as pd
import os.path

# Get the input from the user for multiple website URLs and a single category
urls = input("Enter the URLs where the products are accessible (separated by comma): ").split(",")
category = input("Enter the product category: ")
price = input("enter price: ")

# Define the CSV file path
csv_file_path = os.path.join(os.path.dirname(__file__), 'hotpack_products.csv')


if os.path.isfile(csv_file_path):
    # Load the existing CSV file into a DataFrame
    df_existing = pd.read_csv(csv_file_path)

    # Append the existing data to the respective lists
    product_titles = df_existing['Product'].tolist()
    image_links = df_existing['Image Link'].tolist()
    category_list = df_existing['Category'].tolist()

else:
    # Create empty lists to store the extracted data
    product_titles = []
    image_links = []
    category_list = []

# Iterate over the URLs
for url in urls:
    # Send a GET request to the website
    response = requests.get(url.strip())

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the product boxes
    product_boxes = soup.find_all('div', class_='prodBox')

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

        category_list.append(category)

# Create a pandas DataFrame with the extracted data
data = {'Product': product_titles, 'Image Link': image_links, 'Category': category_list,'Price':price}
df = pd.DataFrame(data)

if os.path.isfile(csv_file_path):
    df = pd.concat([df_existing, df])

# # Save the DataFrame to a CSV file
# df.to_csv('hotpack_products.csv', index=False)

# Save the DataFrame to the CSV file
df.to_csv(csv_file_path, index=False)

print("Data extraction and CSV creation completed successfully.")
