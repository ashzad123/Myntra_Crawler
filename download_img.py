from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
import urllib.parse
import requests


def men_image_download(url):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    time.sleep(3)
    current_directory = os.getcwd()

    parent_directory = os.path.join(current_directory, 'Men-Categories')
    os.makedirs(parent_directory, exist_ok=True)

    # Parse the URL to get the path
    parsed_url = urllib.parse.urlparse(url)
    # Extract the directory name from the URL path
    path_parts = parsed_url.path.split('/')
    # dir_name = '-'.join(path_parts[2:-1])  # Join the relevant parts of the path

    # Find the product name from the URL
    product_name = path_parts[-3]  # Assuming the product name is the second last part of the URL

    # Create the full path for the new directory
    images_directory = os.path.join(parent_directory, product_name)
    os.makedirs(images_directory, exist_ok=True)

    image_elements = driver.find_elements(By.CLASS_NAME, "image-grid-image")
    for index, image in enumerate(image_elements):
        style_attribute = image.get_attribute('style')
        if 'background-image' in style_attribute:
            url_start = style_attribute.find('url("') + len('url("')
            url_end = style_attribute.find('")', url_start)
            image_url = style_attribute[url_start:url_end]

            # Download the image
            response = requests.get(image_url)
            if response.status_code == 200:
                # Format the filename with product name and index
                filename = f"{product_name}_{index + 1}.jpeg"
                # Save the image in the new directory
                with open(os.path.join(images_directory, filename), 'wb') as file:
                    file.write(response.content)
                print(f"Image {index + 1} downloaded: {image_url}")
            else:
                print(f"Failed to download image {index + 1}: {image_url}")

    driver.close()
    
    
def women_image_download(url):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    time.sleep(3)
    current_directory = os.getcwd()

    parent_directory = os.path.join(current_directory, 'Women-Categories')
    os.makedirs(parent_directory, exist_ok=True)

    # Parse the URL to get the path
    parsed_url = urllib.parse.urlparse(url)
    # Extract the directory name from the URL path
    path_parts = parsed_url.path.split('/')
    dir_name = '-'.join(path_parts[2:-1])  # Join the relevant parts of the path

    # Find the product name from the URL
    product_name = path_parts[-3]  # Assuming the product name is the second last part of the URL

    # Create the full path for the new directory
    images_directory = os.path.join(parent_directory, dir_name)
    os.makedirs(images_directory, exist_ok=True)

    image_elements = driver.find_elements(By.CLASS_NAME, "image-grid-image")
    for index, image in enumerate(image_elements):
        style_attribute = image.get_attribute('style')
        if 'background-image' in style_attribute:
            url_start = style_attribute.find('url("') + len('url("')
            url_end = style_attribute.find('")', url_start)
            image_url = style_attribute[url_start:url_end]

            # Download the image
            response = requests.get(image_url)
            if response.status_code == 200:
                # Format the filename with product name and index
                filename = f"{product_name}_{index + 1}.jpeg"
                # Save the image in the new directory
                with open(os.path.join(images_directory, filename), 'wb') as file:
                    file.write(response.content)
                print(f"Image {index + 1} downloaded: {image_url}")
            else:
                print(f"Failed to download image {index + 1}: {image_url}")

    driver.close()

# List of URLs
urls = [
    "https://www.myntra.com/tshirts/roadster/roadster-men-white--pure-cotton-t-shirt/2275365/buy",
    "https://www.myntra.com/tshirts/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-yellow-printed-cotton-pure-cotton-t-shirt/1700944/buy",
    "https://www.myntra.com/tshirts/urbano-fashion/urbano-fashion-men-teal-green-slim-fit-tropical-printed-pure-cotton-t-shirt/12377258/buy",
    "https://www.myntra.com/tshirts/huetrap/huetrap-men-beige--black-typography-printed-sustainable-t-shirt/11148764/buy",
    "https://www.myntra.com/tshirts/roadster/roadster-men-black-cotton-pure-cotton-t-shirt/1996777/buy"
]

# Loop through each URL and download images
for url in urls:
    men_image_download(url)
