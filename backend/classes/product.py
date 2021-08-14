from tkinter import StringVar

from classes.product_category import ProductCategory


class Product:
    ID: str = '123'
    Name: str
    Price: float
    Status: str
    CategoryID: int
    MinQuantity: int
    Quantity: int
    Order: Order
    Inventory: Inventory
    
    def displaySimilarProduct(cls): #show 3 products in the same category, buttons to click to see product page
        print('product',cls.ID)

    def getPrice(cls): #getprice to quote
        print("Product", cls.Name)

    def searchProducts(cls): #search products in category
        print ("Product", cls.Name)

    def getQuantity(cls):
        print ("Quantity", cls.Quantity)

    def checkInventoryLevel(cls):
        if cls.Quantity>cls.MinQuantity:
            True
        else:
            False

    def updateQuantity(cls):
        cls.Quantity-quote_product.quantity = cls.Quantity

    
