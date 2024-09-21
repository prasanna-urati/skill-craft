import requests
from bs4 import BeautifulSoup
import csv

# Function to fetch the HTML content of the page
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None

# Function to parse the product data
def parse_product_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Find all product containers (you need to inspect the page's structure)
    products = soup.find_all('div', class_='product')  # Replace with actual HTML structure of the website

    product_data = []
    
    for product in products:
        try:
            # Extract product name (adjust the tag and class based on the website)
            name = product.find('h2', class_='product-title').get_text(strip=True)
            
            # Extract product price (adjust the tag and class)
            price = product.find('span', class_='product-price').get_text(strip=True)
            
            # Extract product rating (adjust the tag and class)
            rating = product.find('span', class_='product-rating').get_text(strip=True)

            # Store the extracted data in a dictionary
            product_data.append({
                'Name': name,
                'Price': price,
                'Rating': rating
            })
        except AttributeError:
            # In case some product entries are missing details, skip them
            continue

    return product_data

# Function to save data to CSV
def save_to_csv(data, filename='products.csv'):
    # Define the CSV file headers
    headers = ['Name', 'Price', 'Rating']
    
    # Open a CSV file for writing
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        # Write the header row
        writer.writeheader()
        
        # Write the product data rows
        for item in data:
            writer.writerow(item)

    print(f"Data successfully saved to {filename}")

# Main function to scrape product information from the website
def scrape_ecommerce_website():
    url = 'https://example-ecommerce-website.com'  # Replace with the actual URL of the e-commerce website
    html = get_html(url)
    
    if html:
        product_data = parse_product_data(html)
        save_to_csv(product_data)
    else:
        print("Failed to retrieve product data.")

if __name__ == "__main__":
    scrape_ecommerce_website()
