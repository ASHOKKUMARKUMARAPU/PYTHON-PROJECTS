#!/usr/bin/env python
# coding: utf-8




# import libraries


from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib          #for sending emails




# connect to website 

URL = 'https://www.amazon.in/dp/B09V12K8NT/ref=s9_acsd_al_bw_c2_x_2_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=6CAJRCPFZT555HPANF5V&pf_rd_t=101&pf_rd_p=4714343b-1ee0-4ace-92c1-7115aca5ee21&pf_rd_i=11599648031'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

page = requests.get(URL, headers = headers)

soup1  = BeautifulSoup(page.content, "html.parser")

#print(soup1)

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

#print(soup2)

title = soup2.find(id = 'productTitle').get_text()

ratings = soup2.find(id = 'acrCustomerReviewText').get_text()




# Getting data with Clean up the data a little bit

title = soup2.find(id = 'productTitle').get_text()

title = (title.strip())

print(title)

ratings = soup2.find(id = 'acrCustomerReviewText').get_text()

ratings = (ratings.strip())

print(ratings)


import datetime

today = datetime.date.today()

#print(today)



#create csv dataset to import data into it

import csv

header = ['Title' , 'Ratings', 'Date']
data = [title,ratings,today]


with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# To read the csv

import pandas as pd

df = pd.read_csv(r'C:\Users\K ASHOK KUMAR\Downloads\AmazonWebScraperDataset.csv')

print(df)



# we are appending to this csv

with open('AmazonWebSraperDataset.csv','a+',newline='',encoding ='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)



# To add multiple rows of data under check constraint

def check_ratings():
    
    URL = 'https://www.amazon.in/dp/B09V12K8NT/ref=s9_acsd_al_bw_c2_x_2_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=6CAJRCPFZT555HPANF5V&pf_rd_t=101&pf_rd_p=4714343b-1ee0-4ace-92c1-7115aca5ee21&pf_rd_i=11599648031'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

    page = requests.get(URL, headers = headers)

    soup1  = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    
    title = soup2.find(id = 'productTitle').get_text()

    title = (title.strip())

    ratings = soup2.find(id = 'acrCustomerReviewText').get_text()

    ratings = (ratings.strip())
    
    import datetime

    today = datetime.date.today()
    
    import csv

    header = ['Title' , 'Ratings', 'Date']
    data = [title,ratings,today]


    with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# Runs check_ratings after a set time and inputs data into csv

while(True):
    check_ratings()
    time.sleep(86400)



import pandas as pd

df = pd.read_csv(r'C:\Users\K ASHOK KUMAR\Downloads\AmazonWebScraperDataset.csv')

print(df)




# If you want to receive a mail regarding the price drop

def send_mail():
    server = smptlib.SMTP_SSL(smtp.gmail.com,465)
    server.ehlo()
    server.login('ashokkumarkumarapu@gmail.com','xxxxxxxx')
    
    subject = "The price drop is seen!"
    
    body =  "Ashok, This is the moment you have been waiting for. Now is your chance to pick up the watch of your dreams. Don't mess it up! Link here : https://www.amazon.in/dp/B09V12K8NT/ref=s9_acsd_al_bw_c2_x_2_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=6CAJRCPFZT555HPANF5V&pf_rd_t=101&pf_rd_p=4714343b-1ee0-4ace-92c1-7115aca5ee21&pf_rd_i=11599648031 "
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('ashokkumarkumarapu@gmail.com',msg)





