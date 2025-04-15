all_customers = {"John", "Mary", "Steve", "Ana"}
returned_customers = {"Mary", "Ana"}
never_returned_customers = all_customers - returned_customers
print("Customers who bought but never returned:", never_returned_customers)
