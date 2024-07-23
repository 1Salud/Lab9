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