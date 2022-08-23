x_and_y = []

for x in range(1,6):
    for y in range(1,6):
        x_and_y.append((x_and_y))
print(x_and_y)

#comprehension

x_and_y = [(x, y) for x in range(1,6) for y in range(1,6)]
print(x_and_y)