def generate_invoice(name, product, price):
    print("----- INVOICE -----")
    print(f"Customer Name : {name}")
    print(f"Product       : {product}")
    print(f"Price         : ₹{price:.2f}")
    print("-------------------")
generate_invoice("Rahul Sharma", "Bluetooth Speaker", 2599.99)
