def decode(password):
    list = []
    for i in password:
        num = int(i)
        num = num - 3
        stringNum = str(num)
        list.append(stringNum)
    s = ''
    string = s.join(list)
    return string

def encode(password):
    _list = []
    for i in password:
        num = int(i)
        num = num + 3
        stringNum = str(num)
        _list.append(stringNum)
    s = ''
    result = s.join(_list)
    return result


def main():
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")

        user_input = int(input("Please enter an option: "))

        if user_input == 1:
            user_input2 = input("lease enter your password to encode: ")
            encode(user_input2)
            data_storage = encode(user_input2)
            a = data_storage
            print(a)
            print("Your password has been encoded and stored!\n")

        elif user_input == 2:
            result = decode(a)

            print(f"The encoded password is {data_storage} , and the original password is {result}\n")

        elif user_input == 3:

            exit()

if __name__ == '__main__':
    main()