import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_hp"
)

cursor = db.cursor()

sql = "INSERT INTO tbkategori (nama_kategori) VALUES (%s)"

data = ("Smartphone",)

cursor.execute(sql, data)

db.commit()

print("Data berhasil ditambahkan")