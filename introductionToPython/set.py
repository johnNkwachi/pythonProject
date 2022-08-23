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