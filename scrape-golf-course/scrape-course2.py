import ssl

from time import time
from matplotlib.pyplot import axis
from numpy import safe_eval
from soupsieve import select
import time 
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import numpy as np



for i in range(0,5):
    for j in range(0,10):
        url = f'https://reserve.golfdigest.co.jp/course-guide/area/{i}{j}/?page=4&car=top_map'

