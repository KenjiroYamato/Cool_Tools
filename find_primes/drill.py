#num = int(input("Enter a number: "))
num = (2**(101)) - 1
numT = abs(num**(1/2)) #division por tentativa del número
flag = False
cont = 0
if num > 1:

    for i in range(2, int(numT)):
        cont += 1
        if (num % i) == 0:

            flag = True
            break

print(cont)
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")