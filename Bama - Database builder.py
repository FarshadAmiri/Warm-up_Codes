# Ijade database az akharin khodrohaye gozashte shode dar bama (100 safhe akhar)
# Ba estefade az id safahate bama & "Primary key"mysql data tekrari zakhire nemishavad  
import mysql.connector
import requests
import re
from bs4 import BeautifulSoup

cnx = mysql.connector.connect(user = 'root' , password='' , host = '127.0.0.1' )
cursor = cnx.cursor()
try:
    cursor.execute('CREATE DATABASE db_amiri CHARACTER SET utf8 COLLATE utf8_persian_ci;')
except:
    pass
cursor.execute('USE db_amiri;')
try :
    cursor.execute('CREATE TABLE cars (ID VARCHAR (15), Brand VARCHAR(20) , Model Varchar(30), Trim VARCHAR (30), City VARCHAR(30) ,Year VARCHAR(4), Mileage VARCHAR (10), Price VARCHAR (15), PRIMARY KEY (ID));')
except:
    pass

def get_page(url):
    res = requests.get(url, allow_redirects=False)
    soup =  BeautifulSoup (res.text , 'html.parser')
    all_cars = soup.find_all('div' , attrs = {'class' : 'listdata'})
    for i in all_cars:
        id_num = i.find('a' , attrs = {'itemprop' : 'url'})
        id_num = (re.search(r'detail-(\d+)', str(id_num)))[1]
        price = i.find('span' , attrs = {'itemprop' :'price' })
        if price != None:
            price = re.sub(r',' , '' , price.text.strip())
            if str(price).isdigit() == True:
                mileage = i.find('p' , attrs = {'class' :'price hidden-xs' })
                mileage =  re.sub(r' کارکرد (.*) کیلومتر' , '\g<1>' , mileage.text)
                mileage = re.sub(r',' , '',mileage)
                if mileage == 'صفر':
                    mileage = 0
                if str(mileage).isdigit() == True:
                    car = i.find('h2' , attrs = {'itemprop' :'name' })
                    car = re.sub(r'\r\n' , '' , car.text.strip())
                    car = re.sub(r'\s{2,1000}' , ',' , car)
                    car = re.sub(r'،' , '' , car)
                    car = re.sub(r', ' , ',' , car)
                    car = re.sub(r' ,' , ',' , car)
                    car = car.split(',')
                    city = i.find('span' , attrs = {'class' : 'provice-mobile'})
                    city = re.sub(r'،','',city.text)
                    year = (car[0])
                    brand = (car[1])
                    model = (car[2])
                    try:
                        trim = (car[3])
                    except: 
                        trim = ''
                    cursor.execute('USE db_amiri;')
                    try:
                        cursor.execute("INSERT INTO cars VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');" % (id_num , brand , model , trim ,city ,year ,mileage , price))
                    except:
                        pass

def fetch_data():
    url = 'https://bama.ir/car/all-brands/all-models/all-trims?instalment=0&sort=2'
    print(url)
    get_page(url)
    n=2
    while n<= 100:
        urln = ('https://bama.ir/car/all-brands/all-models/all-trims?instalment=0&sort=2&page=%i' % n)
        print(urln)
        get_page(urln)
        n += 1
                
fetch_data()
        
        
        
        
        
        
        
        
        
        
        
        
        