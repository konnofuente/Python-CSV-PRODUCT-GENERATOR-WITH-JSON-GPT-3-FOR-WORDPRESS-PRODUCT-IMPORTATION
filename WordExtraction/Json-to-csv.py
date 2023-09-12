import csv
import json
import os

# Ask for user input
category = input("Please enter a category: ")
csv_file_name = input("Please enter the name of the CSV file (without extension): ")

# Define the directory to save the CSV files
csv_dir = 'CSV'

# Read the JSON file from your local machine
with open('D:\Computer_Science\Camairetech\Project\Python-CSV-PRODUCT-GENERATOR-WITH-JSON-GPT-3-FOR-WORDPRESS-PRODUCT-IMPORTATION\WordExtraction\JSON\Pailles.json') as file:
    data = json.load(file)


# Get the array of products from the JSON data
products = data

# Check if the products list is empty
if len(products) == 0:
    print("No products found in the JSON file.")
else:
    # Get all unique keys from all products
    keys = set()
    for product in products:
        keys.update(product.keys())

    # Make sure that the directory exists, if not create it
    os.makedirs(csv_dir, exist_ok=True)

    with open(os.path.join(csv_dir, f'{csv_file_name}.csv'), 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()

        for product in products:
            # Fill missing keys with None
            for key in keys:
                product.setdefault(key, None)

            # Prepend user's category to 'categories' value only if category is not empty
            if category and 'categories' in product and isinstance(product['categories'], list):
                product['categories'] = [category] + product['categories']
                product['categories'] = ', '.join(product['categories'])

            encoded_product = {key: value.encode('unicode_escape').decode() if isinstance(value, str) else value for key, value in product.items()}
            writer.writerow(encoded_product)

    print(f"{csv_file_name}.csv file created successfully in {csv_dir} directory!")

