from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


# service=Service(executable_path="chromedriver.exe")
#cldriver_path = "C:\Users\ASHZAD KAMAL\Downloads\chromedriver.exe"
# driver = webdriver.Chrome(service=service)


def each_link(url):
    service=Service(executable_path="chromedriver.exe") 
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    time.sleep(3) 
    filtered_links=[]
    href_links=[]
    elements = driver.find_elements(By.CSS_SELECTOR, 'a[href]')
    href_links = [element.get_attribute('href') for element in elements]
    filtered_links.extend([link for link in href_links if '/buy' in link])

    # Print the stored href links
    # for link in filtered_links:
    #     print(link)
        
    # print(len(urls))
    # Close the browser
    driver.quit()
    return filtered_links
    
    
# url='https://www.myntra.com/men-tshirts'
# each_link(url)