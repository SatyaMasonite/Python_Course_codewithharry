dict_1 = {
    "name" : "satya",
    "age" : 20
}

for i,(j,k) in enumerate(dict_1.items()):
    print(i ,j,k)

# print(dict_1.items())

# print(tuple(enumerate(dict_1.items())))


# print(dict_1,type(dict_1))
# print(dict_1["age"])

# print(dict_1.get("age"))

# print(dict_1["age2"]) #if the key is not present then this method will give error

# print(dict_1.get("age2"))  # if the key is not present in teh dictionary then returns None

# print(dict_1.items())
# dict_1.update({"salary":2000,"age":30}) # if key is present then it will update its value and if key is not present in the dict it will insert
# print(dict_1)

# dict_1.update({"name":"bitt","height":23})
# print(dict_1)

# print(dict_1.keys())

# print(dict_1.values())

# print(dict_1["age"])

# student = {"name": "Alice", "age": 22, "course": "Math"}
# print(student)
# # student.pop("age2","No Key Found") # if second argument given then error will not be thrown in case key is not found
# # print(student)

# item_deleted = student.popitem()
# print(item_deleted)
# item_deleted = student.popitem()
# print(item_deleted)

# s= {} # to create empty dictionary
# print(type(s))

# d = set() # to create empty set 
# print(type(d))