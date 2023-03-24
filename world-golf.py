from pprint import pprint
from time import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.support.select import Select
from soupsieve import select
import time 
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
import os


options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');


DRIVER_PATH = '/Users/hattori/Desktop/selenium2/chromedriver'
chrome_service = fs.Service(executable_path=DRIVER_PATH) 
driver = webdriver.Chrome(service=chrome_service)



url = 'https://ncrdb.usga.org/'
driver.get(url)



# ddCountriesOptions = ddCountries.options
ddCountriesSelect = driver.find_element(By.ID,'ddCountries')
select = Select(ddCountriesSelect)
options = select.options

countries = []

for i,option in enumerate(options):
        url = 'https://ncrdb.usga.org/'
        driver.get(url)
        time.sleep(3)
        ddCountriesSelect = driver.find_element(By.ID,'ddCountries')
        select = Select(ddCountriesSelect)
        options = select.options
        arrays = []
        if i==0:
                continue
        else:
                countryTitle = options[i].text
                print("countryTitle",countryTitle)
                select.select_by_index(i)
                ddStateSelect = Select(driver.find_element(By.ID,'ddState'))
                ddStateOptions = ddStateSelect.options
                time.sleep(3)


                
                for j,ddStateOption in enumerate(ddStateOptions):
                        if j == 0:
                                continue
                        else:
                                ddStateSelect = Select(driver.find_element(By.ID,'ddState'))
                                ddStateOptions = ddStateSelect.options
                                stateTables = []
                                print('stateTables',stateTables)
                                
                                try:
                                    stateTitle = ddStateOptions[j].text
                                    print("stateTitle",stateTitle)
                                    ddStateSelect.select_by_index(j)
                                    driver.find_element(By.ID,'myButton').click()
                                    time.sleep(3)

                                    aTags = driver.find_elements(By.TAG_NAME,'a')
                                    for a in aTags:
                                            href = a.get_attribute("href")
                                            isResult = href.find("courseTeeInfo.aspx?CourseID")
                                            
                                            if isResult !=-1:
                                                    time.sleep(3)

                                                    dfs = pd.read_html(href)

                                                    try:
                                                            
                                                            dfs[1].set_axis([a.text if i == 0 else '' for i in range(0,len(dfs[1]))], axis="index", inplace=True)
                                                            print("dfs[1]",dfs[1])
                                                            stateTables.append(dfs[1])
                                                    except:
                                                            print("nothing")
                                    try:
                                        
                                        pd.concat([v for v in stateTables ]).to_csv(f'./{countryTitle}/{stateTitle}.csv')
                                        print("no csv")
                                    except FileNotFoundError:
                                            os.mkdir(f'./{countryTitle}/')
                                            pd.concat([v for v in stateTables ]).to_csv(f'./{countryTitle}/{stateTitle}.csv')
                                except:
                                    break   

