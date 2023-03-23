from playsound import playsound
import getpass
import keyring
import subprocess
import time as tt
import pyttsx3
import os 
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
def srap_from_flipkart(url_to_enter):
    url = url_to_enter
    headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15",
            "Accept-Encoding": None 
        }

    page = requests.get(url, headers=headers)
    data = []
    soup = BeautifulSoup(page.text, 'html.parser')
    name = soup.find_all(class_ = "_4rR01T")
    price = soup.find_all(class_ = "_30jeq3 _1_WHN1")
    name_list = []
    price_list = []
    for each in price: 
        for single in name:
            name_list.append(single.get_text())
            price_list.append(each.get_text())
    new_csv = pd.DataFrame({"name" : name_list, "price":price_list})
    new_csv.to_csv("automation/csvinfo/flipkartpriceinfo.csv")
    # tts("saving and opening the info")
    print("saved to flipkartinfo in csvinfo folder")
    os.system("open automation/csvinfo/flipkartpriceinfo.csv")





xd = input("enter the url: ")
srap_from_flipkart(xd)    
