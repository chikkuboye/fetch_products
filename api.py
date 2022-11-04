import requests
import mysql.connector
import sys
import json

try:
    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'userdb')
except mysql.connector.Error as e:
    sys.exit(e)

mycursor = mydb.cursor()

data = requests.get("https://dummyjson.com/products").text

data_info = json.loads(data)

l = []
for i in data_info:
    l.append(i)
pr = l[0]
dat = data_info[pr]
for i in dat:
#     print(i['title'],i['description'],i['price'],i['discountPercentage'],i['rating'],i['brand'],i['category'])
     price = str(i['price'])
     discountPercentage = str(i['discountPercentage'])
     rating = str(i['rating'])
     sql = "INSERT INTO `rating`(`title`, `Description`, `Price`, `Discount_per`, `Rating`, `Brand`, `Category`) VALUES ('"+i['title']+"','"+i['description']+"','"+price+"','"+discountPercentage+"','"+rating+"','"+i['brand']+"','"+i['category']+"')"
     mycursor.execute(sql)
     mydb.commit()
     print('Inserted succesfully')
