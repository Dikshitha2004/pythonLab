inventory = {
    "apple": 10,
    "banana": 5,
    "mango": 7
}

item = input("Enter item to sell: ").lower()
qty = int(input("Enter quantity to sell: "))

if item in inventory:
    if inventory[item] >= qty:
        inventory[item] -= qty
        print(f"{qty} {item}(s) sold. Remaining stock: {inventory[item]}")
    else:
        print("Not enough stock.")
else:
    print("Item not found in inventory.")
