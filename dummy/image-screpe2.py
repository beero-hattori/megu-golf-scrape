
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import requests



# ブラウザのオプション
options = Options()
options.add_argument("--blink-settings=imagesEnabled=false")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
# options.add_argument("--headless")  # ブラウザを非表示で起動する
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--no-sandbox")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("useAutomationExtension", False)

# ブラウザ起動
service = ChromeService(executable_path="/Users/hattoriakirasatoru/Desktop/golf-scrape/dummy/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# 要素が見つかるまで10秒待つ
# driver.implicitly_wait(10)

# URLにアクセス
for page in range(1):
    time.sleep(3)
    url = f"https://www.photo-ac.com/main/search?by_ai=&q=%E3%82%B4%E3%83%AB%E3%83%95&personalized=1&qid=&creator=&ngcreator=&nq=&exclude_ai=on&srt=dlrank&orientation=all&sizesec=all&color=all&model_count=-1&age=all&mdlrlrsec=all&prprlrsec=all&qt=&p={page+1}&pt=A"
    driver.get(url)

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight*0.1);')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight*0.2);')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight*0.3);')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight*0.4);')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight*0.5);')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight*0.6);')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight*0.7);')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight*0.9);')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    images = driver.find_elements(By.TAG_NAME, "img")



    for index, img in enumerate(images):
        src = img.get_attribute('src')
        if type(src) is str and src.find("thumb.photo-ac.com") != -1:

            response = requests.get(src)
            # 画像をファイルに保存
            with open(f'./dummy/images/{page}-{index}.jpg', 'wb') as f:
                f.write(response.content)
