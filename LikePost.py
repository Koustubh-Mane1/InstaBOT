import os
import csv
import time
import wget
import xlsxwriter
import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from termcolor import colored
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import random
chromedriver_path = '/usr/local/bin/chromedriver' # Change this to your own chromedriver path!
browser = webdriver.Chrome('chromedriver')
s=Service('Chromedriver PATH')
browser.get('https://www.instagram.com/')
excel_file_path = 'User_List.xlsx'  # Replace with the actual path to your Excel file

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)
users = df.iloc[:, 0].tolist()
messages = df.iloc[:, 1].tolist()
actions = ActionChains(browser)
try:
# accept cookies
    accept_cookies=browser.find_element_by_xpath('//button[text()="Accept"]')
    accept_cookies.click()
    time.sleep(1)
except:
    pass


def auth(username, password):
    try:

        browser.get('https://instagram.com')
        time.sleep(random.randrange(2, 4))
        # Entering username ,password
        input_username = browser.find_element(By.NAME, 'username')
        input_password = browser.find_element(By.NAME, 'password')

        input_username.send_keys('elements5493')
        time.sleep(random.randrange(1, 2))
        input_password.send_keys('koustubh')
        time.sleep(random.randrange(1, 2))
        # Logging in
        input_password.send_keys(Keys.ENTER)
        time.sleep(random.randrange(3, 5))


    except Exception as err:
        print("Did not log in")
        browser.quit()

auth("","")
# Cookies
try:
    not_now_1=browser.find_element_by_xpath('//button[text()="Not Now"]')
    not_now_1.click()
    time.sleep(2)
except:
    pass

# Notifications
try:
    not_now_2=browser.find_element_by_xpath('//button[text()="Not Now"]')
    not_now_2.click()
    time.sleep(2)
except:
    pass

# Input after Login
profile_name =['koustubh']
time.sleep(random.randrange(3,4))
browser.find_element(By.XPATH,'//div[@//div[@class="_ab6-"]').click()
time.sleep(random.randrange(3,4))
try:
    not_now_2=browser.find_element_by_xpath('//button[text()="Not Now"]')
    not_now_2.click()
    time.sleep(2)
except:
    pass
browser.find_element(By.XPATH,'//div[@class = "xt0psk2"]').click()
time.sleep(random.randrange(8,10))
browser.find_element_by_xpath('//div[text()="Message"]').click()
time.sleep(random.randrange(7,9))

for user,message in zip(users,messages):
    browser.find_element(By.XPATH,'//div[@class = "x6s0dn4 x78zum5 xdt5ytf xl56j7k"]').click()
    time.sleep(random.randrange(3,4))
    browser.find_element(By.NAME,'queryBox').send_keys(user)
    time.sleep(random.randrange(8,10))

