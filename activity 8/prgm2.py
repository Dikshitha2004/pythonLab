def find_min_max(lst):
    if not lst:
        print("List is empty.")
        return

    minimum = maximum = lst[0]
    for num in lst[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    print("Smallest:", minimum)
    print("Largest:", maximum)
find_min_max([4, 1, 9, 3, 7])
