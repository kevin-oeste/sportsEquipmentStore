from flask import Flask, render_template, request
import pymongo as mongo

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
    #temp
    return
