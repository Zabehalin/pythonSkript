import requests
import boto3
from lib.setings import *
from datetime import datetime
import os

URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"

s3 = boto3.resource(
    's3',
    region_name= 'eu-north-1',
    aws_access_key_id= access_key_id,
    aws_secret_access_key= secret_access_key
)

VALUT = requests.get(URL)
VALUT = VALUT.json()

current_datetime = datetime.now()
print(current_datetime)
f1 = open("test.txt", 'a')
f1.write("DATA => " + str(current_datetime) + "\n===============================================================================================================\n")
for item in VALUT:
    print(item['ccy'], item['base_ccy'], item['buy'], item['sale'])
    f1 = open("test.txt", 'a')
    f1.write("ccy =>            "+ str(item['ccy']) + str("      |"))
f1.write("\n")
for item in VALUT:
    f1 = open("test.txt", 'a')
    f1.write("base_ccy =>       "+ str(item['base_ccy']) + str("      |"))
f1.write("\n")
for item in VALUT:
    f1 = open("test.txt", 'a')
    f1.write("buy =>       "+ str(item['buy']) + str("      |"))
f1.write("\n")
for item in VALUT:
    f1 = open("test.txt", 'a')
    f1.write("sale =>       "+ str(item['sale']) + str("     |"))
f1 = open("test.txt", 'a')
f1.write("\n===============================================================================================================\n")
f1 = open('test.txt')
content = f1.read()
s3.Object('ttttttestbacket', 'test.txt').put(Body=content)
f1.close()


