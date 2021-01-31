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

from webdriver_manager.chrome import ChromeDriverManager



ele={}

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
        self.driver = webdriver.Chrome(executable_path="chromedriver", options=self.options)

        self.driver.get('https://www.worldremit.com/en/morocco?transfer=bnk')
        sleep(5)
        for i in range(12):
            value = self.driver.find_element_by_xpath('//*[@id="country-service-info"]/div/div/div[2]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]/span').text
            # self.driver.get_screenshot_as_file('worldremit.png')
            Dirham = value.split("=")
            ele.update({i+1 : Dirham[1]})  # add current data
            print(value)
            sleep(3) #wait till next retrieve
            self.driver.refresh()
            sleep(5) #wait for the page to refresh
            print(ele)

        for key, value in ele.items():
            print(f'{key} : {value}')

WorldRBot()






    
            
    
    