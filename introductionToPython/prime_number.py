number = int(input("Enter number: "))
if number > 1:
    for p in range(2, number):
        if (number % p)== 0:
            print(number, "the number you entered is not a prime number")
            break
        else:
             print("the number is a prime number")