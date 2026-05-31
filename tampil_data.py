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
    