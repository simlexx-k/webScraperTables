import requests
from bs4 import BeautifulSoup

html_file_path = 'jumia-flash-sales.html'

# Read the HTML content from the file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find the container that holds each item
item_containers = soup.find_all('div', class_='prd card _full')

# Iterate through each item container and extract details
for item_container in item_containers:
    # Extracting item name
    item_name_element = item_container.find('h3', class_='name')
    item_name = item_name_element.text.strip() if item_name_element else "N/A"

    # Extracting current price
    current_price_element = item_container.find('span', class_='curr')
    current_price = current_price_element.text.strip() if current_price_element else "N/A"

    # Extracting old price
    old_price_element = item_container.find('span', class_='old')
    old_price = old_price_element.text.strip() if old_price_element else "N/A"

    # Extracting rating
    rating_element = item_container.find('div', class_='stars')
    rating_percentage = rating_element.find('div', class_='in')['style'] if rating_element else None
    #rating = int(rating_percentage.split(":")[1].split("%")[0].strip()) if rating_percentage else "N/A"

    #intCurrPrice = int(current_price)
    #intOldPrice = int(old_price)


    # Displaying the results for each item
    print(f"Item Name: {item_name}")
    print(f"Current Price: {current_price}")
    print(f"Old Price: {old_price}")
    #print(f"Rating: {rating}%")
    print("-" * 30)


