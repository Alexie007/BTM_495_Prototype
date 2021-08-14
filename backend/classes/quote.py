from quote_product import quote_Product


class Quote:
    ID: int
    ProductDetails: Quote_Product
    Subtotal: float
    Tax: float
    Date: str
    Total: float

    #def calcSubtotal(cls): #comment calculer un sous-total avec des attributs qui sont dans une autre classe?

    # def calcLabourCost(cls):

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
