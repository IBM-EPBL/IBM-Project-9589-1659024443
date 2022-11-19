import sqlite3 as sql


conn = sql.connect('database.db')
# print ("Opened database successfully")

# conn.execute('CREATE TABLE Product (productID INTEGER PRIMARY KEY, productName TEXT ,productDescription TEXT,QTY INTEGER)')
# print ("Table Product Done")

# conn.execute('CREATE TABLE locations (locationID INTEGER PRIMARY KEY, locationName TEXT)')
# print ("Table location Done")

conn.execute('UPDATE TABLE product_movement (movementID INTEGER PRIMARY KEY, productName TEXT, Timing timestamp, Validity DATE,QTY INTEGER)')
print ("Table productmovement Done")

# conn.execute("INSERT INTO Product (productName)VALUES('FURNITURE')")
# conn.commit()
# conn.execute("INSERT INTO product (productName)VALUES('GLASS')")
# conn.commit()
# conn.execute("INSERT INTO product (productName)VALUES('STEEL')")
# conn.commit()
# conn.execute("INSERT INTO product (productName,productDescription,QTY)VALUES('PLAYWOOD','IT CONTAIN WOOD DEMO','4')")
# conn.commit()
# conn.execute("INSERT INTO product (productName,productDescription,QTY)VALUES('GLASS','IT Glass is MIRROR ','10')")
# conn.commit()
# conn.close()
# conn.execute("INSERT INTO locations (locationName) VALUES('Mumbai')")
# conn.commit()
# conn.execute("INSERT INTO product_movement (productName,Timing,fromlocation,tolocation,QTY) VALUES('FURNITURE',datetime('now','localtime'),'nagpur','kalyan','2')")
# conn.commit()
# conn.execute("INSERT INTO product_movement (productName,Timing,tolocation,QTY) VALUES('FURNITURE',datetime('now','localtime'),'kalyan','8')")
# conn.commit()
# conn.execute('CREATE TABLE Balance (locationName TEXT, productName TEXT, QTY INTEGER,  PRIMARY KEY (locationName, productName))')


conn.execute("INSERT INTO Balance (locationName,productName,QTY)VALUES('Mumbai','STEEL','10')")
print ("Table balance c successfully")