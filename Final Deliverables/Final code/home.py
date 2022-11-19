

from flask import Flask,render_template,redirect, url_for
from flask import request
import sqlite3 as sql





from cloudant.client import Cloudant

client=Cloudant.iam('71ba514f-7497-4541-b670-2cca557572d7-bluemix','jbwiZagjHPeEaY_Ff_WeZowtqr_cjHjP5fUsGtkaqfDH',connect=True)
my_database=client.create_database('my_database')
stock_database=client.create_database('stock_database')

con = sql.connect("database.db",check_same_thread=False)
con.row_factory = sql.Row
cur = con.cursor()

app = Flask(__name__)

@app.route('/')
def login():
   return render_template('login.html')


@app.route('/register')
def register():
   return render_template('register.html')


@app.route("/home")
def home():
    return render_template('home.html')
    #stock balance
@app.route("/stock")
def stock():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Product")
   
   rows = cur.fetchall();
   return  render_template('stock.html',rows = rows) 


#register
@app.route('/afterreg',methods=['POST'])
def afterreg():
    x=[x for x in request.form.values()]
    print(x)
    data={
        '_id':x[1],
        'name':x[0],
        'psw':x[2]
    }
    print(data)
    query={'_id':{'$eq':data['_id']}}
    docs=my_database.get_query_result(query)
    print(docs)

    print(len(docs.all()))

    if(len(docs.all())==0):
        url=my_database.create_document(data)
        return render_template('login.html',pred="Registeration successfull, Please login your details")
    else:
        return render_template('register.html',pred="You re already member, Please login using r details")

#login
@app.route('/afterlogin',methods=['POST'])
def afterlogin():
	user = request.form['_id']
	passw = request.form['psw']
	print(user,passw)
	query = {'_id': {'$eq': user}}
	docs = my_database.get_query_result(query)
	print(docs)
	print(len(docs.all()))
	
	if((user==docs[0][0]['_id'] and passw==docs[0][0]['psw'])):
		return render_template('home.html')
	else:
		print('Invalid User')

 
 
                                  #Product Page
@app.route("/Product")
def Product():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Product")
   
   rows = cur.fetchall();
   return  render_template('Product.html',rows = rows) 

                                #ADD Product
@app.route('/addProduct',methods = ['POST'])
def addProduct():
   if request.method == 'POST':
      try:
         pn = request.form['pn']
         pd = request.form['pd']
         pq = request.form['pq']
        
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Product (productName,productDescription,QTY) VALUES (?,?,?)",(pn,pd,pq) )
            
            con.commit()
            msg = "Record added"
      except:
         con.rollback()
         msg = "error in  operation"
      
      finally:
         
         return redirect(url_for('Product')+"?msg="+msg)
         con.close()
                                  #Edit Product
@app.route('/editProduct',methods = ['POST'])
def editProduct():
   if request.method == 'POST':
      try:
         productID = request.form['ProductID']
         productName = request.form['NEWProductName']
         productDescription=request.form['NEWProductDescription']
         ProductQty=request.form['NEWProductQty']
         cur.execute("UPDATE Product SET productName = ?,productDescription = ?, QTY = ? WHERE productID = ?",(productName,productDescription,ProductQty,productID) )
         
         con.commit()
         msg = "Product Edited "
      except:
         con.rollback()
         msg = "error in operation"
      
      finally:
         return redirect(url_for('Product')+"?msg="+msg)
         con.close()

                                #Delete Product
@app.route('/deleteProduct/<productID>')
def deleteProduct(productID):
      try:
            cur.execute("DELETE FROM Product WHERE productID = ?",(productID,))
            
            con.commit()
            msg = "Product Deleted"
      except:
            con.rollback()
            msg = "error in operation"
   
      finally:
            return redirect(url_for('Product')+"?msg="+msg)
            con.close()

   


if __name__ == '__main__':
    app.run(debug=True)
