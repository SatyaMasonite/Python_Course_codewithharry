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
def factorial(n): 
    if (n==1 or n==0):
        return 1
    return n * factorial(n - 1)
a=factorial(5)
print(a)
