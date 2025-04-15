sentence = "the sky is blue and the grass is green"
words = sentence.split()
duplicates = len(words) != len(set(words))
print("Has duplicates:", duplicates)
