from operator import index

nums = [1,2,3,4,5,6,7,8,9,10]
my_list = []
#for num in nums:
#     my_list.append(num)
#print(num, end=' ')

#my_list = [num**num for num in nums]
#print(my_list)

#for num in nums:
#     if num % 2 ==1:
 #        my_list.append(num)
#print(my_list)

#my_list = [num for num in nums if num % 2 ==0]
#print(my_list)

for letters in 'abcd':
    for num in range(5):
        my_list.append((letters, num))
print(my_list)

my_list = [(letters, num) for letters in 'abcd' for num in range(4)]
print(my_list)

courses = ['art', 'biology', 'physics', 'government']
for index, course in enumerate(courses):
    print(index,course, end=' ')

course = [(index, course) for index in courses for course in courses]
print(index, course, end= '  ')