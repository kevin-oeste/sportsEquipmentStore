from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
#from pymongo_get_database import get_database
import uuid
from bson.objectid import ObjectId

# connect to database
# unfinished

#create a list of ids of inserted items
idList = []

uri = ("mongodb+srv://oestekevin:eVCPjvJrbIU8QWcf@sportsequipmentserver"
         ".xsphcuo.mongodb.net/?retryWrites=true&w=majority&appName=sportsEquipmentServer")
client = MongoClient(uri)

db = client["inventoryDB"]
print("Connected to MongoDB")

inventory = db["inventory"]
cart = db["shoppingCart"]

app = Flask(__name__)

displayRole = "Customer"


# home page
@app.route('/')
def index():
    global displayRole
    return render_template('index.html', methods=['POST', 'GET'], displayRole=displayRole)


# displays addItem webpage
@app.route('/addItem', methods=['POST', 'GET'])
def addItem():
    return render_template('addItem.html')


# unfinished
# Actually adds the item to the database
@app.route('/itemAdd', methods=['POST', 'GET'])
def itemAdd():
    if request.method == 'POST':
        try:
            # get parameters
            #may or may not need this, mongoDB creates ID on every insert
            #itemId = uuid.uuid4()
            name = request.form['itemName']
            desc = request.form['itemDescription']
            cat = request.form['itemCategory']
            stock = request.form['itemStock']
            price = request.form['itemPrice']
            #create dictionary with collected data
            newItem = {'name': name, 'desc': desc, 'cat': cat, 'stock': stock, 'price': price}
            # inserts into mongoDB table
            #global idList
            global inventory
            x = inventory.insert_one(newItem)
            #idList.append({"id": x.inserted_id, "name": name})
            msg = "Item Added."
            #return redirect(url_for('result'))
        except:
            msg = "Error: Item could not be added.\n"
        finally:
            return render_template('result.html', msg=msg)

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if msg is null:
        msg = ""
    return render_template(result.html, msg = msg)
@app.route('/shopping', methods=['POST', 'GET'])
def shopping():
    global displayRole
    return render_template('shopping.html', displayRole=displayRole)


@app.route('/updateInventory', methods=['POST', 'GET'])
def updateInventory():
    global displayRole
    if (displayRole == "Manager"):
        return render_template('updateInventory.html')
    else:
        return render_template('accessDenied.html')


@app.route('/changeRole', methods=['POST', 'GET'])
def changeRole():
    global displayRole
    return render_template('changeRole.html', displayRole=displayRole)


@app.route('/customerRole', methods=['POST', 'GET'])
def customerRole():
    global displayRole
    displayRole = "Customer"
    # add mongoDB role code here
    return render_template('roleGranted.html', displayRole=displayRole)


@app.route('/managerRole', methods=['POST', 'GET'])
def managerRole():
    global displayRole
    displayRole = "Manager"
    # add mongoDB role code here
    return render_template('roleGranted.html', displayRole=displayRole)


@app.route('/accessDenied', methods=['POST', 'GET'])
def accessDenied():
    global displayRole
    return render_template('accessDenied.html', displayRole=displayRole)


@app.route('/removeItem', methods=['POST', 'GET'])
def removeItem():
    global inventory
    items = inventory.find()
    return render_template('removeItem.html', items = items)
@app.route('/itemRemove', methods=['POST', 'GET'])
def itemRemove():
    if(request.method == 'POST'):
        try:
            global inventory
            itemIndex = request.form['itemIndex']
            items = inventory.find()
        except:
            msg = "Error: Item could not be removed.\n"
        finally:
            return render_template('result.html', msg=msg)
@app.post("/<id>/delete/")
def delete(id):
    global inventory
    try:
        inventory.delete_one({"_id":ObjectId(id)})
        msg = "Item Deleted."
    except:
        msg = "Error: Item could not be removed."
    finally:
        return render_template("result.html", msg = msg)
@app.route('/listItems', methods=['POST', 'GET'])
def listItems():
    global inventory
    items = inventory.find()
    msg = ""
    return render_template('listItems.html', msg=msg, items = items)

@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    return render_template('checkout.html')

# Set debug to true for now, but set it to false when we turn it in
if __name__ == "__main__":
    app.run(port=8000, debug=True)


