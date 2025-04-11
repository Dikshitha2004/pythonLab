def traverse_reverse(lst):
    print("Traverse the list in reverse order:")
    for i in range(len(lst)-1, -1, -1):
        print(f"{lst[i]} (original index {i})")
traverse_reverse(['red', 'green', 'white', 'black'])
