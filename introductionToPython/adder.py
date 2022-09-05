def add(x, y):
    return x + y


def double(x):
    return x + x



def ava(*args):
    total = 0
    for i in  args:
        total += i
        return total / len(args)


cal = ava(1,3,4,5,6,7,8,9)
print(cal)