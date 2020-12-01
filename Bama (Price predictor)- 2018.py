# Machine Learning
# Baraye afzayeshe behinegi, va bar asase tosiye rahnamye dore, az database kolliye script 1 estefade nakardam.
# Database az khodroye morede nazar ijad va bar asase an ML anjam mishavad. 
from sklearn import tree
from sklearn import preprocessing
import mysql.connector
import requests
import re
from bs4 import BeautifulSoup
from locale import str

car_name = str (input("Enter the car's name you want to purchase\nBrand and model (eg. 'toyota prius' or 'samand lx')\n(lower case and with a space between the car's brand and model) :    "))
mmileage = int(input("What's your ideal car's mileage?  "))
yyear = int(input("What's your ideal car's production year?   "))
ccity = str(input("from which city would you rather to purchase your car?\n(In Persian)  "))

bra,mod = car_name.split(' ')
mod_database = mod.replace('-','_')

cnx = mysql.connector.connect(user = 'root' , password='ml33327ml' , host = '127.0.0.1' )
cursor = cnx.cursor()
try:
    cursor.execute('CREATE DATABASE db_amiri CHARACTER SET utf8 COLLATE utf8_persian_ci;')
except:
    pass
cursor.execute('USE db_amiri;')
try :
    cursor.execute('CREATE TABLE ml_%s (ID VARCHAR (15), Brand VARCHAR(20) , Model Varchar(30), Trim VARCHAR (30), City VARCHAR(30) ,Year VARCHAR(4), Mileage VARCHAR (10), Price VARCHAR (15), PRIMARY KEY (ID));' % mod_database)
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
            price = re.sub(r'span content=\"\d+\"' , '' , price.text.strip())
            print(id_num)
            print(str(price))
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
                        trim = (car [3])
                    except: 
                        trim = ''
                    print(('%s,%s,%s,%s,%s,%s,%s,%s') % (mod_database , id_num , brand , model , trim ,city ,year ,mileage , price))
                    cursor.execute('USE db_amiri;')
                    try:
                        cursor.execute("INSERT INTO ml_%s VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');" % (mod_database , id_num , brand , model , trim ,city ,year ,mileage , price))
                    except:
                        pass


def fetch_data():
    url = ('https://bama.ir/car/%s/%s/all-trims?hasprice=true&sort=2' %(bra,mod) )
    print(url)
    get_page(url)
    n=2
    while n<=20:
        try:
            urln = ('https://bama.ir/car/%s/%s/all-trims?hasprice=true&sort=2&page=%i' %(bra,mod,n) )            
            print(urln)
            get_page(urln)
            n += 1
        except:
            pass
                
fetch_data()
        
cursor.execute('USE db_amiri;')
cursor.execute("SELECT * FROM ml_%s;" % mod_database )

data = cursor.fetchall()
le = preprocessing.LabelEncoder()

cities = []
for i in data:
    cities.append(i[4])
le.fit(cities)

X=[]
Y=[]
for i in data:
    X.append([le.transform(["%s"%i[4]]),i[5],i[6]])
    Y.append([i[7]])

    
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

new_data = [[le.transform(["%s" % ccity]) , yyear , mmileage ]]
answer = clf.predict(new_data)
answer = int(answer)/1000000
print ("This car probably cost around %i million Tomans. " % answer)
p = input()
    

