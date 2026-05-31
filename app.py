from flask import Flask, render_template
from db_config import db

app = Flask(__name__)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/barang')
def barang():
    cursor.execute("SELECT * FROM barang")
    data = cursor.fetchall()
    return render_template('barang.html', data=data)

@app.route('/penjualan')
def penjualan():
    return render_template('penjualan.html')

@app.route('/pembelian')
def pembelian():
    return render_template('pembelian.html')

if __name__ == '__main__':
    app.run(debug=True)