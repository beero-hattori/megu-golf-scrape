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
import requests



options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');


DRIVER_PATH = '/Users/hattori/Desktop/Selenium/chromedriver'
chrome_service = fs.Service(executable_path=DRIVER_PATH) 
driver = webdriver.Chrome(service=chrome_service)


url = 'https://hcp.jga.or.jp/ratings/search'
driver.get(url)
time.sleep(3)
select_elements = driver.find_elements(By.TAG_NAME,'select')
select_element = select_elements[1]
select = Select(select_element)

options = select.options

element = driver.find_element(By.NAME,'searchButton')
        # # エラー発生
element.click()


    # ここはページ総数でいい
for j in range(1,48):
    if j == 0:
        continue
    else:
        url = 'https://hcp.jga.or.jp/ratings/search'
        driver.get(url)
        
        time.sleep(1)
        select_elements = driver.find_elements(By.TAG_NAME,'select')
        select_element = select_elements[1]
        select = Select(select_element)

        options = select.options

        array3 = []
        titleArray3 = []

        index = j

        femaleArray3 = []

        dfs3 = []

        removeArray3 = []

        female_dfs3 = []

        optionTitle = options[index].text
            
        select.select_by_index(index)

        element = driver.find_element(By.NAME,'searchButton')
                # # エラー発生
        element.click()
        time.sleep(1)
        try:
            pageNo = driver.find_element(By.CLASS_NAME,"pageNo").text
            totalPages = int(pageNo.split("/")[1])
            
        except:
            totalPages = 1

        for i in range(0,totalPages):
            aTags = driver.find_elements(By.TAG_NAME,'a')
            for a in aTags:
                href = a.get_attribute("href")
                isResult = href.find(":table:searchResult:")
                if isResult !=-1:
                    titleArray3.append(a.text)
                    array3.append(href)
                            # a.click()
            if i == totalPages-1:
                break
            else:
                driver.find_element(By.LINK_TEXT,"次へ").click()
                time.sleep(3)


        for i in range(0,len(array3)):
                # 問題あり
            driver.get(array3[i])
            time.sleep(3)
            page_title = titleArray3[i]
            print("page_title inside range(0,len(array3))",page_title)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            tables = soup.find_all('table')    
            try:
                df_table = pd.read_html(str(tables))
                dfs3.append(df_table[1])
                df_table[1].set_axis([page_title if i == 0 else '' for i in range(0,len(df_table[1]))], axis="index", inplace=True)
                genders = driver.find_elements(By.TAG_NAME,'a')
                for g in genders:
                    href = g.get_attribute("href")
                    if href != None:
                        isResult = href.find(":female")
                        if isResult !=-1:
                            femaleArray3.append(href)
            except IndexError:
                removeArray3.append(page_title)
                print("no index")



        pd.concat([pd.DataFrame(v) for v in dfs3 ]).to_csv(f'./{optionTitle}-male.csv')
            
        for i in removeArray3:
            print(f'titleArray',i)
            titleArray3.remove(i)

        # ここまで以上なし
        print(f"titleArray{len(titleArray3)}",titleArray3)
        
        for i in range(0,len(titleArray3)):
            try:
                driver.get(femaleArray3[i])
                time.sleep(3)
                page_title = titleArray3[i]
                print("page_title inside  range(0,len(titleArray)):",page_title)
                soup = BeautifulSoup(driver.page_source, 'lxml')
                tables = soup.find_all('table')    
                df_table = pd.read_html(str(tables))
                female_dfs3.append(df_table[1])
                df_table[1].set_axis([page_title if i == 0 else '' for i in range(0,len(df_table[1]))], axis="index", inplace=True)
            except IndexError:
                    print("no index")


        pd.concat([pd.DataFrame(v) for v in female_dfs3 ]).to_csv(f'./{optionTitle}-female.csv')


