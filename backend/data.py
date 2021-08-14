import json
import logging
from json.encoder import JSONEncoder

categories = [
  {
    'Id': 1,
    'Description': 'Ceramic' 
  },
  {
    'Id': 2,
    'Description': 'Natural Stone' 
  }
]

def getCategories():
  return json.dumps(categories)

def getCategory(id):
    for category in categories:
      if str(category['Id']) == id:
        return json.dumps(category)

products = [
  {
    'ID': 1,
    'Name': 'Product 1',
    'Price': 12.99,
    'Status': 'Unavailable',
    'CategoryId': 1,
    'MinQuantity': 250,
    'Quantity': 119
  },
  {
    'ID': 2,
    'Name': 'Product 2',
    'Price': 11.99,
    'Status': 'Unavailable',
    'CategoryId': 1,
    'MinQuantity': 250,
    'Quantity': 104
  },
  {
    'ID': 3,
    'Name': 'Product 3',
    'Price': 12.99,
    'Status': 'In Stock',
    'CategoryId': 1,
    'MinQuantity': 250,
    'Quantity': 624
  },
  {
    'ID': 4,
    'Name': 'Product 4',
    'Price': 15.99,
    'Status': 'In Stock',
    'CategoryId': 1,
    'MinQuantity': 200,
    'Quantity': 438
  },
  {
    'ID': 5,
    'Name': 'Product 5',
    'Price': 10.99,
    'Status': 'In Stock',
    'CategoryId': 1,
    'MinQuantity': 550,
    'Quantity': 1121
  },
  {
    'ID': 6,
    'Name': 'Product 6',
    'Price': 8.99,
    'Status': 'Unavailable',
    'CategoryId': 1,
    'MinQuantity': 1200,
    'Quantity': 567
  },
  {
    'ID': 7,
    'Name': 'Product 7',
    'Price': 24.99,
    'Status': 'In Stock',
    'CategoryId': 1,
    'MinQuantity': 175,
    'Quantity': 204
  },
  {
    'ID': 8,
    'Name': 'Product 8',
    'Price': 20.99,
    'Status': 'Unavailable',
    'CategoryId': 1,
    'MinQuantity': 200,
    'Quantity': 98
  },
  {
    'ID': 9,
    'Name': 'Product 9',
    'Price': 25.99,
    'Status': 'Unavailable',
    'CategoryId': 2,
    'MinQuantity': 200,
    'Quantity': 124
  },
  {
    'ID': 10,
    'Name': 'Product 10',
    'Price': 11.99,
    'Status': 'Unavailable',
    'CategoryId': 2,
    'MinQuantity': 1050,
    'Quantity': 863
  },
  {
    'ID': 11,
    'Name': 'Product 11',
    'Price': 12.99,
    'Status': 'In Stock',
    'CategoryId': 2,
    'MinQuantity': 250,
    'Quantity': 542
  },
  {
    'ID': 12,
    'Name': 'Product 12',
    'Price': 15.99,
    'Status': 'In Stock',
    'CategoryId': 2,
    'MinQuantity': 300,
    'Quantity': 827
  },
  {
    'ID': 13,
    'Name': 'Product 13',
    'Price': 10.99,
    'Status': 'In Stock',
    'CategoryId': 2,
    'MinQuantity': 550,
    'Quantity': 1121
  },
  {
    'ID': 14,
    'Name': 'Product 14',
    'Price': 8.99,
    'Status': 'Unavailable',
    'CategoryId': 2,
    'MinQuantity': 1200,
    'Quantity': 567
  },
  {
    'ID': 15,
    'Name': 'Product 15',
    'Price': 24.99,
    'Status': 'In Stock',
    'CategoryId': 2,
    'MinQuantity': 175,
    'Quantity': 204
  },
  {
    'ID': 16,
    'Name': 'Product 16',
    'Price': 20.99,
    'Status': 'Unavailable',
    'CategoryId': 2,
    'MinQuantity': 200,
    'Quantity': 98
  },
]

def getProducts(categoryId):
  response = []
  for product in products:
    if str(product['CategoryId']) == categoryId:
      response.append(product)
  return json.dumps(response)

def getProduct(id):
  for product in products:
    if str(product['ID']) == id:
      return json.dumps(product)

quotes = {
  'ID': 821012,
  'QuoteProducts': [
    {
      'Quantity': 100,
      'Product': {
        'ID': 3,
        'Name': 'Product 3',
        'Price': 12.99,
        'Status': 'In Stock',
        'CategoryId': 1,
        'MinQuantity': 250,
        'Quantity': 624
      }
    },
    {
      'Quantity': 101,
      'Product': {
        'ID': 4,
        'Name': 'Product 4',
        'Price': 15.99,
        'Status': 'In Stock',
        'CategoryId': 1,
        'MinQuantity': 200,
        'Quantity': 438
      }
    },
    {
      'Quantity': 102,
      'Product': {
        'ID': 5,
        'Name': 'Product 5',
        'Price': 10.99,
        'Status': 'In Stock',
        'CategoryId': 1,
        'MinQuantity': 550,
        'Quantity': 1121
      }
    },
  ],
  'Subtotal': 1000.09,
  'Tax': 150.01,
  'Date': '16/08/2021',
  'Total': 1150.10
}

def getQuote():
  return json.dumps(quotes)

def getRawQuote():
  return quotes

