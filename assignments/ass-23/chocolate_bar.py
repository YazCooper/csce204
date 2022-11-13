#author-yaz c




class ChocolateBar:
    def __init__ (self,title,calories,fat,saturatedfat,protein,carbs,sodium,calcium, nuts):
        self.title = title
        self.calories = calories
        self.fat = fat
        self.saturatedfat = saturatedfat
        self.protein = protein
        self.carbs  = carbs
        self.sodium = sodium
        self.calcium = calcium
        self.nuts = nuts

    def get_title (self):
        return self.title
        
        
    def display(self):
        
        print(f"""
        * {self.title} *
        -calories :{self.calories}
        -fat: {self.fat}
        -saturated fat: {self.saturatedfat}
        -protein: {self.protein}
        -carbs: {self.carbs}
        -sodium: {self.sodium}
        -calcium: {self.calcium}
        """)

    def is_match (self,title):
        if title == self.title:
            return True
        else:
            return False

