list1=["apple","orange","banana","grapes"]
inp=input("Enter list value you want to remove : ")
for i in list1:
    if inp in list1:
        list1.remove(i)

print(list1)