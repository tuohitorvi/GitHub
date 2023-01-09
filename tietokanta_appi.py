# Ohjelma luo tietokannan 'sahkonkulutus.db' johon tallennetaan tietoja sahkonkulutuksesta, lampotilasta ja sahkonhinnasta
# Ohjelman funktioiden avulla saadaan tulostettua kaikki lampotila-arvot seka valitun paivan energiankulutus ja lampotila

import os
import sqlite3

os.remove('sahkonkulutus.db')

db = sqlite3.connect('sahkonkulutus.db')
db.isolation_level = None

def create_tables():
    db.execute("CREATE TABLE Consumption(id INTEGER PRIMARY KEY AUTOINCREMENT, kwh REAL)")
    db.execute("CREATE TABLE Temperatures(id INTEGER PRIMARY KEY AUTOINCREMENT, temp REAL, temp_id INTEGER REFERENCES Consumption)")
    db.execute("CREATE TABLE Prices(id INTEGER PRIMARY KEY AUTOINCREMENT, e_price REAL, price_id INTEGER REFERENCES Consumption)")

def create_consumption(consumption):
    cons = db.execute("INSERT INTO Consumption (kwh) VALUES (?)", [consumption])
    return cons.lastrowid

def create_temperature(temperature):
    t = db.execute("INSERT INTO Temperatures (temp) VALUES (?)", [temperature])
    return t.lastrowid

def create_price(price):
    e_p = db.execute("INSERT INTO Prices (e_price) VALUES (?)", [price])
    return e_p.lastrowid

def read_temp():
    tmp = db.execute("SELECT temp FROM Temperatures T GROUP BY T.temp").fetchall()
    return tmp

def get_temp_and_consumption(day):
    tmp_cons = db.execute("SELECT C.id as pv, C.kwh, T.temp FROM Consumption C JOIN Temperatures T ON C.id=T.temp_id WHERE pv=?", [day]).fetchone()

# Main:

create_tables()

#Tietojen syotto:

i = 1
for i in range(5):
    print("Paiva: ", i)
    cns = float(input("Anna sahkonkulutus: "))
    create_consumption(cns)
    tmpr = float(input("Anna ulkolampotila: "))
    t = create_temperature(tmpr)
    prc = float(input("Anna sahkonhinta: "))
    p = create_price(prc)

#Haetaan annetun paivan (paiva 5) kulutus- ja lampotilalukemat:

print(get_temp_and_consumption(5))

#Tulostetaan kaikki lampotila-arvot:

tmp = [read_temp()]

j = 0
for j in range(len(tmp)):
    tmp[j]  = read_temp()

print(tmp)
