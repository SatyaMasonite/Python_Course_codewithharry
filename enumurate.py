list1= ["guddu","bitt","satya"]
# dic1 ={"name":"satya","age":12}
# a=len(list1)
# print(a,type(a))
# print(list(enumerate(list1)))
# print(enumerate(dic1),list(enumerate(dic1)))


# list3=[]
# list3.append(list(enumerate(list1)))

# print((list3))

for i,value in enumerate(list1):
    if i>0:
        print(f"{i} --> previous value is {list1[i-1]}, current value is {list1[i]}")
    else:
        print(f"{i} --> no previous value,cureent value is {list1[i]}")
        