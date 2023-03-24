from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
import os
import pandas as pd



def packCsv(v):
    prefs = os.listdir(path=v)

    uuids = []
    addresses = []
    courseNames = []

    for prefCsv in prefs:
        prefDF = pd.read_csv(f"./{v}/{prefCsv}")
        pref = prefCsv.split(".")[0]
        courses = prefDF[pref].values
        for course in courses:  
            chrome_service = fs.Service(executable_path='./chromedriver')
            driver = webdriver.Chrome(service=chrome_service)
            sleep(1)
            try:

                driver.get(f"https://www.google.com/search?q={course}+住所+gdo")
                elements = driver.find_elements(By.TAG_NAME, "a")
                for e in elements:
                    isValue = False
                    try:
                        if isValue == False:
                            if "https://reserve.golfdigest.co.jp/golf-course/detail" in e.get_attribute("href"):                     
                                uuid=e.get_attribute("href").split("/detail/")[1]
                                if uuid not in uuids:
                                    uuids.append(uuid)
                                    sleep(2)
                                    driver.get(e.get_attribute("href"))
                                    # print(driver.find_element_by_class_name("page-detail-box"))
                                    courseName = driver.find_element(By.TAG_NAME, "h2").text
                                    print("courseName",courseName)
                                    courseNames.append(courseName)
                                    address = driver.find_element(By.CLASS_NAME, "page-detail-box")
                                    addresses.append(address.find_element(By.CLASS_NAME, "fl-l").text.split("【住所】")[1])
                                    break
                            
                    except:
                        2+2
            except:
                print(print("pref",pref))
                print("error uuid",uuid)
                print("error course",courseName)
            print("pref",pref)
            print("uuids",len(uuids))
            print("courseNames",len(courseNames))
            print("addresses",len(addresses))

        csvDF = pd.DataFrame({
                "uuid":uuids,
                "address":addresses,
                "courseName":courseNames})
        os.makedirs(f"./{v}/${pref}")
        csvDF.to_csv(f"./{v}/${pref}/total.csv")
            


# packCsv("./日本empty")
packCsv("./日本nonempty")


        # ブラウザを終了する。
        # driver.close()