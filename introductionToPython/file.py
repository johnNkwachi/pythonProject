import pathlib

path = pathlib.Path("/home/johnnaas/Documents/MeyerBridge.txt")

my_file = open(path, 'r')

print(path)
print(my_file.read())

home = pathlib.Path.home()
print(home)

