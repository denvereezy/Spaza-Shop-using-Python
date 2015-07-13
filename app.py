from flask.ext.mysqldb import MySQL
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '951022'
app.config['MYSQL_DB'] = 'my_products'




@app.route('/')
def prodList():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT Name from Products''')
	entries = [dict(Name=row[0]) for row in cur.fetchall()]

	cur.execute('''SELECT SUM(Qty) AS TotalQty , Product_Id, Name from Sales s INNER JOIN Products p ON s.Product_Id = p.Id 					GROUP BY Name''')
	products = [dict(Name=row[2],Qty=row[0]) for row in cur.fetchall()]
	
        cur.execute('''SELECT Name from Categories''')
	categories = [dict(Name=row[0]) for row in cur.fetchall()]
       
        cur.execute('''SELECT  Categories.Name, sum(Sales.Qty) AS TotalQty from Sales INNER JOIN Products ON Sales.Product_id = Products.Id INNER JOIN Categories ON Products.Category_id = Categories.Id GROUP BY Categories.Name''')
	cats = [dict(Name=row[0],Qty=row[1]) for row in cur.fetchall()]
	
    	return render_template('menu.html',  entries=entries, products=products, categories=categories, cats=cats)


"""product list with qty sold"""
"""
@app.route('/dee')
def products():
	
	cur.execute('''SELECT SUM(Qty) AS TotalQty , Product_Id, Name from Sales s INNER JOIN Products p ON s.Product_Id = p.Id 					GROUP BY Name''')
	products = [dict(Name=row[2],Qty=row[0]) for row in cur.fetchall()]
    	return render_template('dee.html', products=products)


@app.route('/categorySales')
def categories():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT  Categories.Name, sum(Sales.Qty) AS TotalQty from Sales INNER JOIN Products ON Sales.Product_id = Products.Id INNER JOIN Categories ON Products.Category_id = Categories.Id GROUP BY Categories.Name''')
	entries = [dict(Name=row[0],Qty=row[1]) for row in cur.fetchall()]
    	return render_template('categories.html', entries=entries)


@app.route('/catList')
def catList():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT Name from Categories''')
	entries = [dict(Name=row[0]) for row in cur.fetchall()]
    	return render_template('catList.html', entries=entries)

@app.route('/delete', methods=['DELETE'])
def delete_entry(postID):
    g.db.execute('delete from entries WHERE Id = ?', [postID])
    flash('Entry was deleted')
    return redirect(url_for('/'))""" 


if __name__ == '__main__':
	
	app.run(debug=True, 
	host="172.18.0.78",
    port=int("5000"))
