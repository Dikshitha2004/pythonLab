def sum_even_in_range(start, end):
    even_sum = sum(num for num in range(start, end + 1) if num % 2 == 0)
    print(f"Sum of even numbers from {start} to {end} is: {even_sum}")
sum_even_in_range(1, 10)
