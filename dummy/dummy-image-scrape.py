import sys
import requests
from bs4 import BeautifulSoup
import time




url = 'https://www.photo-ac.com/main/search?by_ai=&q=%E3%82%B4%E3%83%AB%E3%83%95&personalized=1&qid=&creator=&ngcreator=&nq=&exclude_ai=on&srt=dlrank&orientation=all&sizesec=all&color=all&model_count=-1&age=all&mdlrlrsec=all&prprlrsec=all&qt=&pt=A&p=120'
res = requests.get(url)


soup = BeautifulSoup(res.text, "html.parser")


images = soup.find_all('img')

for i,image in enumerate(images):
    # time.sleep(3)
    id = image.attrs.get("id")
    src = image.attrs.get("src")
    print(i,src)
    # if type(id) is str:
    #     if id.find("jq_thumb_") != -1:
    #         if src.find("no_image_lazy_load") == -1:
    #             print(i,src)


    
        
        



# # for page in range(129):
# #     url = f"https://www.photo-ac.com/main/search?by_ai=&q=%E3%82%B4%E3%83%AB%E3%83%95&personalized=1&qid=&creator=&ngcreator=&nq=&exclude_ai=on&srt=dlrank&orientation=all&sizesec=all&color=all&model_count=-1&age=all&mdlrlrsec=all&prprlrsec=all&qt=&p={page+1}&pt=A"
# #     print(page,url)




