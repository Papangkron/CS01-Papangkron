while True:
    user_input = int(input("Enter an integer: "))
    if user_input % 2 != 0:
        print("This number is odd")
        break
    print("This number is even")