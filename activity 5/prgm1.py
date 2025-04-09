def remove_char(s, char):
    return s.replace(char, '')
input_string = "hello"
character_to_remove = 'l'

result = remove_char(input_string, character_to_remove)
print("Result:", result)
