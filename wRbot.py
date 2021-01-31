from selenium import webdriver
from time import sleep
import random


ele={}

class WorldRBot():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def login(self):
        self.driver.get('https://www.worldremit.com/en/morocco?transfer=bnk')
  
    def show(self):
        for i in range(12):
            value = self.driver.find_element_by_xpath('//*[@id="BNK"]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/span').text
            Dirham = value.split("=")
            ele.update({i+1 : Dirham[1]})  # add current data
            print(value)
            sleep(3) #wait till next retrieve
            self.driver.refresh()
            sleep(5) #wait for the page to refresh
            
    
    