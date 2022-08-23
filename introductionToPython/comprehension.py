squares = []
squares = [i *i for  i in range(1,11)]
print(squares)
names = ['bimpe', 'Banke', 'abimbola', 'Kelechi', 'James', 'Olalekan', 'Racheal']
my_names = []
for name in names:
    if name.istitle():
        my_names.append(name)
print(my_names)

    # OR

names = ['bimpe', 'Banke', 'abimbola', 'Kelechi', 'James', 'Olalekan', 'Racheal']
my_names = [name for name in names if name.istitle()]
print(my_names)


evens = [even for even in range(1,11) if even % 2 ==0]
print(evens)