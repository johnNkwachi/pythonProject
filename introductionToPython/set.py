s1 = set("abac")
print(s1)

s2 = {1,2,4}
s3 = {1,3,5}
print(s2.union(s3))

# to check element that appears in the both
# use intersection or &
print(s2.intersection(s3))

# to check the differences between both set
# use difference or -
print(s2.difference(s3))

# symmetric_difference
print(s2.symmetric_difference(s3))

students = {"peter", "john"}
print(students)
students.add("john")
print(students)
students.add("peterson")
print(students)

student1 = {"peter", "johnson", "tim", "hadeeza"}
student2 = {"peter", "johnson", "tim"}
print(student2.issubset(student1))


# dictionary
# add items to dictionary

student ={"111-34-3434": "john"}
student["234-56-9010"] = "Sussan"
student["111-34-3434"] = "Smith"
del student["111-34-3434"]
for key in student:
    print(key + ":" + str(student[key]))
print(student)

