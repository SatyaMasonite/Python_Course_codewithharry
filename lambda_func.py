# list2= [2,54,21]
# tup1=(2,3,5)

# l_func = lambda x:x*x
# print(list(map(l_func,list2)))

# def sqr(val):
#     return val*val

# print(list(map(sqr,list2)))

#map(<function lambda or normal>,list/tuple)
# t2=map(l_func,tup1)
# print(list(t2))

#List comphrensation

# list2 = [2,5,1,7]
# list_sqr = [x*x for x in list2 if x != 2]
# print(list_sqr)

list3 = ["saty",2,45,"da","ty",21,True]
list_num_only= [x for x in list3 if isinstance(x,int)]
print(list_num_only)