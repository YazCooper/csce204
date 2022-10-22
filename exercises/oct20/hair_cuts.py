#author yaz c


def get_cut_cost(length, thickness):
    cost = 15

    if length > 4:
        cost += 10

    if thickness == "thick":
        cost += 10

    return cost

print("Welcome to our Salon!")

length = int(input("Enter number of inches to remove: "))
thickness = input("Enter (Thick) or (Thin): ").strip().lower()

cost = get_cut_cost(length,thickness)
cost *= 1.07

print(f"Your haircut costs ${round(cost,2)}")