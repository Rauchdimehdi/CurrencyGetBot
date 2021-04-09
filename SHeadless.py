#!/Users/rauchdimehdi/Documents/Coding/WorldRemit/env python3
###########################################
## Selenium Headless #####################
############################################
# Few things to add
#     + get data for every week 
#     + lambda to store data in a dynamoDb DB 
#     + website display chart 

from selenium import webdriver
from time import sleep
import random
import smtplib
import csv
import os
from datetime import datetime

from sendmail import sendMemail
from webdriver_manager.chrome import ChromeDriverManager


ele={} # ele is a dict  {1: ' 10.75054 MAD'}
ExchangeHope = 11.0
sensitivity = 0.2

class WorldRBot():
    def __init__(self):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"

        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')

        self.currencyCheck()

    def currencyCheck(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver", options=self.options)
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.worldremit.com/en/morocco?transfer=bnk')
        sleep(5)

        
        i = 0
        while True:
            value = self.driver.find_element_by_xpath('//*[@id="country-service-info"]/div/div/div[2]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]/span').text

            Dirham = value.split("=")
            Dirham_value = float(Dirham[1].split(' ')[1])
            ele.update({i+1 : Dirham[1]})  # add current data
            i = i + 1
            sleep(3)
            print(ele) # print(value) | 1 EUR = 10.75054 MAD
            sleep(3)
            ratio = ExchangeHope - Dirham_value # r<=0: what I want r>0 : Naah
            print(f'Dirham value :{Dirham_value} \nthe ExchangeHoped by me :{ExchangeHope}\nRatio : {ratio}')
            if ratio <= 0:
                #send me an email
                subject = f"[ URGENT ] Dirham is on it's peak {Dirham_value}"
                sendMemail(Dirham_value, subject)

            elif ratio < sensitivity:
                subject = f'[ Good News ] You could take a look on the dirham value {Dirham_value}'
                sendMemail(Dirham_value, subject)

            # sleep(300) #wait till next retrieve
            # self.driver.refresh()
            # sleep(3) #wait for the next $retrive 

            # dd/mm/YY H:M:S
            now = datetime.now()
            date = now.strftime("%d/%m/%Y")
            time = now.strftime("%H:%M:%S")

            self.save_csv(Dirham_value, ExchangeHope, date, time)
    
    def save_csv(self, Dirham_value, ExchangeHope, date, time):
        path = os.getcwd()+'/data/data.csv'
        # path = '/Users/rauchdimehdi/Documents/Coding/WorldRemit/data/data.csv'

        with open(path, 'a+', newline='') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            employee_writer.writerow([Dirham_value, ExchangeHope, ExchangeHope-Dirham_value, date, time])

WorldRBot()






    
            
    
    