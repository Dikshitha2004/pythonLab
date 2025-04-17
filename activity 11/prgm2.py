names = ["Alice", "Arjun", "Bob", "Charlie", "Catherine", "David"]
grouped = {}

for name in names:
    first_letter = name[0]
    if first_letter in grouped:
        grouped[first_letter].append(name)
    else:
        grouped[first_letter] = [name]

print(grouped)
