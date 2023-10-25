def decoder(password):
    string = ""

    for i in password:
        temp = int(i)
        if temp == 0:
            temp = 7
        elif temp == 1:
            temp = 8
        elif temp == 2:
            temp = 9
        else:
            temp -= 3
        string += str(temp)

    return string


def encoder(password):
    string = ""

    for i in password:
        temp = int(i)
        if temp == 7:
            num = 0
            new = str(num)
            string += new
        elif temp == 8:
            num = 1
            new = str(num)
            string += new
        elif temp == 9:
            num = 2
            new = str(num)
            string += new
        else:
            num = temp + 3
            new = str(num)
            string += new
    return string


def main():
    main = True

    while main == True:

        print(f'Menu\n-------------')
        print(f'1. Encode\n2. Decode\n3. Quit\n')

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)

            print("Your password has been encoded and stored!")
            print(f'{encoded_password}')

        if option == 2:
            password = input("Please enter your password to decode: ")
            decoded_password = decoder(password)

            print("Your password has been decoded and stored!")
            print(f'{decoded_password}')

        if option == 3:
            main = False


if __name__ == "__main__":
    main()
