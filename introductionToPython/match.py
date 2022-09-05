print("#################### match ##################")


num = int(input("Enter a number: "))

match num:
    case 1:
        print(1)
    case 2:
        print(2)
    case _:
        print("Don't know you")


match num:
    case _ as x if 1 <= x <= 10:
        print(x)
    case _ as x if 11 <= x <= 20:
        print(x)
    case _:
       print("Don't know you")
