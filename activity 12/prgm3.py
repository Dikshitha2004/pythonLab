my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

try:
    key = input("Enter a key to search in the dictionary: ")
    print(f"The value for '{key}' is {my_dict[key]}")
except KeyError:
    print("Error: Key not found in the dictionary.")
