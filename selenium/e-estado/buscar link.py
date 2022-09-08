#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:06:56 2020

@author: brayan
"""

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import json
from difflib import SequenceMatcher
from selenium import webdriver
import time
from datetime import date
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

link = 'file:///home/brayan/PROJETOS/SPYDER/pegarlink.html'
navegador = webdriver.Firefox()
navegador.get(link)


url = navegador.page_source
soup = BeautifulSoup(url, 'lxml')

a = soup.find("class" == "container-view")

lista = []


for link in a.find_all('a', href=True):
    lista.append(link['href'])
    

df = pd.DataFrame({
    'links': lista,
    })
df.to_csv('links.csv')



#bem = soup.find_all("div",{"class": "container-view"})
#descricao = soup.find_all("h3")[1].text
