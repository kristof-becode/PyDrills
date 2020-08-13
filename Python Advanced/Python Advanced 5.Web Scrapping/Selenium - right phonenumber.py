from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import requests # https://requests.readthedocs.io/en/master/user/quickstart/
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import random
from random import randint

def main():
# I changed to  a diff url on the site, cause original link does not exist
    url='https://www.leboncoin.fr/informatique/1801058301.htm'
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get(url)

    #python_button = driver.find_elements_by_xpath('//div[@data-reactid="269"]')[0]
    #python_button = driver.find_element_by_xpath('*[@data-qa-id="adview_button_phone_contact"]')#[0]
    #/html/body/div[2]/div/section/main/div/div[4]/div/div[2]/div[3]/div[1]/div/div/div[3]/div/div[3]/div/div/button
    time.sleep(90)  #need to add time, otherwise he never finds the element!!!
    #time.sleep(random.uniform(1.0, 2.0))
    python_button = driver.find_element_by_xpath('//div[@data-pub-id="clicknumero" and @class="styles_button__2ps51"]')#[0]
    print(python_button)
    print("yippie")
    python_button.click()
    # And then it's like Beautiful soup
    soup = BeautifulSoup(driver.page_source, 'lxml') # this didnt mention arg "lxml" as HTMLparser but I added it after an error log
    soup

    #driver.close()

    # And then it's like Beautiful soup
    for elem in soup.find_all('a',attrs={"data-qa-id":"adview_number_phone_contact" }):
        print(elem.text)
    for elem in soup.find_all('div', attrs={"data-qa-id":"adview_description_container"}):
        print(elem.text)

    time.sleep(90)

    python_button = driver.find_element_by_link_text('Voir plus')#[0]
    python_button.click()
    # And then it's like Beautiful soup
    soup = BeautifulSoup(driver.page_source, 'lxml')
    soup
    for elem in soup.find_all('div', attrs={"data-qa-id": "adview_description_container"}):
        print(elem.text)

    driver.close()
    """
    Starting from an ad in the right place, collect all the information available to define the product being sold. Use selenium for the telephone number
    """
main()