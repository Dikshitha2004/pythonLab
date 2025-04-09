def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")
count_even_odd([1, 2, 3, 4, 5, 6])
