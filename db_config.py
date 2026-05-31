import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_hp"
)

print("Koneksi berhasil")

