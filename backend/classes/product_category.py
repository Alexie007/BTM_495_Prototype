from classes.product import Product


class ProductCategory:
    ID: int
    Description: str

    def displayCategory(cls):
        print ("Name", cls.Description)

    