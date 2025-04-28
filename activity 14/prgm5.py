import bisect

prices = [10, 20, 30, 50]
position = bisect.bisect(prices, 25)
print("Insert position for 25:", position)
