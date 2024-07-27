def encode(password):
    empty_string = ""
    password = str(password)
    for char in password:
        new_char = (int(char)+3)%10
        empty_string += str(new_char)
    return empty_string

def decode(password):
    decode_password = ""
    password = str(password)
    for char in password:
        changed_char = (int(char) - 3) % 10
        decode_password += str(changed_char)
    return decode_password