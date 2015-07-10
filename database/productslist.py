# view_rows.py - Fetch and display the rows from a MySQL database query

# import the MySQLdb and sys modules
import MySQLdb


# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "localhost", user = "green_grocer", passwd = "password", db = "spaza_shop")

# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.
cursor.execute ("SELECT SUM(Qty) AS TotalQty , Product_Id, Name from Sales s INNER JOIN Products p ON s.Product_Id = p.Id 					GROUP BY Name")

# fetch all of the rows from the query
data = cursor.fetchall ()

# print the rows
for row in data :
 print row[0], row[2]

# close the cursor object
cursor.close ()

# close the connection
connection.close ()


