x = int(input("Number: "))
z = 0
n = " "
for number in range(1, x+1):
    if number % 2 !=0:
        z += 1
        n += str(number) + " "
print(n) 