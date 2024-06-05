from flask import Flask, render_template, request
import pymongo 
from pymongo import MongoClient as mc

#connect to database
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addItem')
def addItem():
    return render_template('addItem.html')

@app.route('/itemAdd', methods = ['POST', 'GET'])
def itemAdd():
    if request.method == 'POST':
        try:
            name = request.form['itemName']
            desc = request.form['itemDescription']
            cat = request.form['itemCategory']
            stock = request.form['itemStock']
            price = request.form['itemPrice']
            
