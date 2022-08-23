import random
count = 0
correct = random.randint(0, 10)
number = 1
print(correct)
while count < 3:
    number = int(input("Guess a number: "))
    if number < correct:
        print("too low")
    elif number > correct:
        print("too high")
    else:
        print("you win")
        break

    count += 1
if number != correct:
     print("you will never get it")