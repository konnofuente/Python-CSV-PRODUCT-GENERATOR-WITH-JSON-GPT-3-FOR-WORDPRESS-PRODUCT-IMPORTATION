import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get the input from the user for multiple links
links = input("Enter the URLs (separated by comma) where the products are accessible: ").split(',')

# Lists to store the extracted data
product_titles = []
product_descriptions = []
image_links = []

# Iterate over each link provided by the user
for url in links:
    # Send a GET request to the website
    response = requests.get(url.strip())

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the product containers
    product_containers = soup.find_all('div', class_='col-md-3')

    # Extract product information from each container
    for container in product_containers:
        title_element = container.find('div', class_='product-title')
        description_element = container.find('div', class_='product-description')
        image_element = container.find('img', class_='img-responsive')

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
            image_links.append("https://www.isap-packaging.com" + image_element['src'])
        else:
            image_links.append("N/A")

# Create a pandas DataFrame with the extracted data
data = {'Title': product_titles, 'Description': product_descriptions, 'Image Link': image_links}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('products.csv', index=False)

print("Data extraction and CSV creation completed successfully.")
