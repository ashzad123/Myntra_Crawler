import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import each_prod as ipl
import download_img as idw
import cloth_category as category

def category_link(url):
    service=Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # url = 'https://www.myntra.com/'  
    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    href_store= []
    catergory_links=driver.find_elements(By.CLASS_NAME, 'desktop-categoryLink')
    for link in catergory_links:
        href=link.get_attribute('href')
        # print(href)
        href_store.append(href)

    # print(href_store)

    driver.quit()
    return href_store


if __name__ == "__main__":
    
    url="https://www.myntra.com/"
    links = category_link(url)
    # print(links)
    # print (links[0])
    # idw.image_downlaod(links[0])
    # prod_link=ipl.each_link(links[0])
    # print(prod_link)
    for i in range (7,9):
        prod_link=[]
        prod_link=ipl.each_link(links[i])
        for j in range(10):
            idw.men_image_download(prod_link[j])
    
    category.men_categorize_images()
    
    for i in range (60,65):
        prod_link=[]
        prod_link=ipl.each_link(links[i])
        for j in range(3):
            idw.women_image_download(prod_link[j])
            
    category.women_categorize_images()
    