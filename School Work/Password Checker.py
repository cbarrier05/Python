# Task 2
def allowed():
    lower = []
    for i in range(97, 123):
        lower.append(chr(i))
    upper = []
    for i in range(65, 91):
        upper.append(chr(i))
    number = []
    for i in range(48, 58):
        number.append(chr(i))
    symbol = []
    for i in range(36,39):
        symbol.append(chr(i))
    for i in range(40,44):
        symbol.append(chr(i))
    for i in range(94,96):
        symbol.append(chr(i))
    symbol.append(chr(45))
    symbol.append(chr(61))
    symbol.append(chr(33))
    qwerty = [["Q", "q"], ["W", "w"], ["E", "e"], ["R", "r"], ["T", "t"], ["Y", "y"], ["U", "u"],
              ["I", "i"], ["O", "o"], ["P", "p"], ["A", "a"], ["S", "s"], ["D", "d"], ["F", "f"],
              ["G", "g"], ["H", "h"], ["J", "j"], ["K", "k"], ["L", "l"], ["Z", "z"], ["X", "x"],
              ["C", "c"], ["V", "v"], ["B", "b"], ["N", "n"], ["M", "m"]]
    return tuple(lower), tuple(upper), tuple(number), tuple(symbol), tuple(qwerty)


def Consecutive(password, qwerty, points):
    try:
        for char in range(0,len(password)):
            for index1 in range(0,len(qwerty)):
                for index2 in range(0,2):
                    if password[char] == qwerty[index1][index2]:
                        if password[char-1] == qwerty[index1-1][0] or password[char-1] == qwerty[index1-1][1]:
                            if password[char+1] == qwerty[index1+1][0] or password[char+1] == qwerty[index1+1][1]:
                                points -= 5
    except:
        pass
    return points


def checkPassword():
    points = 0
    count_lower, count_upper, count_number, count_symbol = False, False, False, False
    lower, upper, number, symbol, qwerty = allowed()
    password = input("Enter a password:  ")
    if len(password) < 8 or len(password) > 24:
        print("Password is the wrong length")
        menu()
    # Task 3
    for character in password:
        if character in lower:
            if not count_lower:
                points += 5
                count_lower = True
        elif character in upper:
            if not count_upper:
                points += 5
                count_upper = True
        elif character in number:
            if not count_number:
                points += 5
                count_number = True
        elif character in symbol:
            if not count_symbol:
                points += 5
                count_symbol = True
        else:
            print("Invalid character in password")
            menu()
    points += len(password)
    if count_lower and count_upper and count_number and count_symbol:
        points += 10
    elif count_lower and count_upper and not count_number and not count_symbol:
        points -= 5
    elif not count_lower and not count_upper and count_number and not count_symbol:
        points -= 5
    elif not count_lower and not count_upper and not count_number and count_symbol:
        points -= 5
    points = Consecutive(password, qwerty, points)

    if points > 20:
        print("Your password is strong")
    elif points > 0:
        print("Your password is medium")
    else:
        print("Your password is weak")
    print("It scores", points, "points")
    menu()
    
# Task 1
def menu():
    print("1. Check Password")
    print("2. Generate Password")
    print("3. Quit")
    choice = int(input("Enter the number of your choice:  "))
    if choice == 1:
        checkPassword()


menu()
