from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
import urllib.parse
import requests


def download_images(url, category):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    time.sleep(5)
    
    current_directory = os.getcwd()
    parent_directory = os.path.join(current_directory, f'{category}-Categories')
    os.makedirs(parent_directory, exist_ok=True)
    
    # Parse the URL to get the path
    parsed_url = urllib.parse.urlparse(url)
    # Extract the directory name from the URL path
    path_parts = parsed_url.path.split('/')
    dir_name = '-'.join(path_parts[2:-1])  # Join the relevant parts of the path
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
                # Generate filename based on URL and index
                image_filename = f"{dir_name}_{index + 1}.jpeg"
                # Save the image in the new directory
                with open(os.path.join(images_directory, image_filename), 'wb') as file:
                    file.write(response.content)
                print(f"Image {index + 1} downloaded: {image_url}")
            else:
                print(f"Failed to download image {index + 1}: {image_url}")

    time.sleep(5)
    driver.close()


# Example usage:
url = "https://www.myntra.com/tshirts/u.s.+polo+assn./us-polo-assn-polo-collar-pure-cotton-slim-fit-t-shirt/29338506/buy"
category = "Men"  # or "Women" depending on the category
download_images(url, category)
