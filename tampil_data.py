<<<<<<< HEAD
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_hp"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM tbkategori")

hasil = cursor.fetchall()

for data in hasil:
    print(data)
=======
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_hp"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM tbkategori")

hasil = cursor.fetchall()

for data in hasil:
    print(data)
>>>>>>> b954615e21c7aee7b61119cd383bcabcd32400a5
    