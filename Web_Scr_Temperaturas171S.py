# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 23:07:14 2021

@author: jsala
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url='https://datos.gob.cl/dataset/temperaturas-segundo-semestre-2017'
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
#Obterner URLS de pagina
eq=soup.find_all('a',class_="text-normal text-accent ml-md-3")
#Hacer Lista de Paginas
links=list()
for i in eq:
    data=(i.get('href'))
    links.append((data))
#Extraer info de URLs de página y crear DataFrame consolidado
df=pd.DataFrame()
for x in links:
    csvs=pd.read_csv((x),sep=";")
    df=df.append(csvs)
    
print(df.keys())
#Crear Output
writer = pd.ExcelWriter('Temperatura171S.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()