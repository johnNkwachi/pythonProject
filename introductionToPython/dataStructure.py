from __future__ import annotations

s1 = ('history', 'biology', 'pol sci', 'comp sci')

print(len(s1))
print(s1[0])
print(s1[1:3])
print(s1[-1])
print(s1[:-1])
print(s1[1:-1])

t = (1,2,3,7,9,0,5)
print(max(t))
print(min(t))
print(sum(t))
print(len(t))

t1 = (1,2,3,7,9,0,5)
t2 = (1,3,22,7,9,0,5)
print(t1 == t2)
print(t1 != t2)
print(t1 > t2)
print(t1 < t2)


def counter(iterable: list | str | tuple)-> dict:
    item_dict = {}

    for item in iterable:
        if item in item_dict:
            item_dict[item] = item_dict[item] + 1
        else:
            item_dict[item] = 1

    return item_dict

print(counter("hello"))
