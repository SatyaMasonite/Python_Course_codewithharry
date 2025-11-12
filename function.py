# def greet_user():
#     a=input("Enter user name:")
#     print(f"Good Day {a}")

# greet_user()

# def greet_user(name):
#     print("Good Day " + name)

# greet_user("Bitt")

# def avg_cal(val1,val2=12):
#     avg= (val1 + val2)/2
#     return avg

# a=avg_cal(10)
# print(a)
# print(a)

#recursive
# def factorial(n): 
#     if (n==1 or n==0):
#         return 1
#     return n * factorial(n - 1)
# a=factorial(5)
# print(a)
# def fun1(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif(b>c and b>a):
#         return b
#     else:
#         return c
    
# f=fun1(10,44,33)
# print(f"{f} is greatest")



# f = ((9/5)*c) +32 #

# def faren(c):
#     return (1.8*c) + 32

# f=faren(20)
# print(f" {f} degree farenheit ")


# print("a")
# print("b",end="")
# print("c")
# print("d",end="")

# def func1(n):
#     if (n==1):
#         return 1
#     return func1(n-1) + n

# print(func1(4))

# def inch_to_cm(inch):
#     return inch*2.54

# print(inch_to_cm(5))

# list1=["apple","orange","banana","grapes"]
# inp=input("Enter list value you want to remove : ")
# if inp in list1:
#     list1.remove(inp)
# print(list1)

def multi_table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i} ")

multi_table(3)