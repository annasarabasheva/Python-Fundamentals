class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        list_letter = []
        for el in self.products:
            if el[0] == first_letter:
                list_letter.append(el)
        return list_letter

    def __repr__(self):
        self.products.sort()
        result = f"Items in the {self.name} catalogue:"
        for el in self.products:
            result += "\n" + el
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

