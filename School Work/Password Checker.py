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
    return tuple(lower), tuple(upper), tuple(number), tuple(symbol)
def checkPassword():
    points = 0
    first_lower, first_upper, first_number, first_symbol = True, True, True, True
    lower, upper, number, symbol = allowed()
    password = input("Enter a password:  ")
    if len(password) < 8 or len(password) > 24:
        print("Password is the wrong length")
        menu()
    # Task 3
    for character in password:
        if character in lower:
              if first_lower == True:
                  points += 5
                  first_lower = False
        elif character in upper:
              if first_upper == True:
                  points += 5
                  first_upper = False
        elif character in number:
              if first_number == True:
                  points += 5
                  first_number = False
        elif character in symbol:
              if first_symbol == True:
                  points += 5
                  first_symbol = False
        else:
            print("Invalid character in password")
            menu()
    if first_lower == False and first_upper == False and first_number == False and first_symbol == False:
        points += 10
    elif first_lower == False and first_upper == False and first_number == True and first_symbol == True:
        points -= 5
    
    print("Your password is acceptable")
    
# Task 1
def menu():
    print("1. Check Password")
    print("2. Generate Password")
    print("3. Quit")
    choice = int(input("Enter the number of your choice:  "))
    if choice == 1:
        checkPassword()


menu()
