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
	cur.execute('''SELECT Id,Name from Products''')
	entries = [dict(Id=row[0], Name=row[1]) for row in cur.fetchall()]

	cur.execute('''SELECT SUM(Qty) AS TotalQty , Product_Id, Name from Sales s INNER JOIN Products p ON s.Product_Id = p.Id 					GROUP BY Name''')
	products = [dict(Name=row[2],Qty=row[0]) for row in cur.fetchall()]
	
        cur.execute('''SELECT Id,Name from Categories''')
	categories = [dict(Id=row[0],Name=row[1]) for row in cur.fetchall()]
       
        cur.execute('''SELECT  Categories.Name, sum(Sales.Qty) AS TotalQty from Sales INNER JOIN Products ON Sales.Product_id = Products.Id INNER JOIN Categories ON Products.Category_id = Categories.Id GROUP BY Categories.Name''')
	cats = [dict(Name=row[0],Qty=row[1]) for row in cur.fetchall()]
	
    	return render_template('menu.html',  entries=entries, products=products, categories=categories, cats=cats)

#delete product
@app.route('/delete/<Product_Id>', methods=['GET'])
def delete_product(Product_Id):
        cur = mysql.connection.cursor()
        cur.execute('delete from Products where Id = %s', Product_Id)
        mysql.connection.commit()
        return redirect(url_for('prodList'))

#add product
@app.route('/products/add', methods = ['POST'])
def add_product():
        category_id = request.form['Category_Id']
        product_name = request.form['Product_Name']
        cur = mysql.connection.cursor()
        cur.execute('insert into Products(Category_Id, Name) values( %s, %s)', (category_id, product_name))
        mysql.connection.commit()
        return redirect(url_for('prodList'))

#add category
@app.route('/categories/add', methods = ['POST'])
def add_category():
        category_name =request.form['Name']
        #category_id =request.form['Id']
        cur = mysql.connection.cursor()
        cur.execute('insert into Categories(Name) values( %s)', (category_name))
        mysql.connection.commit()
        return redirect(url_for('prodList'))

#delete category
@app.route('/delete/<Category_Id>', methods=['GET'])
def delete_category(Category_Id):
        cur = mysql.connection.cursor()
        cur.execute('delete from Categories where Id = %s', Category_Id)
        mysql.connection.commit()
        return redirect(url_for('prodList'))

#add sale
@app.route('/sales/add', methods = ['POST'])
def add_sale():
        Sales_date =request.form['Sales_date']
        Qty =request.form['Qty']
        Sales_price =request.form['Sales_price']
        cur = mysql.connection.cursor()
        cur.execute('insert into Sales(Sales_date,Qty,Sales_price) values( %s,%s,%s)', (Sales_date,Qty,Sales_price))
        mysql.connection.commit()
        return redirect(url_for('prodList'))

if __name__ == '__main__':
	
	app.run(debug=True, 
	host="172.18.0.78", 
	port=int("8030"))
