# import csv
# import json

# # Read the JSON file from your local machine
# with open('H:\My Drive\Client\La rosee\Web developement\code\WordExtraction\ProductJSON.json') as file:
#     data = json.load(file)

# # Get the array of products from the JSON data
# products = data

# # Check if the products list is empty
# if len(products) == 0:
#     print("No products found in the JSON file.")
# else:
#     # Get all unique keys from all products
#     keys = set()
#     for product in products:
#         keys.update(product.keys())

#     # Create a CSV file and write the data
#     with open('products.csv', 'w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=keys)
#         writer.writeheader()

#         for product in products:
#             # Fill missing keys with None
#             for key in keys:
#                 product.setdefault(key, None)

#             writer.writerow(product)

#     print("CSV file created successfully!")


# import csv
# import json

# # Read the JSON file from your local machine
# with open('H:\My Drive\Client\La rosee\Web developement\code\WordExtraction\ProductJSON.json') as file:
#     data = json.load(file)

# # Get the array of products from the JSON data
# products = data

# # Check if the products list is empty
# if len(products) == 0:
#     print("No products found in the JSON file.")
# else:
#     # Get all unique keys from all products
#     keys = set()
#     for product in products:
#         keys.update(product.keys())

#     # Create a CSV file and write the data with 'latin-1' encoding
#     with open('products4.csv', 'w', newline='', encoding='latin-1') as file:
#         writer = csv.DictWriter(file, fieldnames=keys)
#         writer.writeheader()

#         for product in products:
#             # Fill missing keys with None
#             for key in keys:
#                 product.setdefault(key, None)

#             # Decode the product values using 'latin-1' encoding
#             decoded_product = {key: value.decode('latin-1') if isinstance(value, bytes) else value for key, value in product.items()}
#             writer.writerow(decoded_product)

#     print("CSV file created successfully!")



# import csv
# import json

# # Read the JSON file from your local machine
# with open('H:\My Drive\Client\La rosee\Web developement\code\WordExtraction\ProductJSON.json') as file:
#     data = json.load(file)

# # Get the array of products from the JSON data
# products = data

# # Check if the products list is empty
# if len(products) == 0:
#     print("No products found in the JSON file.")
# else:
#     # Get all unique keys from all products
#     keys = set()
#     for product in products:
#         keys.update(product.keys())

#     # Create a CSV file and write the data with 'utf-8' encoding
#     with open('products52.csv', 'w', newline='', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames=keys)
#         writer.writeheader()

#         for product in products:
#             # Fill missing keys with None
#             for key in keys:
#                 product.setdefault(key, None)

#             # Encode the product values using unicode escape sequences
#             encoded_product = {key: value.encode('unicode_escape').decode() if isinstance(value, str) else value for key, value in product.items()}
#             writer.writerow(encoded_product)

#     print("CSV file created successfully!")


# import csv
# import json

# # Read the JSON file from your local machine
# with open('H:\My Drive\Client\La rosee\Web developement\code\WordExtraction\ProductJSON2.json') as file:
#     data = json.load(file)

# # Get the array of products from the JSON data
# products = data

# # Check if the products list is empty
# if len(products) == 0:
#     print("No products found in the JSON file.")
# else:
#     # Get all unique keys from all products
#     keys = set()
#     for product in products:
#         keys.update(product.keys())

#     # Add 'categories' column to keys
#     keys.add('categories')
#     keys.add('short_description')

#     # Create a CSV file and write the data with 'utf-8' encoding
#     with open('NewProduct03.csv', 'w', newline='', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames=keys)
#         writer.writeheader()

#         for product in products:
#             # Fill missing keys with None
#             for key in keys:
#                 product.setdefault(key, None)

#             # Modify 'categories' value based on 'material' or 'type' key
#             if 'type' in product:
#                 product['categories'] = product['material']
#             elif 'material' in product:
#                 product['categories'] = product['type']

#             # Modify 'unite package' value
#             if 'units_per_package' in product:
#                 value = product['units_per_package']
#                 product['short_description'] = f"pack de {value}"

#             # Modify 'price' value
#             if 'price' in product:
#                 price = product['price']
#                 if 'XAF' not in price:
#                     product['price'] = f"XAF {price}"

#             # Encode the product values using unicode escape sequences
#             encoded_product = {key: value.encode('unicode_escape').decode() if isinstance(value, str) else value for key, value in product.items()}
#             writer.writerow(encoded_product)

#     print("CSV file created successfully!")


# import csv
# import json

# # Read the JSON file from your local machine
# with open('H:\My Drive\Client\La rosee\Web developement\code\WordExtraction\ProductJSON3.json') as file:
#     data = json.load(file)

# # Get the array of products from the JSON data
# products = data

# # Check if the products list is empty
# if len(products) == 0:
#     print("No products found in the JSON file.")
# else:
#     # Get all unique keys from all products
#     keys = set()
#     for product in products:
#         keys.update(product.keys())

#     with open('NewProduct03.csv', 'w', newline='', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames=keys)
#         writer.writeheader()

#         for product in products:
#             # Fill missing keys with None
#             for key in keys:
#                 product.setdefault(key, None)

#             # Remove quotation marks from 'categories' value
#             if 'categories' in product and isinstance(product['categories'], list):
#                 product['categories'] = ', '.join(product['categories'])

#             encoded_product = {key: value.encode('unicode_escape').decode() if isinstance(value, str) else value for key, value in product.items()}
#             writer.writerow(encoded_product)

#     print("CSV file created successfully!")


import csv
import json

# Ask for user input
category = input("Please enter a category: ")
csv_file_name = input("Please enter the name of the CSV file (without extension): ")

# Read the JSON file from your local machine
with open('H:\My Drive\Client\La rosee\Web developement\code\Python-CSV-PRODUCT-GENERATOR-WITH-JSON-GPT-3-FOR-WORDPRESS-PRODUCT-IMPORTATION\WordExtraction\Gobelets.json') as file:
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

    with open(f'{csv_file_name}.csv', 'w', newline='', encoding='utf-8') as file:
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

    print(f"{csv_file_name}.csv file created successfully!")
