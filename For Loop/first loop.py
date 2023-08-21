successful = True
for number in range(1, 10 , 2):
    print("Attemt", number, (number + 1) * ".")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")