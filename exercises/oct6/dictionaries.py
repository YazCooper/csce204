#author-yaz c

#Dictionary
toys = {
    "doll":19.89,
    "car":1.99,
    "truck":7.85,
    "puzzle":14.98,
    "slinky":2.00
}


print(f"A truck costs: ${toys['truck']}")

#add to dictionary
toys["yo-yo"] = 4.50

#loop through and display all the toys in the dictionary
for toyname in toys:
    print(f"{toyname} costs ${toys[toyname]}")