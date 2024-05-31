lastItemId = 0
class Item:
    #Primary Key (changed name from productId to itemId)
    int itemId
    string itemName
    string itemDescription
    string itemCategory
    int stock
    double price

    def Item():
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
        

class shoppingCart:
    cartItems = []
    #foreign key (Order)
    int orderId
    #foreign key (Item)
    int itemId
    int numInCart
    
