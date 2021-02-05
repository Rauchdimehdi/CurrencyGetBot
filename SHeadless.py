###########################################
## Selenium Headless #####################
############################################
# Few things to add
#     + add sensitivity (if value > s: send mail )
#     + lambda to store data in a dynamoDb DB 
#     + website display chart 


from selenium import webdriver
from time import sleep
import random
import smtplib

from webdriver_manager.chrome import ChromeDriverManager



ele={} # ele is a dict  {1: ' 10.75054 MAD'}
ExchangeHope = 11.0
sensitivity = 0.3

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
        self.driver.get('https://www.worldremit.com/en/morocco?transfer=bnk')
        sleep(5)

        
        i = 0
        while True:
            value = self.driver.find_element_by_xpath('//*[@id="country-service-info"]/div/div/div[2]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]/span').text

            Dirham = value.split("=")
            Dirham_value = float(Dirham[1].split(' ')[1])
            ele.update({i+1 : Dirham[1]})  # add current data
            i = i + 1
            print(ele) # print(value) | 1 EUR = 10.75054 MAD

            sleep(6) #wait till next retrieve
            self.driver.refresh()
            sleep(3) #wait for the next $retrive 

            ratio = ExchangeHope - Dirham_value # r<=0: what I want r>0 : Naah
            print(f'Dirham value :{Dirham_value} \nthe ExchangeHoped by me :{ExchangeHope}\nRatio : {ratio}')
            if ratio <= 0:
                #send me an email
                print(f"[ URGENT ] Dirham is on it's peak {Dirham_value}")
            elif ratio < sensitivity:
                print(f'[ Good News ] You could take a look on the dirham value {Dirham_value}')


WorldRBot()






    
            
    
    