def split_list(lst, split_length):
    part1 = lst[:split_length]
    part2 = lst[split_length:]
    print("Splitted the list into two parts:", (part1, part2))
split_list([1, 1, 2, 3, 4, 4, 5, 1], 3)
