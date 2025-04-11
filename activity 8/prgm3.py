def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    print("Duplicate values:", list(duplicates))
find_duplicates([1, 1, 2, 3, 4, 4, 5, 1])
