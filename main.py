def encode(password):
    empty_string = ""
    password = str(password)
    for char in password:
        new_char = (int(char)+3)%10
        empty_string += str(new_char)
    return empty_string