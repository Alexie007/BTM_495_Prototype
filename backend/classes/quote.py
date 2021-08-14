from backend.classes.quote_product import quote_product
from quote_product import quote_Product


class Quote:
    ID: int
    quote_product
    Subtotal: float
    Tax: float
    Date: str
    Total: float

    def generateQuote(cls):
        print ("Date", cls.Date)
        print ("Quote ID", cls.ID)
        print ("Product Details", cls.ProductDetails)
        print ("Subtotal", cls.Subtotal)
        print ("Tax", cls.Tax)
        print ("Total", cls.Total)

    def getQuoteCost(cls):
        getattr (cls.Total)

    def addProduct(cls):
        getattr (cls.ProductDetails)

    def ConvertQuote(cls):
        return Order
