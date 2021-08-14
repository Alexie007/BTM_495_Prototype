import json
import random

from flask import Flask, request
from flask_cors import CORS, cross_origin

from classes.customer import Customer
from data import (getCategories, getCategory, getProduct, getProducts,
                  getQuote, getRawQuote)

HEIGHT = 500
WIDTH = 600

app = Flask(__name__)
cors = CORS(app)

# ROUTES

@app.route("/categories")
@cross_origin()
def categories():
    return getCategories()

@app.route("/category/<categoryId>")
@cross_origin()
def category(categoryId):
    return getCategory(categoryId)

@app.route("/products/<categoryId>")
@cross_origin()
def products(categoryId):
    return getProducts(categoryId)

@app.route("/product/<id>")
@cross_origin()
def product(id):
  return getProduct(id)

@app.route("/quote")
@cross_origin()
def quotes():
    return getQuote()

@app.route("/submitQuote")
@cross_origin()
def submitQuote():
  createOrder(getRawQuote())
  return 'true'
  
@app.route("/order")
@cross_origin()
def order():
  f = open("./data/order.txt", "r")
  return f.read()

@app.route("/customers/<phone>")
@cross_origin()
def customers(phone):
  f = open("./data/customers.txt", "r")
  return Customer.lookupCustomers(f.read(), phone)

@app.route("/customer/<customerId>")
@cross_origin()
def customer(customerId):
  f = open("./data/customers.txt", "r")
  return json.dumps(Customer.getCustomer(f.read(), customerId))

@app.route("/createCustomer/<id>/<fn>/<ln>/<address>/<phone>/<email>")
@cross_origin()
def createCustomer(id, fn, ln, address, phone, email):
  Customer.createCustomer(id, fn, ln, address, phone, email)
  return 'success'

@app.route("/updateCustomer/<customerId>")
@cross_origin()
def updateCustomer(customerId):
  return 'true'

@app.route("/selectCustomer/<customerId>")
@cross_origin()
def selectCustomer(customerId):
  f = open("./data/customers.txt", "r")
  customer = Customer.getCustomer(f.read(), customerId)
  createCustomerOrder(customer)
  return 'success'

@app.route("/confirmOrder")
@cross_origin()
def confirmOrder():
  f = open("./data/customerOrder.txt", "r")
  customerOrder = json.loads(f.read());
  updatedCustomerOrder = {
    'Customer': customerOrder['Customer'],
    'Order': customerOrder['Order'],
    'Status': 'validated'
  }

  g = open("./data/customerOrder.txt", "w")
  g.write(json.dumps(updatedCustomerOrder))

  return 'true'


# UTILS

def createOrder(quote):
  order = {
    'ID': random.randint(1000, 9999999),
    'status': 'draft',
    'quote': quote
  }
  f = open("./data/order.txt", "w")
  f.write(json.dumps(order))
  f.close()

def createCustomerOrder(customer):
  f = open("./data/order.txt", "r")
  order = json.loads(f.read());
  customerOrder = {
    'Customer': customer,
    'Order': order,
    'Status': 'pending'
  }

  g = open("./data/customerOrder.txt", "w")
  g.write(json.dumps(customerOrder))
