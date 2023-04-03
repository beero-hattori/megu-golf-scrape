import time
from numpy import safe_eval
from soupsieve import select
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import uuid
import datetime

dt = datetime.datetime.now()
ts = datetime.datetime.timestamp(dt)


tieDf = pd.read_csv('./scrape-golf-course/tie.csv')
course_layout_ids = []


for v in tieDf["golf_course_id"].values:
    course_layout_id = str(uuid.uuid4())
    course_layout_ids.append(course_layout_id)

tieDf["course_layout_id"] = course_layout_ids
tieDf["created_at"]        = int(ts)
tieDf["updated_at"]        = int(ts)

print(tieDf.head(5))

tieDf.to_csv('./scrape-golf-course/tie.csv',index=False)
