def count_vowels(s):
    vowels = "aeiouAEIOU"  
    count = sum(1 for char in s if char in vowels) 
    return count
print(count_vowels("Hello World"))
print(count_vowels("Python"))
print(count_vowels("Beautiful Day")) 
