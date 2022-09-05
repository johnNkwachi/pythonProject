numbers_of_cake = 33
hungry_men = "how many did you eat"
print(hungry_men + " " +str(numbers_of_cake))

print(hungry_men.find("how"))


s =  "some of the stuff"
changed = s.replace("some", "all")
print(changed)


def greet(name):
    print(f"Hello, {name}!")


print(greet("John Nkwachi"))


n = 1
while n < 5:
    print(n)

    n+=1


amount = float(input("Enter an amount: $ "))

for number_of_people in range(2, 6):
    print(f"{number_of_people} people: ${amount / number_of_people: ,.2f} each")


