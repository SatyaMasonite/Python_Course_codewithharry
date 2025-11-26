# def file_input(b):
#     a= input("input any keyword : ")

#     with open("poem.txt") as f:
#         x= f.read()
#         if (b in x):
#             print(f"{b} is present")
#         else:
#             print(f"{b} is not present ")
            


# file_input("twinkle2")

# import random

# def hiscore():
#     a=random.randint(1,120)
#     print(a)

#     with open("hiscore.txt","r+") as f:
#         b=f.read()
#         print(b)
#         if(b==''):
#             score=int(0)
#         else:
#             score=int(b)
#         if(a>score):
#             score=a
#         with open("hiscore.txt","w") as f1:
#             f1.write(str(score))


# hiscore()

# def multi_table(a):
#     tab=''
#     for i in range(1,11):
#         tab += (f"{a}*{i} = {a*i}\n")

#     with open(f"{a}.txt","w") as f:
#         f.write(tab)

# for i in range(1,5):
#     multi_table(i)

def replace_word():
    with open("donkey.txt","r") as f:
        text = f.read()
        replace_text= text.replace("donkey","#####")

    with open("donkey.txt","w") as f2:
        f2.write(replace_text)

replace_word()

