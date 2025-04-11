def remove_extra_spaces(message):
    cleaned = ' '.join(message.split())
    print(f"Cleaned Message: {cleaned}")
remove_extra_spaces("  This   is   a   message   with   extra    spaces. ")
