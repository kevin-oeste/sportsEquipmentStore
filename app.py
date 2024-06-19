from flask import Flask, render_template, request
from pymongo import MongoClient

# connect to database
# unfinished

try:
    uri = "mongodb+srv://oestekevin:nbFFcWwiS4OYx5k4@sportsequipmentserver.xsphcuo.mongodb.net/?retryWrites=true&w=majority&appName=sportsEquipmentServer"
    client = MongoClient(uri)

    db = client.inventoryDB
    inventory = db.inventory
    cart = db.shoppingCart

    # Replace with code

    client.close()
except Exception as e:
    raise Exception("The following error occured: ", e)


app = Flask(__name__)

displayRole = "Customer"

# home page
@app.route('/')
def index():
    global displayRole
    return render_template('index.html', methods=['POST', 'GET'], displayRole = displayRole)


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
            name = request.form['itemName']
            desc = request.form['itemDescription']
            cat = request.form['itemCategory']
            stock = request.form['itemStock']
            price = request.form['itemPrice']
            # calls parameterized constructor
            #inventory.append(im.Item(name, desc, cat, stock, price))
        except:
            msg = "Error: Item could not be added.\n"
        finally:
            return render_template('result.html', msg=msg)

@app.route('/shopping', methods = ['POST', 'GET'])
def shopping():
    global displayRole
    return render_template('shopping.html', displayRole = displayRole)

@app.route('/updateInventory', methods = ['POST', 'GET'])
def updateInventory():
    global displayRole
    if(displayRole == "Manager"):
        return render_template('updateInventory.html')
    else:
        return render_template('accessDenied.html')

@app.route('/changeRole', methods = ['POST', 'GET'])
def changeRole():
    global displayRole
    return render_template('changeRole.html', displayRole = displayRole)
@app.route('/customerRole', methods = ['POST', 'GET'])
def customerRole():
    global displayRole
    displayRole = "Customer"
    #add mongoDB role code here
    return render_template('roleGranted.html',  displayRole = displayRole)
@app.route('/managerRole', methods = ['POST', 'GET'])
def managerRole():
    global displayRole
    displayRole = "Manager"
    #add mongoDB role code here
    return render_template('roleGranted.html',  displayRole = displayRole)
@app.route('/accessDenied', methods = ['POST', 'GET'])
def accessDenied():
    global displayRole
    return render_template('accessDenied.html', displayRole = displayRole)
@app.route('/removeItem', methods = ['POST', 'GET'])
def removeItem():
    return render_template('removeItem.html')
@app.route('/checkout', methods = ['POST', 'GET'])
def checkout():
    return render_template('checkout.html')
# Set debug to true for now, but set it to false when we turn it in
if __name__ == "__main__":
    app.run(port = 8000, debug=True)

