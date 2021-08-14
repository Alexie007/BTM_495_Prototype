from classes.product import Product
from classes.order import Order
from classes.employee import Employee


class Inventory_Order:
    SupplierID: int
    Employee
    Order

#this is to send a notification of new draft order to Warehouse Manager
    def notifyWarehouseManager(cls): 
        return None

    def calcOrderQuantity(cls):
        q = int
        q = Product.MinQuantity - Product.Quantity