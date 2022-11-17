#author- yaz c

class Product:
    def __init__(self, title,description,price):  #dies unless assigned to self
        self.title = title
        self.description = description
        self.price = price

    def get_cost(self):
        return round(self.price * 1.07,2)

    def display(self):
        print(f"""
        *** {self.title}***
            {self.description}
            Price: $ {self.get_cost()}""")



