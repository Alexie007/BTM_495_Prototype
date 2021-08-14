
import json
import os


class Customer:
    ID: int
    ShippingAddress: str
    PaymentMethod: str
    Phone: str
    Email: str
    CreationDate: int

    def getCustomer(customers, customerId):
        for customer in json.loads(customers):
          if str(customer['ID']) == customerId:
            return customer

    def lookupCustomers(customers, phone):
        list = []
        for customer in  json.loads(customers):
          if (customer['Phone'] == phone):
            list.append(customer)
        return json.dumps(list) 

    def createCustomer(id, fn, ln, address, phone, email):
        customer = {
          'ID': id,
          "CreationDate": "16/08/2021",
          'PaymentMethod': "Cash",
          'FName': fn,
          'LName': ln,
          'ShippingAddress': address,
          'Phone': phone,
          'Email': email
        }

        # delete last character of json file
        with open("./data/customers.txt", 'rb+') as filehandle:
          filehandle.seek(-1, os.SEEK_END)
          filehandle.truncate()

        # add new customer to json file and close array with ]
        f = open("./data/customers.txt", "a")
        f.write(", " + json.dumps(customer) + "]")
