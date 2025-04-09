num = int(input("Enter a number: "))
sum_of_digits = 0
original_num = num
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
print(f"Sum of digits of {original_num} is {sum_of_digits}")
