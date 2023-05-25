from bs4 import BeautifulSoup
import requests
import mysql.connector

"""

"""
url = 'https://www.imdb.com/chart/top/'

response = requests.get(url)
result = response.content

soup = BeautifulSoup(result,'lxml')




film_name = soup.find_all(class_ = "titleColumn")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="11sql11",
  database="parsing"
)

mycursor = mydb.cursor()


for i in film_name:

    sql = "UPDATE main_films SET name =  %s WHERE id = 1 "


    val = [
            (str(i).split('\n')[2].split('>')[1][:-3]),
    ]

    # print(str(i).split('\n')[2].split('>')[1][:-3])


mycursor.execute(sql, val)

mydb.commit()

print( "Good Joooooob")