#Setup database with MongoDB

#Note: This file mostly exists to test connection to the MongoDB server
#As of June 18, this file serves no purpose in the functionality of our app

#from flask import Flask, render_template, request
import pymongo
import sys

#Based on example code from MongoDB
try:
  client = pymongo.MongoClient(mongodb+srv://oestekevin:nbFFcWwiS4OYx5k4@sportsequipmentserver.xsphcuo.mongodb.net/?retryWrites=true&w=majority&appName=sportsEquipmentServer)
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("Error: Could not connect to MongoDB.")
  sys.exit(1)

# use a database named "myDatabase"
db = client.myDatabase

# use a collection named "recipes"
my_collection = db["inventory"]

inventory_documents = []

# drop the collection in case it already exists
try:
  my_collection.drop()  

# return a friendly error if an authentication error is thrown
except pymongo.errors.OperationFailure:
  print("An authentication error was received. Are your username and password correct in your connection string?")
  sys.exit(1)
#add inventory to database
try: 
 result = my_collection.insert_many(inventory_documents)

# return a friendly error if the operation fails
except pymongo.errors.OperationFailure:
  print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
  sys.exit(1)
else:
  inserted_count = len(result.inserted_ids)
  print("Inserted %x items." %(inserted_count))

  print("\n")
