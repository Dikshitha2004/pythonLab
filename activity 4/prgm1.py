age = int(input("Enter your age: "))
if age < 5:
    print("Ticket Price: Free")
elif 5 <= age <= 18:
    print("Ticket Price: ₹100")
elif 19 <= age <= 60:
    print("Ticket Price: ₹200")
else:  
    print("Ticket Price: ₹150")
