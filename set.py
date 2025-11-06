
# set do not allow duplicates if it is there .It removes
# set enclosed in curly braces

# order of items in the list is not maintained but duplicates are eliminated .

# s = {1,23,452,13,2,2,2}
# print(s,type(s)) # output is {1, 2, 452, 23, 13} <class 'set'>

# s1 = {1,2,5,8,4,"satya"}
# s2 = {4,2,8,6,"bitt"}
# s3=s1.union(s2)
# s4=s1.intersection(s2)
# print(s3)
# print(s4)
#Q1
# dict_2 ={
#     "cat" : "billi",
#     "dog" : "kutta",
#     "elephant" : "hathi"
# }

# search = input("enter the value you want to know the hindi meaning of:")

# print(dict_2.get(search,"No Key found"))

#Q2
# set1 = set()
# s1=input("Enter number:")
# set1.add(s1)
# s2=input("Enter number:")
# set1.add(s2)
# s3=input("Enter number:")
# set1.add(s3)
# s4=input("Enter number:")
# set1.add(s4)
# s5=input("Enter number:")
# set1.add(s5)
# s6=input("Enter number:")
# set1.add(s6)

# print(set1)

#Q3
# s3 = {18,'18',18.0}
# print(s3,type(s3),len(s3))

#Q4

dict_5 = {}
print(dict_5)
sub = input("Enter subject:")
name = input("Enter name:")
dict_5.update({name:sub})
sub = input("Enter subject:")
name = input("Enter name:")
dict_5.update({name:sub})
print(dict_5)