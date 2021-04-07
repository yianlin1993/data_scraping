from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv

f = open('WiserAdvisor.csv', 'a')
browser = webdriver.Chrome()
#f.write('Name, URL, Company, Fee, phone, Zip, Address')
f.write('\n')

browser.get('https://www.wiseradvisor.com/financial-advisors.asp')

a = 1
while browser.find_element(By.XPATH, '/html/body/section/div/div/div[2]/ul[1]/li[%d]/a' %a).text != "":
    state = browser.find_element(By.XPATH, '/html/body/section/div/div/div[2]/ul[1]/li[%d]/a' %a)
    print(state.text)
    state.send_keys(Keys.RETURN)

    i = 1
    try:
        Name = browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div[4]/div[%d]/div[1]/span/div/div/div[2]/a/h3' %i)
        while Name.text != "":
        #while browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div[4]/div[%d]/div[1]/span/div/div/div[2]/a/h3' %i):
        #print(i)
            Name = browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div[4]/div[%d]/div[1]/span/div/div/div[2]/a/h3' %i)
            print(Name.text)
            f.write(Name.text)
            f.write('\t')
            URL = browser.find_element(By.XPATH,'/html/body/section[2]/div/div/div[1]/div[4]/div[%d]/div[1]/span/div/div/div[2]/a' %i).get_attribute('href')
            print(URL)
            f.write(URL)
            f.write('\t')
            company = browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div[4]/div[%d]/div[1]/span/div/div/div[2]/a/span/b' %i)
            print(company.text)
            f.write(company.text)
            f.write('\t')
        #Qualification = browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div[4]/div[%d]/div[1]/span/div/div/div[4]/div/p[1]' %i)
        #print(Qualification.text)
        #f.write(Qualification.text)
        #f.write('\t')
            Fee = browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div[4]/div[%d]/div[1]/span/div/div/div[4]/div/p[2]/span' %i)
            print(Fee.text)
            f.write(Fee.text)
            f.write('\t')
            if Fee == None:
                phone = browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div[4]/div[%d]/div[1]/span/div/div/div[4]/div/p[2]/span[2]' %i)
            else:
                phone = browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div[4]/div[%d]/div[1]/span/div/div/div[4]/div/p[3]/span[2]' %i)
                print(phone.text)
                f.write(phone.text)
                f.write('\t')
                Zip = browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div[4]/div[%d]/div[1]/span/div/div/div[4]/div/p[3]/span[1]/span[3]' %i)
            print(Zip.text)
            f.write(Zip.text)
            f.write('\t')
            Address = browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div[4]/div[%d]/div[1]/span/div/div/div[4]/div/p[3]/span[1]' %i)
            print(Address.text)
            f.write(Address.text)
            f.write('\n')
            i += 1
    except NoSuchElementException:
        pass
    a += 1
    browser.get('https://www.wiseradvisor.com/financial-advisors.asp')

f.close()
browser.quit()
