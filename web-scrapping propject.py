from turtle import distance
from selenium import webdriver
from bs4 import BeautifulSoup
import requests 
import pandas as pd

import csv

stars_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

control=requests.get(stars_url)
soup=BeautifulSoup(control.text,"html.parser")
star_table=soup.find("table")

star_list=[]
table_rows=star_table.find_all("tr")

for i in table_rows:
    td=i.find_all("td")
    r=[i.text.rstrip() for i in td]
    star_list.append(r)


star_names=[]
distances=[]
mass=[]
radius=[]

for i in range(1,len(star_list)):
    star_names.append(star_list[i][1])
    distances.append(star_list[i][3])
    mass.append(star_list[i][5])
    radius.append(star_list[i][6])


df=pd.DataFrame(list(zip(star_names,distances,mass,radius)),columns=["star_names","distance","mass","radius"])
df.to_csv("stars_of_the_universe.csv")
