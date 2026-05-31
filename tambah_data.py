<<<<<<< HEAD
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

=======
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

>>>>>>> b954615e21c7aee7b61119cd383bcabcd32400a5
print("Data berhasil ditambahkan")