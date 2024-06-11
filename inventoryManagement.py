#ideally the IDs should auto-increment, or we could 
lastItemId = 0
lastCustomerId = 0
lastOrderId = 0
class Item:
    #Primary Key (changed name from productId to itemId)
    int itemId
    string itemName
    string itemDescription
    string itemCategory
    int stock
    double price

    def __init__(self):
        #Temporary implementation, but we will need to have an auto-incrementing ID number or use something like a GUID
        itemId = lastItemId + 1
        lastItemId = itemId
    #all parameters are optional except for the Item parameter, and you cannot update the itemId as it should not change ever.
    def updateItem(Item item1, string newName = item1.itemName, string newDescription = item1.itemDescription, string newCategory = item1.itemCategory, int newStock = item1.stock, double newPrice = item1.price):
        item1.itemName = newName
        item1.itemDescription = newDescription
        item1.itemCategory = newCategory
        item1.stock = newStock
        item1.price = newPrice
        return item1
    def Item(string itemName, string itemDescription, strnig itemCategory, int stock, double price):
        Item tempItem
        tempItem.itemName = itemName
        tempItem.itemDescription = itemDescription
        tempItem.itemCategory = itemCategory
        tempItem.stock = stock
        tempItem.price = price
        return tempItem
        

class shoppingCart:
    cartItems = []
    #foreign key (Order)
    int orderId
    #foreign key (Item)
    #int itemId
    #int numInCart
    def __init__(self):
        cartItems = [(Item, 1)]
    def addItemToCart(Item i):
        cartItems.append(i)
    

class customer:
    #primary key
    int customerId
    string name
    string address
    string email
    string phone
    def __init__(self):
        customerId = lastCustomerId + 1
        lastCustomerId = customerId
        name = "John Doe"
        address = "123 Road Way"
        email = "johndoe@email.com"
        phone = "123-456-7890"
    def customer(string name1, string address1, string email1, string phone1):
        customer tempCustomer
        tempCustomer.name = name1
        tempCustomer.address = address1
        tempCustomer.email = email1
        tempCustomer.phone = phone1
        return tempCustomer
class order:
    #primary key
    int orderId
    #foreign key customer(customerId)
    int customerId
    double total
    #datetime
    string datePlaced
    shoppingCart cart
    def __init__(self):
        orderId = lastOrderId + 1
        lastOrderId = orderId
        customerId = 0
    def createOrder(customer c):
        customerId = c.customerId
        
        

class shipping:
    string trackingNo
    #foreign key order(orderId)
    int orderId
        
    
