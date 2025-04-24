my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index to access the list: "))
    print(f"Value at index {index} is {my_list[index]}")
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid integer.")
