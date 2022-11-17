#author-yaz c

from product import Product


#make list
shoppingList = []      #array ALSO dont put quotes around numbers
shoppingList.append(Product("steak","beef",10))
shoppingList.append(Product("rice","grain",2))
shoppingList.append(Product("carrots","vegetable",3))

print("Your Shopping List")

total = 0 

for item in shoppingList:
    item.display()
    total += item.get_cost()
    print(f"Total Cost: ${round(total,1)}")