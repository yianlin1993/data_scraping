#Python3
###Objective
#This script is designed to collect a list of Financial Advisor information using Python and Selenium. The information of the Financial Advisor in each state is on the website (https://www.paladinregistry.com/find/search-for-local-financial-advisors).

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
import time


f = open('Paladin.csv', 'a')
browser = webdriver.Chrome()
f.write('\n')

### Steps ###
#Navigate to https://www.paladinregistry.com/find/search-for-local-financial-advisors
#Click each the hyper link of each state.
#Collect the infomation of every listed financial advisor in each state.

browser.get('https://www.paladinregistry.com/find/search-for-local-financial-advisors')

a = 2
try:
    state = browser.find_element(By.XPATH, '/html/body/header/div[6]/div/ul[1]/li[%d]/a' %a)
    while state.text != "":
        print(state.text)
        state.send_keys(Keys.RETURN)
        time.sleep(5)
        try:
            cross = browser.find_element(By.XPATH, '//*[@id="myModal"]/div/div/div[1]/button/span')
            print(cross.text)
            if cross.text == "×":
                cross.click()
        except NoSuchElementException:
            pass
        i = 1
        try:
            Name = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[%d]/div/div[2]/h3/a' %i)
            while Name.text != "":
                Name = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[%d]/div/div[2]/h3/a' %i)
                print(Name.text)
                f.write(Name.text)
                f.write('\t')
                URL = browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[%d]/div/div[2]/h3/a' %i).get_attribute('href')
                print(URL)
                f.write(URL)
                f.write('\t')
                company = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[%d]/div/div[2]/h5/a' %i)
                print(company.text)
                f.write(company.text)
                f.write('\t')
                
                try:
                    phone = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[%d]/div/div[2]/div[4]/a[1]/div' %i).get_attribute('innerText')
                    print(phone)
                    f.write(phone)
                except NoSuchElementException:
                    phone = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[%d]/div/div[2]/div[3]/a[1]/div' %i).get_attribute('innerText')
                    print(phone)
                    f.write(phone)
                f.write('\t')
                try:
                    city = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[%d]/div/div[2]/div[4]/div/span' %i)
                    print(city.text)
                    f.write(city.text)
                except NoSuchElementException:
                    city = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[%d]/div/div[2]/div[3]/div/span' %i)
                    print(city.text)
                    f.write(city.text)
                f.write('\n')
                i += 1
        except NoSuchElementException:
            pass
        a += 1
        browser.get('https://www.paladinregistry.com/find/search-for-local-financial-advisors')
        state = browser.find_element(By.XPATH, '/html/body/header/div[6]/div/ul[1]/li[%d]/a' %a)
except NoSuchElementException:
    pass

f.close()
browser.quit()
