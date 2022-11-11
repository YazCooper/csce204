#author yaz c

class Person:       #class name are always in uppercase
    def __init__(self,first,last,phone):#constructor(__init__(self))
        self.first = first
        self.last = last
        self.phone = phone

    def display(self):
        print(f"{self.first} {self.last} : {self.phone}")

    def get_phone(self):
        return self.phone

        