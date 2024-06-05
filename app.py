from flask import Flask, render_template, request
import pymongo 
from pymongo import MongoClient as mc
import inventoryManagement as im

#unsure if I will need these in the future, database should handle it
inventory = []
shoppingCart = []

#connect to database
#unfinished
try:
    uri = "mongodb+srv://oestekevin:nbFFcWwiS4OYx5k4@sportsequipmentserver.xsphcuo.mongodb.net/?retryWrites=true&w=majority&appName=sportsEquipmentServer"
    client = mc(uri)
    
    database = client["sportsEquipmentServer"]
    collection = database["ShoppingCart"]

    #Replace with code
    
    client.close()
except Exception as e:
    raise Exception("The following error occured: ", e)
    

app = Flask(__name__)

#home page
@app.route('/')
def index():
    return render_template('index.html')

#displays addItem webpage
@app.route('/addItem')
def addItem():
    return render_template('addItem.html')

#unfinished
#Actually adds the item to the database
@app.route('/itemAdd', methods = ['POST', 'GET'])
def itemAdd():
    if request.method == 'POST':
        try:
            #get parameters
            name = request.form['itemName']
            desc = request.form['itemDescription']
            cat = request.form['itemCategory']
            stock = request.form['itemStock']
            price = request.form['itemPrice']
            #calls parameterized constructor
            inventory.append(im.Item(name, desc, cat, stock, price))
        except:
            msg = "Error: Item could not be added.\n"
        finally:
            return render_template('result.html', msg = msg)

#Set debug to true for now, but set it to false when we turn it in
if __name__ == "__main__":
    app.run(debug = True)
            
