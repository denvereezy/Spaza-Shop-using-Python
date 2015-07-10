from flask.ext.mysqldb import MySQL
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '951022'
app.config['MYSQL_DB'] = 'spaza_shop'

@app.route('/')
def main():
    return render_template('menu.html')

@app.route('/products')
def products():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * from Products''')
	entries = [dict(Id=row[2],Name=row[1]) for row in cur.fetchall()]
    	return render_template('products.html', entries=entries)

if __name__ == '__main__':
	
	app.run(debug=True, 
	host="172.18.0.78",
    port=int("5000"))
