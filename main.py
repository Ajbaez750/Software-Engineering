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
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu = int(input("Please enter an option: "))
        if menu == 1:
            password = input("Please enter your password to encode: ")
            val = encode(password)
            print("Your password has been encoded and stored!")
        elif menu == 2:
            if val:
                decode_password = decode(val)
                print(f"The encoded password is {val}, and the original password is {decode_password}.")
        elif menu == 3:
            break
if __name__ == "__main__":
    main()
